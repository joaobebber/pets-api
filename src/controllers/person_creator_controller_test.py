import pytest

from .person_creator_controller import PersonCreatorController


class MockPeopleRepository:
    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int):
        pass


def test_create():
    person_info = {
        "first_name": "John",
        "last_name": "Doe",
        "age": 30,
        "pet_id": 123,
    }

    person_creator_controller = PersonCreatorController(people_repository=MockPeopleRepository())

    response = person_creator_controller.create(person_info=person_info)

    assert response["data"]["type"] == "Person"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == person_info

def test_create_error():
    person_info = {
        "first_name": "John",
        "last_name": "Doe Example",
        "age": 30,
        "pet_id": 123,
    }

    person_creator_controller = PersonCreatorController(people_repository=MockPeopleRepository())

    with pytest.raises(Exception):
        person_creator_controller.create(person_info=person_info)
