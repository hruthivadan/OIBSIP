import hashlib

# Dictionary to store user information
users = {}

# Function to handle user registration
def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    users[username] = hashed_password
    print("Registration successful!")

# Function to handle user login
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in users and users[username] == hashed_password:
        return True
    else:
        return False

# Function to access secured page
def secured_page():
    print("Welcome to the secured page!")

# Main program loop
while True:
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        if login():
            secured_page()
        else:
            print("Invalid username or password.")
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
