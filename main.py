from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import queries
from hashlib import sha256

app = FastAPI()

origins = ["*"]

app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)



@app.get("/")
async def home():
	return("Hello, please go to '127.0.0.1:8000/docs' to find the testing page.")


@app.post("/hash_password")
async def get_pass(input_):
	input_ = (f'enter password: ')
	return(sha256(input_.encode('utf-8')).hexdigest())


@app.get("/genres")
async def list_genres():
	genre = queries.get_genres()
	return genre


@app.get("/actors")
async def all_actors():
	actors = queries.list_actors()
	return actors


@app.get("/surnames")
async def list_surnames(last_name_letter):
	letter = str(last_name_letter)
	surname = queries.get_surnames(letter)
	return surname


@app.get("/films")
async def list_films(title):
	filmname = str(title)
	films = queries.get_films(filmname)
	return films


class NewFilm(BaseModel):
	title: str
	description: str
	release_year: str
	language_id: str
	original_language_id: str
	rental_duration: int
	rental_rate: float
	length: int
	replacement_cost: float
	rating: str
	special_features: str

@app.post("/add_film")
async def insert_film(new_film: NewFilm):
	print(new_film)
	new_title = queries.new_film(new_film.__dict__)
	return new_title


@app.get("/features")
async def list_special_features():
	feats = queries.spec_features()
	return feats


@app.get("/filter_features")
async def filter_special_features(feature_name):
	feat = str(feature_name)
	select_feats = queries.filter_feature(feat)
	return select_feats


class PlayTime(BaseModel):
	short_time: int
	long_time: int

@app.post("/playtime")
async def list_times(play_time: PlayTime):
	print(play_time)
	time = queries.get_time(play_time.__dict__)
	return time


@app.get("/rating")
async def list_rating():
	rating = queries.get_rating()
	return rating


@app.get("/rental")
async def list_rentaltime():
	rental = queries.get_rental()
	return rental


@app.get("/shortlistTime")
async def list_short_time():
	time_limit = queries.get_timeSmall()
	return time_limit


@app.get("/language")
async def list_languages():
	language = queries.get_language()
	return language


class NewRent(BaseModel):

	
	inventory_id: int
	customer_id: int
	staff_id: int

@app.post("/new_rental")
async def add_rental(add_rental:NewRent):
	print(add_rental)
	new_rental = queries.new_rent(add_rental.__dict__)
	return new_rental


@app.get("/payments")
async def first_five_payments():
	# customer = str(name)
	payment = queries.get_payments()
	return payment


@app.get("/lw_payments")
async def payments_from_linda_williams():
	lw_pay = queries.get_lw_payments()
	return lw_pay


@app.post("/newadd")
async def add_new_address():
	addr = queries.new_addy()
	return addr


@app.post("/newcust")
async def add_customer():
	customer = queries.new_cust()
	return customer


@app.put("/chg_customer")
async def edit_customer():
	cust_det = queries.upd_cust()
	return cust_det


@app.get("/staff")
async def list_staff():
	staff = queries.get_staff()
	return staff


class NewStaff(BaseModel):
	first_name: str
	last_name: str
	address_id: str
	email: str
	store_id: str
	username: str
	password: str


@app.post("/new_staff")
async def update_staff(new_staff: NewStaff):
	print(new_staff)
	upd_staff = queries.edit_staff(new_staff.__dict__)
	return upd_staff


@app.delete("/remove_staff")
async def delete_staff(enter_name):
	name = str(enter_name)
	rem_staff = queries.remove_staff(name)
	return rem_staff


@app.get("/inventory")
async def get_total_inventory_at_store(store_number):
	s_inv = str(store_number)
	st_inv = queries.inv_by_store(s_inv)
	return st_inv


class StoreAddress(BaseModel):
	address: str
	district: str
	city: str

@app.post("/store_address")
async def add_new_store(store_address: StoreAddress):
	print(store_address)
	new_store = queries.add_address1(store_address.__dict__)
	return new_store


@app.get("/city")
async def list_cities():
	city_list = queries.get_cities()
	return city_list


@app.get("/city_US")
async def list_cities_by_country(enter_country):
	name = str(enter_country)
	us_list = queries.get_us(name)
	return us_list


@app.get("/country")
async def list_countries(country_name):
	name = str(country_name)
	country_list = queries.get_countries(name)
	return country_list
