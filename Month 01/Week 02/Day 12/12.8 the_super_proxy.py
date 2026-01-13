
class User:
    def __init__(self, username):
        self.username = username
        self.is_active = True


class Admin(User):
    def __init__(self, username, age):
        super().__init__(username)
        self.age=age

a=Admin("sakib",10)

print(a.username)

#super loads all the property of parents