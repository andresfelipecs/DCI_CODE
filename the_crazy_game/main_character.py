class CannotMoveError(Exception):
    pass


class Character:
    
    def __init__(self, x = 0, y = 0) -> None:
        self.x_pos = x 
        self.y_pos = y

    def move_to_x(self, new_position_in_x, obstacles=False):
        if obstacles:
            raise CannotMoveError

        if(new_position_in_x < 0):
            self.x_pos = 0
        else:
            self.x_pos = new_position_in_x

    def move_to_y(self, new_position_in_y):
        self.y_pos = new_position_in_y