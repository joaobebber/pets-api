from abc import ABC, abstractmethod

from src.models.sqlite.entities.pets import PetsTable


class PetsRepositoryInterface(ABC):
    @abstractmethod
    def list_pets(self) -> list[PetsTable]: pass

    @abstractmethod
    def delete_pet(self, name: str) -> None: pass
