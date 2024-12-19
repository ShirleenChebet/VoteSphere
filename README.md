# VoteSphere
BY SHIRLEEN CHEBET

VoteSphere is a simple voting system implemented in Python using SQLAlchemy for database management. The system allows users to create accounts, register candidates, cast votes, and view results.

## Features

- **User Management**: Create and list users.
- **Candidate Management**: Create and list candidates.
- **Voting System**: Cast votes for candidates.
- **Results Viewing**: Display the list of votes cast.

## Prerequisites

To run this project, ensure you have the following installed:

- Python 3.10+
- Virtual environment tool (e.g., `venv` or `virtualenv`)
- SQLite (or any database supported by SQLAlchemy)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/VoteSphere.git
   cd VoteSphere
   ```

2. Set up a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:

   ```bash
   export PYTHONPATH=$PYTHONPATH:$(pwd)
   python3 lib/models/setup_db.py
   ```

## Usage

Run the CLI to interact with the system:

```bash
python3 lib/cli.py
```

### CLI Options

- `1. Create User`: Register a new user by providing a username and email.
- `2. List Users`: View a list of all registered users.
- `3. Create Candidate`: Add a candidate by providing their name and party.
- `4. List Candidates`: View a list of all candidates.
- `5. Vote`: Cast a vote for a candidate.
- `6. List Votes`: Display all votes cast.
- `0. Exit`: Exit the application.

## Project Structure

The following is the structure of the project:

```
VoteSphere/
├── lib/
│   ├── cli.py             # Main CLI interface for the voting system
│   ├── models/
│   │   ├── __init__.py    # Database models initialization
│   │   ├── setup_db.py    # Script to initialize and set up the database
│   │   ├── user.py        # User model definition
│   │   ├── candidate.py   # Candidate model definition
│   │   ├── vote.py        # Vote model definition
├── requirements.txt       # List of dependencies
├── README.md              # Project documentation
├── LICENSE                # License information
├── venv/                  # Virtual environment directory (optional)
```

## Database Models

### User

| Field      | Type    | Description    |
| ---------- | ------- | -------------- |
| `id`       | Integer | Unique user ID |
| `username` | String  | User's name    |
| `email`    | String  | User's email   |

### Candidate

| Field   | Type    | Description         |
| ------- | ------- | ------------------- |
| `id`    | Integer | Unique candidate ID |
| `name`  | String  | Candidate's name    |
| `party` | String  | Candidate's party   |

### Vote

| Field          | Type    | Description                         |
| -------------- | ------- | ----------------------------------- |
| `id`           | Integer | Unique vote ID                      |
| `user_id`      | Integer | ID of the user casting the vote     |
| `candidate_id` | Integer | ID of the candidate being voted for |

## Example Workflow

1. Create a user:

   ```
   > 1
   Enter username: alice
   Enter email: alice@example.com
   ```

2. Create a candidate:

   ```
   > 3
   Enter candidate name: Bob
   Enter candidate party: Independent
   ```

3. Cast a vote:

   ```
   > 5
   Enter your user ID: 1
   Enter the candidate ID: 1
   ```

4. List votes:

   ```
   > 6
   ```

## Troubleshooting

- **`ModuleNotFoundError: No module named 'lib'`**:
  Ensure the `PYTHONPATH` environment variable is set correctly.

  ```bash
  export PYTHONPATH=$PYTHONPATH:$(pwd)
  ```

- **`sqlite3.OperationalError: no such table`**:
  Ensure you have run the database setup script:

  ```bash
  python3 lib/models/setup_db.py
  ```

## Contributing

Feel free to submit issues or pull requests to improve this project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

