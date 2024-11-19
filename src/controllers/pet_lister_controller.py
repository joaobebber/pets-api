from typing import List

from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface
from .interfaces.pet_lister_controller import PetListerControllerInterface


class PetListerController(PetListerControllerInterface):
    def __init__(self, pets_repository: PetsRepositoryInterface) -> None:
        self.__pets_repository = pets_repository

    def list(self) -> dict:
        pets = self.__get_pets_in_db()

        return self.__format_response(pets=pets)

    def __get_pets_in_db(self) -> List[PetsTable]:
        return self.__pets_repository.list_pets()

    def __format_response(self, pets: List[PetsTable]) -> dict:
        formatted_pets = []
        for pet in pets:
            formatted_pets.append({"name": pet.name, "id": pet.id})

        return {
            "data": {
                "type": "Pets",
                "count": len(formatted_pets),
                "attributes": formatted_pets,
            }
        }
