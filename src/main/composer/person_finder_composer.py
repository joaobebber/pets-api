from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.people_repository import PeopleRepository
from src.controllers.person_finder_controller import PersonFinderController
from src.views.person_finder_view import PersonFinderView


def person_finder_composer():
    people_repository = PeopleRepository(db_connection=db_connection_handler)
    controller = PersonFinderController(people_repository=people_repository)
    view = PersonFinderView(controller=controller)

    return view
