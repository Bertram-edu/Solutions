"""
Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Anvend det, du har lært i dette kapitel om databaser, på en første opgave.

Trin 1:
Opret en ny SQLite database "S2311_my_second_sql_database.db" i din solutions mappe.
Denne database skal indeholde 2 tabeller.
Den første tabel skal hedde "customers" og repræsenteres i Python-koden af en klasse kaldet "Customer".
Tabellen bruger sin første attribut "id" som primærnøgle.
De andre attributter i tabellen hedder "name", "address" og "age".
Definer selv fornuftige datatyper for attributterne.

Trin 2:
Den anden tabel skal hedde "products" og repræsenteres i Python-koden af en klasse kaldet "Product".
Denne tabel bruger også sin første attribut "id" som primærnøgle.
De andre attributter i tabellen hedder "product_number", "price" og "brand".

Trin 3:
Skriv en funktion create_test_data(), der opretter testdata for begge tabeller.

Trin 4:
Skriv en metode __repr__() for begge dataklasser, så du kan vise poster til testformål med print().

Til læsning fra databasen kan du genbruge de to funktioner select_all() og get_record() fra S2240_db_class_methods.py.

Trin 5:
Skriv hovedprogrammet: Det skriver testdata til databasen, læser dataene fra databasen med select_all() og/eller get_record() og udskriver posterne til konsollen med print().

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-besked til din lærer: <filename> færdig
Fortsæt derefter med den næste fil.
"""
import random

from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine, select
from sqlalchemy import delete

Database = "sqlite:///S2311_my_second_sql_database.db"
Base = declarative_base()

f = open("S2310_db_exercise_customer_names.txt", "r")
temp_customer_names = f.readlines()
f.close()

customer_names = []
for line in temp_customer_names:
    customer_names.append(line.replace("\n", ""))

f = open("S2310_db_exercise_address_names.txt", "r")
temp_address_names = f.readlines()
f.close()

address_names = []
for line in temp_address_names:
    address_names.append(line.replace("\n", ""))

f = open("S2310_db_exercise_brand_names.txt", "r")
temp_brand_names = f.readlines()
f.close()

brand_names = []
for line in temp_brand_names:
    brand_names.append(line.replace("\n", ""))


# print(f"customers: {customer_names} \n\naddresses: {address_names} \n\nbrands: {brand_names}")


class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"Customer({self.id=}    {self.name=}    {self.address=}    {self.age=})"


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)

    product_number = Column(Integer)
    price = Column(Integer)
    brand = Column(String)

    def __repr__(self):
        return f"Product({self.id=}    {self.product_number=}    {self.price=}    {self.brand=})"


def create_test_data(amount_of_customers, amount_of_products, customers_delete_old=False, product_delete_old=False):
    product_counter = 0
    with Session(engine) as session:

        if customers_delete_old is True:
            delete_all_records(Customer)
        if product_delete_old is True:
            delete_all_records(Product)

        new_items = []
        #  customers
        for i in range(amount_of_customers):
            customer_name = random.choice(customer_names)
            address_name = random.choice(address_names)
            customer_age = random.randint(0, 130)
            new_items.append(Customer(name=customer_name, address=address_name, age=customer_age))
        #  products
        for i in range(amount_of_products):
            product_counter += 1
            what_price = random.randint(0, 100)
            what_price *= 100
            brand_name = random.choice(brand_names)
            new_items.append(Product(product_number=product_counter, price=what_price, brand=brand_name))

        #  adding it to the database
        session.add_all(new_items)
        session.commit()


def delete_all_records(classparam):
    with Session(engine) as session:
        if classparam == Customer:
            session.execute(delete(Customer))
            session.commit()
        elif classparam == Product:
            session.execute(delete(Product))
            session.commit()
        else:
            print(f"{classparam} is not a table and therefor nothing was deleted")


def select_all(classparam):
    with Session(engine) as session:
        records = session.scalars(select(classparam))
        result = []
        for record in records:
            result.append(record)
    return result


engine = create_engine(Database, echo=False, future=True)
Base.metadata.create_all(engine)

#  delete_all_records(Customer)
#  delete_all_records(Product)

create_test_data(10, 10, True, True)

print(select_all(Customer))

print("\n\n\n")

print(select_all(Product))
