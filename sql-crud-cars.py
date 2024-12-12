from sqlalchemy import (
    create_engine, Column, Integer, String, Float
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Car" table
class Car(base):
    __tablename__ = "Car"
    id = Column(Integer, primary_key=True)
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    price = Column(Float)
    color = Column(String)


# create a session
Session = sessionmaker(db)
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# creating sample car records
tesla_model3 = Car(
    make="Tesla",
    model="Model 3",
    year=2023,
    price=45000.00,
    color="Red"
)

toyota_camry = Car(
    make="Toyota",
    model="Camry",
    year=2022,
    price=25000.00,
    color="Silver"
)

ford_mustang = Car(
    make="Ford",
    model="Mustang",
    year=2023,
    price=35000.00,
    color="Blue"
)

honda_civic = Car(
    make="Honda",
    model="Civic",
    year=2022,
    price=22000.00,
    color="Black"
)


# Add cars to the session (uncomment these lines)
# session.add(tesla_model3)
# session.add(toyota_camry)
# session.add(ford_mustang)
# session.add(honda_civic)
# session.commit()


# Example of updating a single record
# car = session.query(Car).filter_by(id=1).first()
# if car is not None:
#     car.price = 46000.00
#     session.commit()


# Example of updating multiple records
# cars = session.query(Car)
# for car in cars:
#     if car.year == 2022:
#         car.year = 2023
#     session.commit()


# Example of deleting a single record
make = input("Enter car make: ")
model = input("Enter car model: ")
car = session.query(Car).filter_by(make=make, model=model).first()
if car is not None:
    print("Car Found:", car.make, car.model)
    confirmation = input("Are you sure you want to delete this record? (y/n) ")
    if confirmation.lower() == "y":
        session.delete(car)
        session.commit()
        print("Car has been deleted")
    else:
        print("Car not deleted")
else:
    print("No records found")


# Example of deleting all records
# cars = session.query(Car)
# for car in cars:
#     session.delete(car)
#     session.commit()


# Query the database to find all Cars
cars = session.query(Car)
for car in cars:
    print(
        car.id,
        car.make + " " + car.model,
        car.year,
        f"${car.price:,.2f}",
        car.color,
        sep=" | "
    ) 