import re

from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface
from src.errors.error_types.http_bad_request import HttpBadRequestError
from .interfaces.person_creator_controller import PersonCreatorControllerInterface


class PersonCreatorController(PersonCreatorControllerInterface):
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
        self.__people_repository = people_repository

    def create(self, person_info: dict) -> dict:
        first_name = person_info["first_name"]
        last_name = person_info["last_name"]
        age = person_info["age"]
        pet_id = person_info["pet_id"]

        self.__validate_name(first_name=first_name, last_name=last_name)

        self.__insert_person_in_db(first_name=first_name, last_name=last_name, age=age, pet_id=pet_id)

        return self.__format_response(person_info=person_info)

    def __validate_name(self, first_name: str, last_name: str) -> None:
        # Regular Expression for non letters chars
        non_valid_chars = re.compile(pattern=r"[^a-zA-Z]")

        if non_valid_chars.search(string=first_name) or non_valid_chars.search(string=last_name):
            raise HttpBadRequestError(message="Invalid person name")

    def __insert_person_in_db(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        self.__people_repository.insert_person(first_name=first_name, last_name=last_name, age=age, pet_id=pet_id)

    def __format_response(self, person_info: dict) -> dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": person_info,
            }
        }
