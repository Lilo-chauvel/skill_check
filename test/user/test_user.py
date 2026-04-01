"""Tests pour la classe User."""

import pytest
from src.skill_check import User


class TestUser:
    """Teste la classe User et ses méthodes."""

    def test_user_creation(self):
        """Teste la création d'un utilisateur."""
        user = User("Jean", 1)
        assert user.name == "Jean"
        assert user.id == 1

    def test_user_str(self):
        """Teste la représentation textuelle."""
        user = User("Paul", 2)
        assert "Paul" in str(user)
        assert "2" in str(user)

    def test_user_cannot_validate_by_default(self):
        """Teste que User ne peut pas valider par défaut."""
        user = User("Bob", 3)
        assert user.can_validate(1) is False

