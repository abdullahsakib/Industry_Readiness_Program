
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __eq__(self, other):
        if isinstance(other, User):
            return self.user_id == other.user_id
        return False

u1=User(1)
u2=User(2)

print(u1==u2)