class User:
    def __init__(self, name: str, id: int):
        self.name: str = name
        self.id: int = id
    def can_validate(self,competence_id: int) -> bool:
        return False