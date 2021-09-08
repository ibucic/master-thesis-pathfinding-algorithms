import pygame
import queue
import Grid


def Dijkstra(draw_window, grid, start, end):
    count = 0
    completed = False

    open_set = queue.PriorityQueue()
    open_set.put((0, count, start))
    open_set_hash = {start}

    path = {}

    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0

    while open_set_hash:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        count += 1
        current = open_set.get()[2]
        open_set_hash.remove(current)
        current.node_color(close=True)

        if current == end:
            completed = True
            path_length, path_cost = Grid.reconstruct_path(path, end, draw_window)
            return [path, [count, path_length, path_cost, completed]]

        for neighbour in current.neighbours:
            temp_g_score = g_score[current] + neighbour.weight

            if temp_g_score < g_score[neighbour]:
                path[neighbour] = current
                g_score[neighbour] = temp_g_score
                if neighbour not in open_set_hash:
                    open_set.put((g_score[neighbour], count, neighbour))
                    open_set_hash.add(neighbour)
                    neighbour.node_color(open=True)
        draw_window()

    return [path, [count, -1, -1, completed]]
