from sqlalchemy import Column, ForeignKey, String, BIGINT

from src.models.sqlite.settings.base import Base


class PeopleTable(Base):
    __tablename__ = "people"

    id = Column(BIGINT, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(BIGINT, nullable=False)
    pet_id = Column(BIGINT, ForeignKey(column="pets.id"))

    def __repr__(self):
        return f"People [first_name={self.first_name}, last_name={self.last_name}, pet_id={self.pet_id}]"
