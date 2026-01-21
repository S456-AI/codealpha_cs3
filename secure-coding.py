
import hashlib

# Store passwords as hashed values
users = {
    "admin": hashlib.sha256("admin123".encode()).hexdigest(),
    "user": hashlib.sha256("password".encode()).hexdigest()
}

# Function to hash input password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Optional: show hashed password for review screenshot
print("Stored hashed password for admin:", users["admin"])

# Take user input with basic validation
username = input("Enter username: ").strip()
password = input("Enter password: ").strip()

if not username or not password:
    print("Invalid input")
else:
    # Compare hashed password (secure)
    if username in users and users[username] == hash_password(password):
        print("Login successful")
    else:
        print("Invalid credentials")
