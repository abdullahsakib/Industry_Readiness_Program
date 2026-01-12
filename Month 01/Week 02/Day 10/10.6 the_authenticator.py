
def admin_required(func):
    def wrapper(*args, **kwargs):
        if args[0] != "admin":
            raise PermissionError("Admin access required")
        return func(*args, **kwargs)
    return wrapper

@admin_required
def login(username):
    print("log in  success")

login("admin")
