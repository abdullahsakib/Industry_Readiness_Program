
class User:
    def __init__(self,username):
        self.username=username
        self.is_active=True

    def __str__(self):
        return f"user: {self.username}"
    def __repr__(self):
        return f"user: {self.username}, is active:{self.is_active}"
        
    
u1=User("sakib")

print(repr(u1))
    
