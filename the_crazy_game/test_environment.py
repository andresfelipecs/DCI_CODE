import pytest

from unittest.mock import Mock

from environment import Environment

@pytest.fixture
def new_environment():
    return Environment()

@pytest.fixture
def populated_environment():
    environment = Environment()
    environment.add_character(Mock(x_pos=1, y_pos=0))
    environment.add_character(Mock(x_pos=1, y_pos=0))
    environment.add_character(Mock(x_pos=1, y_pos=0))
    environment.add_character(Mock(x_pos=1, y_pos=0))
    environment.add_character(Mock(x_pos=1, y_pos=0))


class TestEnvironment:

    def test_if_new_environment_have_no_characters(self):
        """New environment must not contain any characters"""
        enviroment = Environment()
        assert len(enviroment.characters) == 0

    def test_addition_of_character_in_the_environment(self, new_environment):
        """If a new character is give the it needs to be added to the enviroment"""
        character = Mock()
        new_environment.add_character(character)

        assert len(new_environment.characters) == 1
        assert new_environment.characters[0] is character

    def test_should_return_true_if_there_are_characters_between_two_points(self):
        environment = Environment()
        character = Mock(x_pos=100)
        environment.add_character(character)

        result = environment.has_character_between(1, 200)
        assert result == True
