
class User:
    def __init__(self,username):
        self.username=username
        self.is_active=True
    
u1=User("sakib")

print(u1.username)
print(u1.is_active)