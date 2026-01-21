
users = {
    "admin": "admin123",
    "user": "password"
}

# Take user input
username = input("Enter username: ")
password = input("Enter password: ")

# Direct comparison (insecure)
if username in users and users[username] == password:
    print("Login successful")
else:
    print("Invalid credentials")
