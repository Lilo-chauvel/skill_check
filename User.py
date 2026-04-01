class User:
    def __init__(self, name: str, id: int):
        self.name: str = name
        self.id: int = id
    
    def __str__(self) -> str:
        return f"{self.name} have this id : {self.id}\n"

    def can_validate(self,competence_id: int) -> bool:
        return False
    