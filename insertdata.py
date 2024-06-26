from datetime import datetime
from app import app, db, User, Ride, RidePassenger

# Manually insert data for user John
from datetime import datetime
from app import app, db, User, Ride, RidePassenger

# Manually insert data for user John
def insert_user1():
    with app.app_context():
        Driver2 = User(
            username='Driver2',
            password='Driver2',
            address='123 Main St',
            email='Driver2@gmail.com',
            age=30,
            birthday=datetime.strptime('1994-05-20', '%Y-%m-%d'),  # Convert string to date object
            gender='Male',
            phone='123-456-7890',
            role='driver'
        )
        db.session.add(Driver2)
        db.session.commit()

# Manually insert data for user Alice
def insert_user2():
    with app.app_context():
        Rider2 = User(
            username='Rider2',
            password='Rider2',
            address='456 Elm St',
            email='Rider2@example.com',
            age=25,
            birthday=datetime.strptime('1999-10-15', '%Y-%m-%d'),  # Convert string to date object
            gender='Female',
            phone='987-654-3210',
            role='rider'
        )
        db.session.add(Rider2)
        db.session.commit()

# Call the insert_user1() and insert_user2() functions


def insert_user3():
    with app.app_context():
        Rider3 = User(
            username='Rider3',
            password='Rider3',
            address='456 Abc St',
            email='Rider3@example.com',
            age=22,
            birthday=datetime.strptime('2001-10-15','%Y-%m-%d'),
            gender='Female',
            phone='897-154-3213',
            role='rider'
        )
        db.session.add(Rider3)
        db.session.commit()

#insert_user1()
#insert_user2()
#insert_user3()

# Manually insert data into the Ride table
def insert_ride(driver, origin, destination, date, time, seats_available):
    with app.app_context():
        new_ride = Ride(driver=driver, origin=origin, destination=destination, date=date, time=time, seats_available=seats_available)
        db.session.add(new_ride)
        db.session.commit()
        print("Ride added successfully!")

# Manually insert data into the RidePassenger table
def insert_ride_passenger(ride_id, passenger_id):
    with app.app_context():
        new_ride_passenger = RidePassenger(ride_id=ride_id, passenger_id=passenger_id)
        db.session.add(new_ride_passenger)
        db.session.commit()
        print("Ride passenger added successfully!")



# Insert a ride
#insert_ride(driver='Driver2', origin='Tampines MRT Station', destination='SIM Global Education', date='2024-03-15', time='08:00', seats_available=3)

# Insert a ride passenger
insert_ride_passenger(ride_id=1, passenger_id=2)
insert_ride_passenger(ride_id=1, passenger_id=3)
