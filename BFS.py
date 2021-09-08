import pygame
import Grid


def breadthFirstSearch(draw_window, grid, start, end):
    count = 0
    completed = False

    queue = [start]
    visited = [[False for _ in range(len(grid))] for _ in range(len(grid[0]))]
    path = {}

    visited[start.row][start.column] = True

    while queue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    
        count += 1
        current = queue.pop()
        current.node_color(close=True)

        if current == end:
            completed = True
            path_length, path_cost = Grid.reconstruct_path(path, end, draw_window)
            return [path, [count, path_length, path_cost, completed]]

        for neighbour in current.neighbours:
            if not visited[neighbour.row][neighbour.column]:
                queue.insert(0, neighbour)
                neighbour.node_color(open=True)
                visited[neighbour.row][neighbour.column] = True
                path[neighbour] = current
        draw_window()

    return [path, [count, -1, -1, completed]]
