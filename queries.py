import sqlite3

# twenty unique queries for use with sakilaDB:


# list genre by name
def get_genres():
    with sqlite3.connect('sakila.db') as conn:
        c = conn.cursor()
        q1 = "SELECT name FROM category;"
        c.execute(q1)
        genres = c.fetchall()
        print(genres)
        return genres

# list actors by name(ORDER BY)


def list_actors():
    with sqlite3.connect('sakila.db') as conn:
        c = conn.cursor()
        q2 = f"SELECT first_name, last_name FROM actor ORDER BY first_name ASC"
        c.execute(q2)
        results = c.fetchall()
        for result in results:
            first_name = result[0]
            last_name = result[1]
            print(f'{first_name} {last_name}')
        return results

# list actors with matching surnames(WHERE, LIKE)


def get_surnames(letter):
    with sqlite3.connect('sakila.db') as conn:
        c = conn.cursor()
        q3 = f"SELECT first_name, last_name FROM actor WHERE last_name LIKE '{letter}%'"
        c.execute(q3)
        results = c.fetchall()
        for result in results:
            first_name = result[0]
            last_name = result[1]
            print(f"{first_name} {last_name}")
        return results

# list films by name


def get_films(name):
    with sqlite3.connect('sakila.db') as conn:
        c = conn.cursor()
        q4 = f"SELECT title FROM film WHERE title LIKE '%{name}%'"
        c.execute(q4)
        results = c.fetchall()
        # for result in results:
        # 	title = result[0]
        # 	print(f"{title}")
    return results

# (INSERT) into film details into film table
def new_film(film: dict):

    title = film["title"]
    desc = film["description"]
    rel = film["release_year"]
    lang = film["language_id"]
    orig = film["original_language_id"]
    renttime = film["rental_duration"]
    rentrate = film["rental_rate"]
    length = film["length"]
    cost = ["replacement_cost"]
    rating = film["rating"]
    spec = film["special_features"]

    with sqlite3.connect('sakila.db') as conn:
        c = conn.cursor()
        q5 = f"INSERT INTO film (title, description, release_year, language_id, original_language_id,	rental_duration, rental_rate, length, rating, special_features, last_update) VALUES ('{title}', '{desc}', '{rel}', '{lang}', '{orig}', '{renttime}', '{rentrate}', '{length}', '{rating}', '{spec}', DATETIME('now'));"
        c.execute(q5)
        results = c.fetchall()
        return results


# list special features
def spec_features():
    with sqlite3.connect('sakila.db') as conn:
        c = conn.cursor()
        q6 = "SELECT title, special_features FROM film"
        c.execute(q6)
        results = c.fetchall()
        return results

# list films with certain special features (WHERE, LIKE)
def filter_feature(feat):
    with sqlite3.connect('sakila.db') as conn:
        c = conn.cursor()
        q7 = f"SELECT title, special_features FROM film WHERE special_features LIKE '{feat}%'"
        c.execute(q7)
        results = c.fetchall()
        for result in results:
            title = result[0]
            special_feature = result[1]
            print(f"{title} {special_feature}")
        return results

# list films by duration (WHERE, BETWEEN) ***
def get_time(time: dict):

    min = time["short_time"]
    max = time["long_time"]


    with sqlite3.connect('sakila.db') as conn:
        c = conn.cursor()
        q8 = f"SELECT title, length FROM film WHERE length BETWEEN '{min}' AND '{max}'"
        c.execute(q8)
        results = c.fetchall()
        # for result in results:
        #     title = result[0]
        #     length = result[2]
        #     print(f"{title} {length}")
        return results


# (q9) list films by rating (ORDER BY)
def get_rating():
    with sqlite3.connect('sakila.db') as conn:
        c = conn.cursor()
        c.execute(
            "SELECT title, description, rating FROM film ORDER BY rating DESC;")
        rated = c.fetchall()
        return rated

# (q10) list films by rental rate (ORDER BY)


def get_rental():
    with sqlite3.connect('sakila.db') as conn:
        c = conn.cursor()
        c.execute(
            "SELECT title, rating, rental_duration FROM film ORDER BY rental_duration DESC LIMIT 20;")
        rent = c.fetchall()
        return rent

# (q11)list films by duration (LIMIT(10))


def get_timeSmall():
    with sqlite3.connect('sakila.db') as conn:
        c = conn.cursor()
        q11 = f"SELECT title as Title, rating as Rating, length as Duration FROM film ORDER BY length DESC LIMIT 10;"
        c.execute(q11)
        time_limit = c.fetchall()
        return time_limit


# (q12) list film languages
def get_language():
    with sqlite3.connect('sakila.db') as conn:
        c = conn.cursor()
        c.execute("SELECT name FROM language;")
        lang = c.fetchall()
        return lang

# add rental(INSERT)


def new_rent(rent: dict):

    inv_id = rent["inventory_id"]
    cust_id = rent["customer_id"]
    staff = rent["staff_id"]

    with sqlite3.connect('sakila.db') as conn:
        c = conn.cursor()
        q13 = f"INSERT INTO rental (rental_date, inventory_id, customer_id, return_date, staff_id, last_update) VALUES (datetime('now'), '{inv_id}', '{cust_id}', datetime('now','+7 days'), '{staff}', datetime('now'));"
        c.execute(q13)
        results = c.fetchall()
        # for result in results:
        #     title = result[0]
        #     length = result[2]
        #     print(f"{title} {length}")
        return results


