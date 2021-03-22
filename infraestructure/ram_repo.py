from domain.entities import User
from domain.repositories import UserRepository


class RamRepository(UserRepository):

    def __init__(self):
        self.users_map = dict()
        self.index = 0

    def save(self, user: User) -> User:
        self.index += 1
        user.identifier = self.index
        self.users_map[self.index] = user
        return user

    def search(self, user_id: int) -> User:
        return self.users_map.get(user_id)

