import sys
from lib.models import session, User, Candidate, Vote

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
            create_candidate()
        elif choice == "4":
            list_candidates()
        elif choice == "5":
            vote()
        elif choice == "6":
            list_votes()
        else:
            print("Invalid choice, please try again.")

def print_menu():
    print("\nPlease select an option:")
    print("1. Create User")
    print("2. List Users")
    print("3. Create Candidate")
    print("4. List Candidates")
    print("5. Vote")
    print("6. List Votes")
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

def create_candidate():
    candidate_name = input("Enter candidate name: ")

    # Create a new candidate
    candidate = Candidate(name=candidate_name)

    # Add candidate to session and commit to the database
    session.add(candidate)
    session.commit()
    
    print(f"Candidate '{candidate_name}' created successfully.")

def list_candidates():
    # Query the candidates from the database
    candidates = session.query(Candidate).all()
    
    if not candidates:
        print("No candidates found.")
    else:
        for candidate in candidates:
            print(f"ID: {candidate.id}, Name: {candidate.name}")

def vote():
    user_id = int(input("Enter your User ID: "))
    candidate_id = int(input("Enter Candidate ID to vote for: "))

    # Check if the user and candidate exist
    user = session.query(User).filter_by(id=user_id).first()
    candidate = session.query(Candidate).filter_by(id=candidate_id).first()

    if user and candidate:
        # Create a new vote
        vote = Vote(user_id=user.id, candidate_id=candidate.id)
        session.add(vote)
        session.commit()

        print(f"Vote recorded: User '{user.username}' -> Candidate '{candidate.name}'")
    else:
        print("Invalid User ID or Candidate ID")

def list_votes():
    # List all votes and how many votes each candidate has received
    candidates = session.query(Candidate).all()
    
    for candidate in candidates:
        vote_count = session.query(Vote).filter_by(candidate_id=candidate.id).count()
        print(f"Candidate '{candidate.name}' has {vote_count} votes.")

def exit_program():
    print("Goodbye!")
    session.close()
    sys.exit()

if __name__ == "__main__":
    main()
