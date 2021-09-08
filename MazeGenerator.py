import random
import Main

WALL = 1
CELL = 0
UNVISITED = -1


def print_maze(maze):
    for i in range(Main.GRID_ROWS):
        for j in range(Main.GRID_COLUMNS):
            print(str(maze[i][j]), end=" ")
        print('\n')


# Find number of surrounding cells
def surrounding_cells(maze, rand_wall):
    s_cells = 0
    if maze[rand_wall[0] - 1][rand_wall[1]] == CELL:
        s_cells += 1
    if maze[rand_wall[0] + 1][rand_wall[1]] == CELL:
        s_cells += 1
    if maze[rand_wall[0]][rand_wall[1] - 1] == CELL:
        s_cells += 1
    if maze[rand_wall[0]][rand_wall[1] + 1] == CELL:
        s_cells += 1

    return s_cells


def mark_new_walls(maze, walls, rand_wall, upper=False, bottom=False, left=False, right=False):
    maze[rand_wall[0]][rand_wall[1]] = CELL

    # Upper cell
    if upper:
        if rand_wall[0] != 0:
            if maze[rand_wall[0] - 1][rand_wall[1]] != CELL:
                maze[rand_wall[0] - 1][rand_wall[1]] = WALL
            if [rand_wall[0] - 1, rand_wall[1]] not in walls:
                walls.append([rand_wall[0] - 1, rand_wall[1]])

    # Bottom cell
    if bottom:
        if rand_wall[0] != Main.GRID_COLUMNS - 1:
            if maze[rand_wall[0] + 1][rand_wall[1]] != CELL:
                maze[rand_wall[0] + 1][rand_wall[1]] = WALL
            if [rand_wall[0] + 1, rand_wall[1]] not in walls:
                walls.append([rand_wall[0] + 1, rand_wall[1]])

    # Left cell
    if left:
        if rand_wall[1] != 0:
            if maze[rand_wall[0]][rand_wall[1] - 1] != CELL:
                maze[rand_wall[0]][rand_wall[1] - 1] = WALL
            if [rand_wall[0], rand_wall[1] - 1] not in walls:
                walls.append([rand_wall[0], rand_wall[1] - 1])

    # Right cell
    if right:
        if rand_wall[1] != Main.GRID_ROWS - 1:
            if maze[rand_wall[0]][rand_wall[1] + 1] != CELL:
                maze[rand_wall[0]][rand_wall[1] + 1] = WALL
            if [rand_wall[0], rand_wall[1] + 1] not in walls:
                walls.append([rand_wall[0], rand_wall[1] + 1])


def delete_wall(walls, rand_wall):
    for wall in walls:
        if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
            walls.remove(wall)


def maze_generator():
    maze = [[UNVISITED for _ in range(Main.GRID_COLUMNS)] for _ in range(Main.GRID_ROWS)]

    # Randomize starting point and set it a cell
    starting_width, starting_height = random.randint(1, Main.GRID_ROWS - 1), random.randint(1, Main.GRID_COLUMNS - 1)

    # Mark it as cell and add surrounding walls to the list
    maze[starting_width][starting_height] = CELL
    walls = [[starting_width - 1, starting_height], [starting_width, starting_height - 1],
             [starting_width, starting_height + 1], [starting_width + 1, starting_height]]

    # Denote walls in maze
    for wall in walls:
        maze[wall[0]][wall[1]] = WALL

    while walls:
        # Pick a random wall
        rand_wall = walls[int(random.random() * (len(walls) - 1))]

        # Check the upper wall
        if rand_wall[0] != 0:
            if maze[rand_wall[0] - 1][rand_wall[1]] == UNVISITED and maze[rand_wall[0] + 1][rand_wall[1]] == CELL:
                s_cells = surrounding_cells(maze, rand_wall)
                if s_cells < 2:
                    mark_new_walls(maze, walls, rand_wall, upper=True, left=True, right=True)

                delete_wall(walls, rand_wall)

        # Check the bottom wall
        if rand_wall[0] != Main.GRID_COLUMNS - 1:
            if maze[rand_wall[0] + 1][rand_wall[1]] == UNVISITED and maze[rand_wall[0] - 1][rand_wall[1]] == CELL:
                s_cells = surrounding_cells(maze, rand_wall)
                if s_cells < 2:
                    mark_new_walls(maze, walls, rand_wall, bottom=True, left=True, right=True)

                delete_wall(walls, rand_wall)

        # Check the left wall
        if rand_wall[1] != 0:
            if maze[rand_wall[0]][rand_wall[1] - 1] == UNVISITED and maze[rand_wall[0]][rand_wall[1] + 1] == CELL:
                s_cells = surrounding_cells(maze, rand_wall)
                if s_cells < 2:
                    mark_new_walls(maze, walls, rand_wall, upper=True, bottom=True, left=True)

                delete_wall(walls, rand_wall)

        # Check the right wall
        if rand_wall[1] != Main.GRID_ROWS - 1:
            if maze[rand_wall[0]][rand_wall[1] + 1] == UNVISITED and maze[rand_wall[0]][rand_wall[1] - 1] == CELL:
                s_cells = surrounding_cells(maze, rand_wall)
                if s_cells < 2:
                    mark_new_walls(maze, walls, rand_wall, upper=True, bottom=True, right=True)

                delete_wall(walls, rand_wall)

        delete_wall(walls, rand_wall)

    # Mark the remaining unvisited cells as walls
    maze = [[WALL if maze[i][j] == UNVISITED else maze[i][j] for j in range(Main.GRID_ROWS)]
            for i in range(Main.GRID_COLUMNS)]

    # print_maze(maze)
    return maze


def random_maze_generator():
    maze = []
    for i in range(Main.GRID_ROWS):
        row = []
        for j in range(Main.GRID_COLUMNS):
            if i == 0 or j == 0 or i == Main.GRID_ROWS - 1 or j == Main.GRID_COLUMNS - 1:
                row.append(1)
            elif i == 1 and j == 1 or i == Main.GRID_ROWS - 2 and j == Main.GRID_COLUMNS - 2:
                row.append(0)
            else:
                node = random.uniform(0, 1)
                if node <= 0.33:
                    row.append(1)
                else:
                    row.append(0)
        maze.append(row)
    return maze
