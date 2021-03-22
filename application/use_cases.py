from domain.entities import User
from domain.repositories import UserRepository


class UserRetriever:

    def __init__(self, repo: UserRepository):
        self.repo = repo

    def get_user_by_id(self, user_id) -> User:
        user = self.repo.search(user_id)
        return user


class UserCreator:

    def __init__(self, repo: UserRepository):
        self.repo = repo

    def create_user(self, user_name: str, password: str, name: str) -> User:
        user = User(user_name=user_name, password=password, name=name)
        user = self.repo.save(user)
        return user
