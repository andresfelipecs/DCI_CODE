class Environment:
    
    def __init__(self) -> None:
        self.characters = []

    def add_character(self, character):
        self.characters.append(character)

    def has_character_between(self, x1, x2):
        for character in self.characters:
            if character.x_pos > x1 and character.x_pos < x2:
                return True
            else:
                return False