import pytest
from src.skill_check import Instructor, User

class TestInstructor:
    """Teste la classe Instructor."""

    def test_student_inheritance(self):
        """Teste que Student hérite de User."""
        student = Instructor("Alice", 10)
        assert isinstance(student, User)

    def test_instructor_can_validate_all(self):
        """Teste qu'un Instructor peut valider toute compétence."""
        instructor = Instructor("Prof", 1)
        assert instructor.can_validate(1) is True
        assert instructor.can_validate(999) is True