from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.people_repository import PeopleRepository
from src.controllers.person_creator_controller import PersonCreatorController
from src.views.person_creator_view import PersonCreatorView


def person_creator_composer():
    people_repository = PeopleRepository(db_connection=db_connection_handler)
    controller = PersonCreatorController(people_repository=people_repository)
    view = PersonCreatorView(controller=controller)

    return view
