import pygame
import Main

NODE_SIZE_WIDTH = Main.WINDOW_SIZE_WIDTH // Main.GRID_COLUMNS
NODE_SIZE_HEIGHT = Main.WINDOW_SIZE_HEIGHT // Main.GRID_ROWS

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARK_BLUE = (0, 0, 139)
LIGHT_BLUE = (173, 216, 230)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
GREY = (128, 128, 128)
LIGHT_GREY = (220, 220, 220)
DARK_GREY = (169, 169, 169)
SILVER = (192, 192, 192)


class Node:
    def __init__(self, row, column, color=WHITE):
        self.row = row
        self.column = column
        self.coordinate = [row * NODE_SIZE_WIDTH, column * NODE_SIZE_HEIGHT]  # x, y coordinate
        self.color = color
        self.weight = 1
        self.neighbours = []

    def get_position(self):
        return self.row, self.column

    def node_color(self, open=False, close=False, walk=False, barrier=False, start=False, end=False, path=False):
        if open:
            self.color = GREEN
        elif close:
            self.color = RED
        elif walk:
            self.color = WHITE
        elif barrier:
            self.color = BLACK
        elif start:
            self.color = DARK_BLUE
        elif end:
            self.color = LIGHT_BLUE
        elif path:
            self.color = PURPLE

    def is_node_barrier(self):
        return self.color == BLACK

    def draw(self, window):
        pygame.draw.rect(window, self.color,
                         (self.coordinate[1], self.coordinate[0], NODE_SIZE_WIDTH, NODE_SIZE_HEIGHT))

    def update_neighbours(self, grid):
        self.neighbours = []
        if self.row < Main.GRID_ROWS - 1 and not grid[self.row + 1][self.column].is_node_barrier():  # Down
            self.neighbours.append(grid[self.row + 1][self.column])

        if self.row > 0 and not grid[self.row - 1][self.column].is_node_barrier():  # Up
            self.neighbours.append(grid[self.row - 1][self.column])

        if self.column < Main.GRID_COLUMNS - 1 and not grid[self.row][self.column + 1].is_node_barrier():  # Right
            self.neighbours.append(grid[self.row][self.column + 1])

        if self.row > 0 and not grid[self.row][self.column - 1].is_node_barrier():  # Left
            self.neighbours.append(grid[self.row][self.column - 1])

        # Checking corner neighbours - optional (change in 'Main.py')
        if Main.CORNER_NEIGHBOURS:
            if self.row < Main.GRID_ROWS - 1 and self.column > 0 and not grid[self.row + 1][self.column - 1].is_node_barrier():  # Left down
                self.neighbours.append(grid[self.row + 1][self.column - 1])

            if self.row > 0 and self.column > 0 and not grid[self.row - 1][self.column - 1].is_node_barrier():  # Left up
                self.neighbours.append(grid[self.row - 1][self.column - 1])

            if self.row < Main.GRID_ROWS - 1 and self.column < Main.GRID_COLUMNS - 1 and not grid[self.row + 1][self.column + 1].is_node_barrier():  # Right down
                self.neighbours.append(grid[self.row + 1][self.column + 1])

            if self.row > 0 and self.column < Main.GRID_COLUMNS - 1 and not grid[self.row - 1][self.column + 1].is_node_barrier():  # Right up
                self.neighbours.append(grid[self.row - 1][self.column + 1])

    def node_weight(self):
        number_of_neighbours = len(self.neighbours)
        if number_of_neighbours == 1:
            self.weight = 5
        else:
            self.weight = len(self.neighbours) - 1

    def color_by_weight(self):
        if self.color == WHITE:
            if self.weight == 1:
                self.color = WHITE
            elif self.weight == 2:
                self.color = LIGHT_GREY
            elif self.weight == 3:
                self.color = DARK_GREY
            else:
                self.color = GREY

    def __lt__(self, other):
        return False
