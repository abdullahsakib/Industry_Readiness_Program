
from datetime import date

class User:
    def __init__(self, username, birth_year):
        self.username = username
        self.birth_year = birth_year

    @property
    def age(self):
        current_year = date.today().year
        return current_year - self.birth_year

u=User("sakib",2000)

print(u.age)