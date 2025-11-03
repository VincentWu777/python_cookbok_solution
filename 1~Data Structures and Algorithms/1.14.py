"""
U want to sort objects of the same class, but they don't natively support comparison operations.
"""
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

users = [User(23), User(3), User(99)]
sorted(users, key=lambda u: u.user_id)
