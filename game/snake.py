from enum import Enum


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Snake:
    head_color = (255, 255, 255)

    def __init__(self, board, start_x: int, start_y: int, direction: Direction):
        self.head_x = start_x
        self.head_y = start_y
        self.direction = direction
        self.board = board

        board.draw_block(start_x, start_y, self.head_color)

    def face(self, direction: Direction):
        self.direction = direction

    def advance(self):
        # clear old position
        self.board.clear_block(self.head_x, self.head_y)

        # advance position
        if (self.direction == Direction.UP):
            self.head_y = self.head_y - 1
        elif (self.direction == Direction.DOWN):
            self.head_y = self.head_y + 1
        elif (self.direction == Direction.LEFT):
            self.head_x = self.head_x - 1
        elif (self.direction == Direction.RIGHT):
            self.head_x = self.head_x + 1

        # paint at new position
        self.board.draw_block(self.head_x, self.head_y, self.head_color)

    def check_game_over(self) -> bool:
        out_of_y_range = self.head_y < 0 or self.head_y >= self.board.blocks_per_side
        out_of_x_range = self.head_x < 0 or self.head_x >= self.board.blocks_per_side

        return out_of_y_range or out_of_x_range
