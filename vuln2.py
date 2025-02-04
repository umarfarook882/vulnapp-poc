def connect_to_service():
    # Vulnerable to exposure of sensitive data
    username = "admin"
    password = "password123"  # Hardcoded credentials
    print(f"Connecting with {username} and {password}")

connect_to_service()

print("test")
