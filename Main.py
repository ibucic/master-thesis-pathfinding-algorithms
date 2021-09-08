import pygame
import time

import AStar
import BFS
import DFS
import Dijkstra
import Grid
import MazeGenerator

WINDOW_SIZE_WIDTH = 1024
WINDOW_SIZE_HEIGHT = 1024
GRID_ROWS = 64
GRID_COLUMNS = 64

CORNER_NEIGHBOURS = False
DIFFERENT_NODE_WEIGHTS = False


def main():
    maze = MazeGenerator.random_maze_generator()
    # maze = MazeGenerator.maze_generator()
    grid = Grid.make_grid(maze)
    window = pygame.display.set_mode((WINDOW_SIZE_WIDTH, WINDOW_SIZE_HEIGHT))
    pygame.display.set_caption("Path Finding Algorithm")

    start, end = None, None
    run, started = True, False

    Grid.update_nodes_neighbours(grid)
    while run:
        if not started:
            Grid.refresh_grid(window, grid, start, end)
        Grid.draw(window, grid, start, end)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed(num_buttons=3)[0]:  # Left mouse click
                started = False
                position = pygame.mouse.get_pos()
                row, column = Grid.get_clicked_position(position)
                node = grid[row][column]
                if not start and node != end:
                    start = node
                    start.node_color(start=True)
                elif not end and node != start:
                    end = node
                    end.node_color(end=True)
                elif node != start and node != end:
                    node.node_color(barrier=True)
                Grid.update_nodes_neighbours(grid)
            elif pygame.mouse.get_pressed(num_buttons=3)[2]:  # Right mouse click
                started = False
                position = pygame.mouse.get_pos()
                row, column = Grid.get_clicked_position(position)
                node = grid[row][column]
                node.node_color(walk=True)
                if node == start:
                    start = None
                if node == end:
                    end = None
                Grid.update_nodes_neighbours(grid)

            if event.type == pygame.KEYDOWN:
                started = True
                if start is not None and end is not None:

                    if event.key == pygame.K_UP:
                        Grid.refresh_grid(window, grid, start, end)
                        print("---------------------------------\nBreath First Search algorithm")
                        start_time = time.time()
                        results = BFS.breadthFirstSearch(lambda: Grid.draw(window, grid, start, end), grid, start, end)
                        print_result_info(results, [start_time, time.time()])

                    if event.key == pygame.K_DOWN:
                        Grid.refresh_grid(window, grid, start, end)
                        print("---------------------------------\nDepth First Search algorithm")
                        start_time = time.time()
                        results = DFS.depthFirstSearch(lambda: Grid.draw(window, grid, start, end), grid, start, end)
                        print_result_info(results, [start_time, time.time()])

                    if event.key == pygame.K_LEFT:
                        Grid.refresh_grid(window, grid, start, end)
                        print("---------------------------------\nDijkstra algorithm")
                        start_time = time.time()
                        results = Dijkstra.Dijkstra(lambda: Grid.draw(window, grid, start, end), grid, start, end)
                        print_result_info(results, [start_time, time.time()])

                    if event.key == pygame.K_RIGHT:
                        Grid.refresh_grid(window, grid, start, end)
                        print("---------------------------------\nA* algorithm")
                        start_time = time.time()
                        results = AStar.AStar(lambda: Grid.draw(window, grid, start, end), grid, start, end)
                        print_result_info(results, [start_time, time.time()])

    pygame.quit()


def print_result_info(results, times):
    print("Time: " + str(round(times[1] - times[0], 5)) + " seconds" +
          "\nCompleted: " + str(results[1][3]) +
          "\nLength of the path: " + str(results[1][1]) +
          "\nCost of the path: " + str(results[1][2]) +
          "\nNumber of visited nodes: " + str(results[1][0]) +
          "\n---------------------------------")


if __name__ == '__main__':
    main()
