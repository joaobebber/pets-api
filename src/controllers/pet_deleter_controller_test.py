from .pet_deleter_controller import PetDeleterController


def test_delete(mocker):
    mock_repository = mocker.Mock()

    pet_deleter_controller = PetDeleterController(pets_repository=mock_repository)
    pet_deleter_controller.delete(name="piggy")

    mock_repository.delete_pet.assert_called_once_with(name="piggy")
