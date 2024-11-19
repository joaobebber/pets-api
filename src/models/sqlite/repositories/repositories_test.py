import pytest

from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pets_repository import PetsRepository
from src.models.sqlite.repositories.people_repository import PeopleRepository


db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Interação com o banco")
def test_list_pets():
    pets_repository = PetsRepository(db_connection=db_connection_handler)
    response = pets_repository.list_pets()
    print(response)

@pytest.mark.skip(reason="Interação com o banco")
def test_delete_pet():
    pets_repository = PetsRepository(db_connection=db_connection_handler)
    pets_repository.delete_pet(name="belinha")

@pytest.mark.skip(reason="Interação com o banco")
def test_insert_person():
    people_repository = PeopleRepository(db_connection=db_connection_handler)
    people_repository.insert_person(
        first_name="First Name",
        last_name="Last Name",
        age=77,
        pet_id=2,
    )

@pytest.mark.skip(reason="Interação com o banco")
def test_get_person():
    people_repository = PeopleRepository(db_connection=db_connection_handler)
    response = people_repository.get_person(person_id=1)

    print(response.pet_name)
