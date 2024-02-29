import mysql.connector
import hashlib

def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="mohan5632",
        database="railway_reservation_system"
    )

def register_user(username, password):
    try:
        db = connect_to_database()
        cursor = db.cursor()

        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        db.commit()
        print("User registered successfully!")

    except mysql.connector.Error as error:
        print("Failed to register user:", error)

    finally:
        if db.is_connected():
            db.close()

def login_user(username, password):
    try:
        db = connect_to_database()
        cursor = db.cursor()

        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, hashed_password))
        user = cursor.fetchone()

        if user:
            print("Login successful!")
        else:
            print("Invalid username or password!")

    except mysql.connector.Error as error:
        print("Failed to login:", error)

    finally:
        if db.is_connected():
            db.close()

def display_trains():
    try:
        db = connect_to_database()
        cursor = db.cursor()

        cursor.execute("SELECT * FROM trains")
        result = cursor.fetchall()
        print("Train ID | Train Name | Source | Destination | AC Seats | Sleeper Seats | Non-AC Seats")
        print("-----------------------------------------------------------------------------------")
        for row in result:
            print(row[0], "|", row[1], "|", row[2], "|", row[3], "|", row[4], "|", row[5], "|", row[6])

    except mysql.connector.Error as error:
        print("Failed to display trains:", error)

    finally:
        if db.is_connected():
            db.close()


def book_ticket(train_id, user_name, num_ac_tickets, num_non_ac_tickets, num_sleeper_tickets):
    try:
        db = connect_to_database()
        cursor = db.cursor()

        cursor.execute("SELECT ac_seats, non_ac_seats, sleeper_seats FROM trains WHERE train_id = %s", (train_id,))
        ac_seats, non_ac_seats, sleeper_seats = cursor.fetchone()
        
        cursor.execute("SELECT SUM(num_ac_tickets), SUM(num_non_ac_tickets), SUM(num_sleeper_tickets) FROM reservations WHERE train_id = %s", (train_id,))
        booked_ac_tickets, booked_non_ac_tickets, booked_sleeper_tickets = cursor.fetchone()

        if booked_ac_tickets is None:
            booked_ac_tickets = 0
        if booked_non_ac_tickets is None:
            booked_non_ac_tickets = 0
        if booked_sleeper_tickets is None:
            booked_sleeper_tickets = 0
        
        available_ac_seats = ac_seats - booked_ac_tickets
        available_non_ac_seats = non_ac_seats - booked_non_ac_tickets
        available_sleeper_seats = sleeper_seats - booked_sleeper_tickets
        
        if available_ac_seats >= num_ac_tickets and available_non_ac_seats >= num_non_ac_tickets and available_sleeper_seats >= num_sleeper_tickets:
            cursor.execute("INSERT INTO reservations (train_id, user_name, num_ac_tickets, num_non_ac_tickets, num_sleeper_tickets) VALUES (%s, %s, %s, %s, %s)", (train_id, user_name, num_ac_tickets, num_non_ac_tickets, num_sleeper_tickets))
            db.commit()
            print("Ticket booked successfully!")
        else:
            print(available_ac_seats)
            print(available_non_ac_seats)
            print( available_sleeper_seats)
            print("Not enough seats available!")

    except mysql.connector.Error as error:
        print("Failed to book ticket:", error)

    finally:
        if db.is_connected():
            db.close()


def main():
    logged_in = False
    while True:
        print("\nRailway Reservation System")
        print("1. Register")
        print("2. Login")
        print("3. View available trains")
        print("4. Book a ticket")
        print("5. Logout")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            username = input("Enter username: ")
            password = input("Enter password: ")
            register_user(username, password)
        elif choice == 2:
            username = input("Enter username: ")
            password = input("Enter password: ")
            logged_in = login_user(username, password)
        elif choice == 3:
            display_trains()
        elif choice == 4:
            if logged_in:
                train_id = int(input("Enter Train ID: "))
                user_name = input("Enter your name: ")
                num_ac_tickets = int(input("Enter number of AC tickets: "))
                num_non_ac_tickets = int(input("Enter number of Non-AC tickets: "))
                num_sleeper_tickets = int(input("Enter number of Sleeper tickets: "))
                book_ticket(train_id, user_name, num_ac_tickets, num_non_ac_tickets, num_sleeper_tickets)
            
            else:
                print("Please login first!")
        elif choice == 5:
            logged_in = False
            print("Logged out successfully!")
        elif choice == 6:
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()