from .person_finder_controller import PersonFinderController


class MockPerson:
    def __init__(self, first_name: str, last_name: str, pet_name: str, pet_type: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.pet_name = pet_name
        self.pet_type = pet_type


class MockPeopleRepository:
    def get_person(self, person_id: int):  # pylint: disable=unused-argument
        return MockPerson(first_name="John", last_name="Doe", pet_name="Fluffy", pet_type="cat")


def test_find():
    person_finder_controller = PersonFinderController(people_repository=MockPeopleRepository())

    response = person_finder_controller.find(person_id=123)

    assert response == {
        "data": {
            "type": "Person",
            "count": 1,
            "attributes": {
                "first_name": "John",
                "last_name": "Doe",
                "pet_name": "Fluffy",
                "pet_type": "cat",
            }
        }
    }
