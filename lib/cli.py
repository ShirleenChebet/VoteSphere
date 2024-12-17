import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user import User

# Configure the database engine and session
DATABASE_URL = "sqlite:///your_database.db"  # Use your actual database URL here
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def main():
    while True:
        print_menu()
        choice = input("> ")
        
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_user()
        elif choice == "2":
            list_users()
        elif choice == "3":
            delete_user()
        else:
            print("Invalid choice, please try again.")

def print_menu():
    print("\nPlease select an option:")
    print("1. Create User")
    print("2. List Users")
    print("3. Delete User")
    print("0. Exit")

def create_user():
    username = input("Enter username: ")
    email = input("Enter email: ")

    # Create a new user
    user = User(username=username, email=email)

    # Add user to session and commit to the database
    session.add(user)
    session.commit()
    
    print(f"User '{username}' created successfully.")

def list_users():
    # Query the users from the database
    users = session.query(User).all()
    
    if not users:
        print("No users found.")
    else:
        for user in users:
            print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}")

def delete_user():
    user_id = input("Enter the ID of the user to delete: ")

    # Query the user by ID
    user = session.query(User).filter(User.id == user_id).first()

    if user:
        session.delete(user)
        session.commit()
        print(f"User '{user.username}' deleted successfully.")
    else:
        print(f"No user found with ID {user_id}.")

def exit_program():
    print("Goodbye!")
    session.close()
    sys.exit()

if __name__ == "__main__":
    main()
