
class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password 

u =User("sakib","1234")

u.__password="abcd"

print(u.__dict__)

# the real password is not changed