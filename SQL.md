Task 1 - Database
=====
-----
**a)**  Tables in the database:
* actor
* address
* category
* city
* country
* customer
* film
* film_actor
* film-category
* film_text
* inventory
* language
* payment
* rental
* sqlite_master
* sql_sequence
* staff
* store

-----

**b)** Data types of entities from the table: 'actor'
* actor_id = auto incrementing INTEGER
* first_name = VARCHAR(45)
* last_name VARCHAR(45)
* last_update TIMESTAMP

-----

**c)** The purpose of the 'autoincrement' is to increase the count every time an entry is made,
it means that when a new row is added, it is assigned a unique id. 
( a condition required by the primary key column )

-----

**d)** The purpose of the 'references' keyword is to point data from one column to an entry in another 
table and check that it's data aligns or the entry cannot be made or changed. The use of the
referential actions following it ( on update cascade on delete restrict ) mean that when there is a change in the values 
that are "referenced" or linked with foreign keys, either upon updating or deletion, 
those values will be affected accordingly.
