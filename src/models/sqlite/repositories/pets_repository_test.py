from unittest import mock

import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.exc import NoResultFound

from src.models.sqlite.entities.pets import PetsTable
from .pets_repository import PetsRepository


class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(PetsTable)],  # Query
                    [
                        PetsTable(name="dog", type="dog"),
                        PetsTable(name="cat", type="cat"),
                    ],  # Result
                ),
            ],
        )

    def __enter__(self):
        return self

    def __exit__(self, exctype, excvalue, exctb):
        pass


class MockConnectionWithNoResult:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__raise_no_result_found

    def __raise_no_result_found(self, *args, **kwargs):
        raise NoResultFound("No result found")

    def __enter__(self):
        return self

    def __exit__(self, exctype, excval, exctb):
        pass


def test_list_pets():
    mock_connection = MockConnection()

    pets_repository = PetsRepository(db_connection=mock_connection)
    response = pets_repository.list_pets()

    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.all.assert_called_once()
    mock_connection.session.filter.assert_not_called()

    assert response[0].name == "dog"

def test_delete_pet():
    mock_connection = MockConnection()

    pets_repository = PetsRepository(db_connection=mock_connection)
    pets_repository.delete_pet(name="petName")

    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.filter.assert_called_once_with(PetsTable.name == "petName")
    mock_connection.session.delete.assert_called_once()

def test_list_pets_with_no_result():
    mock_connection_with_no_result = MockConnectionWithNoResult()

    pets_repository = PetsRepository(db_connection=mock_connection_with_no_result)
    response = pets_repository.list_pets()

    mock_connection_with_no_result.session.query.assert_called_once_with(PetsTable)
    mock_connection_with_no_result.session.all.assert_not_called()
    mock_connection_with_no_result.session.filter.assert_not_called()

    assert response == []

def test_delete_pet_error():
    mock_connection_with_no_result = MockConnectionWithNoResult()

    pets_repository = PetsRepository(db_connection=mock_connection_with_no_result)

    with pytest.raises(Exception):
        pets_repository.delete_pet(name="petName")

    mock_connection_with_no_result.session.rollback.assert_called_once()
