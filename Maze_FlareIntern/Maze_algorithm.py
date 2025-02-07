# Author: Shivang Chaudhary
# Education: King's College London - University of London (2023-2024)
# Date: 26/06/2024
# ----
# The following is the working back-end code for generating valid maze utilising Prim's algorithm for path generation.
# ----
import random


# 1. Prints the final maze
def print_maze(maze):
    for row in maze:
        print(''.join(row))

# 2. Initialise the maze with walls
def initialize_maze(width, height):
    maze = [['#'] * width for _ in range(height)]
    return maze

# 3. To verify positioning of the cell in the maze
def in_bounds(x, y, width, height):
    return 0 <= x < width and 0 <= y < height

# 4. Important function: Working function to generate valid mazes using effective "Prim's algorithm".
def prim_maze(width, height):
    maze = initialize_maze(width, height)

    # Let's start from a random cell
    start_x, start_y = random.randint(1, (width // 2) * 2 - 1), random.randint(1, (height // 2) * 2 - 1)
    maze[start_y][start_x] = ' '

    # List of walls
    walls = []
    if start_x > 1: walls.append((start_x - 1, start_y, start_x - 2, start_y))
    if start_x < width - 2: walls.append((start_x + 1, start_y, start_x + 2, start_y))
    if start_y > 1: walls.append((start_x, start_y - 1, start_x, start_y - 2))
    if start_y < height - 2: walls.append((start_x, start_y + 1, start_x, start_y + 2))

    while walls:
        # Randomly select a wall
        wall_index = random.randint(0, len(walls) - 1)
        wx, wy, nx, ny = walls.pop(wall_index)

        if in_bounds(nx, ny, width, height) and maze[ny][nx] == '#':
            # Making the wall a passage
            maze[wy][wx] = ' '
            maze[ny][nx] = ' '

            # Adding the neighboring walls of the new cell
            if nx > 1 and maze[ny][nx - 2] == '#': walls.append((nx - 1, ny, nx - 2, ny))
            if nx < width - 3 and maze[ny][nx + 2] == '#': walls.append((nx + 1, ny, nx + 2, ny))
            if ny > 1 and maze[ny - 2][nx] == '#': walls.append((nx, ny - 1, nx, ny - 2))
            if ny < height - 3 and maze[ny + 2][nx] == '#': walls.append((nx, ny + 1, nx, ny + 2))

            # Defining the entry and exit points
            entry_side = random.choice(['top', 'bottom', 'left', 'right'])
            exit_side = random.choice(['top', 'bottom', 'left', 'right'])
            while exit_side == entry_side:
                exit_side = random.choice(['top', 'bottom', 'left', 'right'])

            if entry_side == 'top':
                entry_x, entry_y = random.choice(range(1, width, 2)), 0
            elif entry_side == 'bottom':
                entry_x, entry_y = random.choice(range(1, width, 2)), height - 1
            elif entry_side == 'left':
                entry_x, entry_y = 0, random.choice(range(1, height, 2))
            elif entry_side == 'right':
                entry_x, entry_y = width - 1, random.choice(range(1, height, 2))

            if exit_side == 'top':
                exit_x, exit_y = random.choice(range(1, width, 2)), 0
            elif exit_side == 'bottom':
                exit_x, exit_y = random.choice(range(1, width, 2)), height - 1
            elif exit_side == 'left':
                exit_x, exit_y = 0, random.choice(range(1, height, 2))
            elif exit_side == 'right':
                exit_x, exit_y = width - 1, random.choice(range(1, height, 2))

    # Constructing outermost borders:-
    # Ensure only entry and exit points are open on borders
    for x in range(width):
        if x != 0:
            maze[0][x] = '#'  # Top border
            maze[height - 1][x] = '#'  # Bottom border
    for y in range(height):
        if y != 0:
            maze[y][0] = '#'  # Left border
            maze[y][width - 1] = '#'  # Right border

    # # Marking the entry and exit points only
    maze[entry_y][entry_x] = '0'
    maze[exit_y][exit_x] = '0'

    # Ensure that the entry and exit points are connected to the whole maze
    if entry_side == 'top':
        maze[entry_y + 1][entry_x] = ' '
    elif entry_side == 'bottom':
        maze[entry_y - 1][entry_x] = ' '
    elif entry_side == 'left':
        maze[entry_y][entry_x + 1] = ' '
    elif entry_side == 'right':
        maze[entry_y][entry_x - 1] = ' '

    if exit_side == 'top':
        maze[exit_y + 1][exit_x] = ' '
    elif exit_side == 'bottom':
        maze[exit_y - 1][exit_x] = ' '
    elif exit_side == 'left':
        maze[exit_y][exit_x + 1] = ' '
    elif exit_side == 'right':
        maze[exit_y][exit_x - 1] = ' '

    return maze


# Chosen dimensions of the maze
width, height = 21, 21

# Generating the maze : Test-sample.
#maze = prim_maze(width, height)

# Print the generated maze
# print_maze(maze)
