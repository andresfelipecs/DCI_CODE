import pytest
from main_character import Character

@pytest.fixture(scope='module')
def character():
    return Character()
