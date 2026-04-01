import pytest
from src.skill_check import Student,User


class TestStudent:
    """Teste la classe Student."""

    def test_student_inheritance(self):
        """Teste que Student hérite de User."""
        student = Student("Alice", 10)
        assert isinstance(student, User)

    def test_student_can_validate_competence(self):
        """Teste la validation de compétences pour Student."""
        student = Student("Alice", 10, [1, 2, 3])
        assert student.can_validate(1) is True
        assert student.can_validate(99) is False