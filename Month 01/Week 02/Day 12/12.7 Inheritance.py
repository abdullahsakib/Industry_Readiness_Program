
class User:
    def __init__(self, username):
        self.username = username
        self.is_active = True


class Admin(User):
    def delete_db(self):
        print("database deleted")

u=User("sakib")
a=Admin("Rakib")

#u.delete_db()

a.delete_db()