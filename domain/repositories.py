from abc import ABC, abstractmethod

from domain.entities import User


class UserRepository(ABC):

    @abstractmethod
    def save(self, user: User) -> User:
        pass

    @abstractmethod
    def search(self, user_id: int) -> User:
        pass
