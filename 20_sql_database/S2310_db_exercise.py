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

from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine, select
from sqlalchemy import delete

Database = "sqlite:///S2311_my_second_sql_database.db"
Base = declarative_base()


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


def create_test_data():
    with Session(engine) as session:
        new_items = []
        #  customers
        new_items.append(Customer(name="person 1", address="123 nothington st", age=20))
        new_items.append(Customer(name="person 2", address="321 nothington st", age=23))
        #  products
        new_items.append(Product(product_number=1, price=100, brand="sneakys"))
        new_items.append(Product(product_number=2, price=500, brand="keanys"))

        #  adding it to the database
        session.add_all(new_items)
        session.commit()

def delete_all_records(classparam):
    with Session(engine) as session:
        if classparam == Customer:

        elif classparam == Product:
            Product.delete()
        else:
            print("nothing was deleted")

def select_all(classparam):
    with Session(engine) as session:
        records = session.scalars(select(classparam))
        result = []
        for record in records:
            result.append(record)
    return result


engine = create_engine(Database, echo=False, future=True)
Base.metadata.create_all(engine)

delete_all_records(Customer)

#create_test_data()

print(select_all(Customer))

print()
print()
print()

print(select_all(Product))