from typing import Optional
from user import User


class Student(User):

    def __int__(self, name: str, id: int,validate_competences: Optional[list[int]] = None):
        super().__init__(name,id)
        self.__validate_competences = (validate_competences or [])

    def can_validate(self, competence_id: int) -> bool:
        return competence_id in self.__validate_competences

    def add_competence(self,competence_id: int):
        if competence_id in self.__validate_competences:
            return ValueError
        else:
            self.__validate_competences.insert(competence_id)
            return self