# list payments made by customer id(JOIN, LIMIT)
def get_payments():
    with sqlite3.connect('sakila.db') as conn:
        c = conn.cursor()
        q14 = f"""SELECT payment.payment_id as Payment, payment.rental_id as Rental, payment.amount as Paid, customer.first_name, customer.last_name 
		FROM payment INNER JOIN customer ON payment.customer_id = customer.customer_id LIMIT 5"""
        c.execute(q14)
        results = c.fetchall()
        # for result in results:
        #     customer.first_name = result
        #     print(f"{customer.first_name}")
        return results

# (q15)list payments made by specific customer(JOIN, WHERE)


def get_lw_payments():
    with sqlite3.connect('sakila.db') as conn:
        c = conn.cursor()
        c.execute("""SELECT payment.payment_id as Payment, payment.rental_id as Rental, payment.amount as Paid, customer.first_name, customer.last_name 
		FROM payment INNER JOIN customer ON payment.customer_id = customer.customer_id WHERE customer.customer_id = '3';""")
        payid = c.fetchall()
        return payid

# add new address(INSERT)
def add_address1(address: dict):

    addy = address["address"]
    dist = address["district"]
    city = address["city"]

    with sqlite3.connect('sakila.db') as conn:
        c = conn.cursor()
        q16 = f"SELECT city_id FROM city WHERE city = '{city}';"
        city_id = c.execute(q16)
        print(city_id)
        q17 = f"INSERT INTO address (address, district, city_id, phone, last_update) VALUES ('{addy}', '{dist}', '{city_id}', '', DATETIME('now'));"
        c.execute(q17)
        results = c.fetchall()
        return results


def new_cust(customer: dict):

    st_id = customer["store_id"]
    fname = customer["first_name"]
    lname = customer["last_name"]
    em = customer["email"]
    ad = customer["address_id"]

    with sqlite3.connect('sakila.db') as conn:
        c = conn.cursor()
        q18 = f"""INSERT INTO customer (store_id, first_name, last_name, email, address_id, active, create_date, last_update) 
		VALUES ('{st_id}', '{fname}', '{lname}', '{em}', '{ad}', '1', DATETIME('now'), DATETIME('now'));"""
        c.execute(q18)
        customer = c.fetchall()
        return customer

# (q19) update customer details(UPDATE)
def upd_cust(email):
    with sqlite3.connect('sakila.db') as conn:
        c = conn.cursor()
        c.execute("""UPDATE customer SET email = '{email}', last_update 
		= DATETIME('now') WHERE customer_id = ;""")
        updated = c.fetchall()
        return updated

# (q20) list staff at store
def get_staff():
    with sqlite3.connect('sakila.db') as conn:
        c = conn.cursor()
        c.execute(
            "SELECT staff.first_name, staff.last_name, staff.store_id FROM staff")
        staff = c.fetchall()
        return staff


def edit_staff(details: dict):

    fname = details["first_name"]
    lname = details["last_name"]
    add = details["address_id"]
    em = details["email"]
    st_id = details["store_id"]
    uname = details["username"]
    pword = details["password"]

    with sqlite3.connect('sakila.db') as conn:
        c = conn.cursor()
        q21a = f"SELECT address_id FROM address WHERE address_id = '{add}';"
        add_id = c.execute(q21a)
        print(add_id)
        q21b = f"INSERT INTO staff (first_name, last_name, address_id, picture, email, store_id, active, username, password, last_update) VALUES ('{fname}', '{lname}', '{add_id}', '', '{em}', '{st_id}', '1', '{uname}', '{pword}', DATETIME('now'));"
        c.execute(q21b)
        results = c.fetchall()
        return results



def remove_staff(name):
    with sqlite3.connect('sakila.db') as conn:
        c = conn.cursor()
        q22 = f"DELETE FROM staff WHERE first_name LIKE '%{name}%';"
        c.execute(q22)
        cut_staff = c.fetchall()
        return cut_staff

# (q23)ist inventory at store?
def inv_by_store(store):
    with sqlite3.connect('sakila.db') as conn:
        c = conn.cursor()
        q23 = f"SELECT COUNT (store_id) FROM inventory WHERE store_id = '{store}';"
        c.execute(q23)
        store_inv = c.fetchall()
        for result in store_inv:
            inv = result[0]
            print("{inv}")
            return store
        return store_inv

# (q24) list cities
def get_cities():
    with sqlite3.connect('sakila.db') as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM city ORDER BY country_id;")
        list_city = c.fetchall()
        return list_city

# (q25)list cities by country(JOIN, LIKE)
def get_us(name):
    with sqlite3.connect('sakila.db') as conn:
        c = conn.cursor()
        q22 = f"""SELECT city.city, city.country_id, country.country 
			FROM city INNER JOIN country ON city.country_id = country.country_id 
			WHERE country.country LIKE '%{name}%';"""
        c.execute(q22)
        list_city = c.fetchall()
        for result in list_city:
            city = result[0]
            print("{city}")
        return list_city


# (q27)list countries
def get_countries(cid):
    with sqlite3.connect('sakila.db') as conn:
        c = conn.cursor()
        q23 = f"SELECT country_id, country FROM country WHERE country LIKE '%{cid}%'"
        c.execute(q23)
        list_country = c.fetchall()
        for result in list_country:
            country_id = result[0]
            country = result[1]
            print(f"{country_id} {country}")
        return list_country
