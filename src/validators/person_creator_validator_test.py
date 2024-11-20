from .person_creator_validator import person_creator_validator


class MockRequest:
    def __init__(self, body: dict) -> None:
        self.body = body


def test_person_creator_validator():
    request = MockRequest(body={
        "first_name": "Marco",
        "last_name": "Antonio",
        "age": 3,
        "pet_id": 7,
    })

    person_creator_validator(http_request=request)
