import pytest
from main_character import Character, CannotMoveError


@pytest.fixture(scope='module')
def character():
    return Character()


class TestCharacter:

    def test_if_a_new_character_when_created_starts_at_x_0_y0(self, character):
        """Test if a new character starts at x=0 and y=0"""
        assert character.x_pos == 0
        assert character.y_pos == 0

    @pytest.mark.parametrize('value, expected', [(1, 1), (2, 2), (10, 10), (-1, 0)])
    def test_update_the_x_position_of_a_character(self, value, expected, character):
        """Test if the character moves accordinly in X if asked to do so."""
        character.move_to_x(value)
        assert character.x_pos == expected

    def test_update_should_raise_an_cannot_move_error_if_obstacle_present(self, character):
        """If there is an obstacle between the character and the final position raise an error"""
        with pytest.raises(CannotMoveError):
            character.move_to_x(100, obstacles=True)

    def test_update_the_y_position_of_a_character(self, character):
        """Test if the character moves accordingly in y if asked to do so"""
        character.move_to_y(10)
        assert character.y_pos == 10
