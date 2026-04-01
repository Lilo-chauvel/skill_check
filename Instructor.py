from User import User


class Instructor(User):


    def can_validate(self,competence_id: int) -> bool:
        return True