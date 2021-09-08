import pygame

import Main
import Node


def make_grid(maze):
    grid = []
    for i in range(Main.GRID_ROWS):
        grid_row = []
        for j in range(Main.GRID_COLUMNS):
            if maze[i][j] == 1:
                node = Node.Node(i, j, color=Node.BLACK)
            else:
                node = Node.Node(i, j, color=Node.WHITE)
            grid_row.append(node)
        grid.append(grid_row)
    return grid


def draw_grid(window):
    x, y = 0, 0

    for _ in range(Main.GRID_ROWS):
        x += Node.NODE_SIZE_WIDTH
        y += Node.NODE_SIZE_HEIGHT

        pygame.draw.line(window, Node.GREY, (x, 0), (x, Main.WINDOW_SIZE_HEIGHT))
        pygame.draw.line(window, Node.GREY, (0, y), (Main.WINDOW_SIZE_WIDTH, y))


def draw(window, grid, start, end):
    window.fill(Node.WHITE)

    if start is not None:
        start.node_color(start=True)
    if end is not None:
        end.node_color(end=True)

    for row in grid:
        for node in row:
            node.draw(window)
    draw_grid(window)
    pygame.display.update()


def get_clicked_position(position):
    row = position[1] // Node.NODE_SIZE_WIDTH
    column = position[0] // Node.NODE_SIZE_HEIGHT

    return row, column


def update_nodes_neighbours(grid):
    for row in grid:
        for node in row:
            node.update_neighbours(grid)
            if Main.DIFFERENT_NODE_WEIGHTS:
                node.node_weight()
                node.color_by_weight()


def refresh_grid(window, grid, start, end):
    for row in grid:
        for node in row:
            if node.color not in [Node.DARK_BLUE, Node.LIGHT_BLUE, Node.BLACK]:
                node.node_color(walk=True)
                if Main.DIFFERENT_NODE_WEIGHTS:
                    node.color_by_weight()
    draw(window, grid, start, end)


def reconstruct_path(path, current, draw_window):
    path_length, path_cost = 0, 0
    while current in path:
        path_length += 1
        path_cost += current.weight
        current = path[current]
        current.node_color(path=True)
        # draw_window()
    draw_window()
    return path_length, path_cost
