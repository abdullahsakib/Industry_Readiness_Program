
class Wallet:
    def __init__(self,amount):
        self.amount=amount
    
    def __add__(self,other):
        return self.amount+other.amount
    

w1=Wallet(20)
w2=Wallet(40)

print(w1+w2)
    



        