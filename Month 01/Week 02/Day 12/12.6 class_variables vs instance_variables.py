

class Name:
    species="human"

    def __init__(self,name):
        self.name=name

u1=Name("A")
u2=Name("B")

#print(u.species)

Name.species="animal"

print(u1.species, u2.species)

u1.species="lion"

print(u1.species, u2.species)

#changing User.species affects everyone. 
#changing u1.species affects only u1. 
