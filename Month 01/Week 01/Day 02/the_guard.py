

user = None

if user is not None and user.get("access")=="admin":
    print("Access granted")
else:
    print("Access denied")