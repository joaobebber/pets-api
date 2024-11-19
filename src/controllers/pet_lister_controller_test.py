from src.models.sqlite.entities.pets import PetsTable
from .pet_lister_controller import PetListerController


class MockPetsRepository:
    def list_pets(self):
        return [
            PetsTable(name="Fluffy", type="cat", id=4),
            PetsTable(name="Buddy", type="dog", id=7),
        ]


def test_find():
    pet_lister_controller = PetListerController(pets_repository=MockPetsRepository())

    response = pet_lister_controller.list()

    assert response == {
        "data": {
            "type": "Pets",
            "count": 2,
            "attributes": [
                {"name": "Fluffy", "id": 4},
                {"name": "Buddy", "id": 7},
            ]
        }
    }
