import pickle

class User:
    def __init__(self , name, age):
        self.name=name
        self.age=age
      
    def __repr__(self):
        return f"name:{self.name}, age: {self.age}"
    

u=User("sakib","31")

with open("user.pkl","wb") as f:
    pickle.dump(u,f)


