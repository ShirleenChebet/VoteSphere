from lib.models import session, User, Candidate, Vote

def create_user(name):
    user = User(username=name, email=name + "@example.com")
    session.add(user)
    session.commit()
    print(f"User '{name}' created with ID: {user.id}")

def create_candidate(name):
    candidate = Candidate(name=name)
    session.add(candidate)
    session.commit()
    print(f"Candidate '{name}' created with ID: {candidate.id}")

def vote(user_id, candidate_id):
    user = session.query(User).filter_by(id=user_id).first()
    candidate = session.query(Candidate).filter_by(id=candidate_id).first()
    if user and candidate:
        vote = Vote(user_id=user_id, candidate_id=candidate_id)
        session.add(vote)
        session.commit()
        print(f"Vote recorded: User '{user.username}' -> Candidate '{candidate.name}'")
    else:
        print("Invalid User ID or Candidate ID")

def list_users():
    users = session.query(User).all()
    for user in users:
        print(user)

def list_candidates():
    candidates = session.query(Candidate).all()
    for candidate in candidates:
        print(candidate)

def exit_program():
    print("Goodbye!")
    exit()
