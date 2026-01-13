

class User:
    def __init__(self,username):
        self.username=username
        self.is_active=True
    
u1=User("sakib")
u2=User("rakib")

# self is required because need to know on which object is being called
# self points the specific method that called the method

