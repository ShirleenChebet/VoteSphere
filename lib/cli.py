from lib.helpers import (
    create_user,
    create_candidate,
    vote,
    list_users,
    list_candidates,
    exit_program
)

def main():
    while True:
        menu()
        choice = input("> ").strip()
        if choice == "0":
            exit_program()
        elif choice == "1":
            name = input("Enter user name: ").strip()
            create_user(name)
        elif choice == "2":
            name = input("Enter candidate name: ").strip()
            create_candidate(name)
        elif choice == "3":
            try:
                user_id = int(input("Enter user ID: ").strip())
                candidate_id = int(input("Enter candidate ID: ").strip())
                vote(user_id, candidate_id)
            except ValueError:
                print("Invalid input. Please enter numeric IDs.")
        elif choice == "4":
            list_users()
        elif choice == "5":
            list_candidates()
        else:
            print("Invalid choice.")

def menu():
    print("\nPlease select an option:")
    print("0. Exit")
    print("1. Create a User")
    print("2. Create a Candidate")
    print("3. Record a Vote")
    print("4. List All Users")
    print("5. List All Candidates")

if __name__ == "__main__":
    main()
