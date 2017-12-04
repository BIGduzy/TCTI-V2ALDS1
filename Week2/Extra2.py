import copy
g_full_path = []


def inverted_direction(direction) -> int:
    """
    Description
    Inverts direction

    :param direction: Direction
    :return: Inverted direction
    """
    return direction + 2 if direction < 2 else direction - 2


def valid_tile(maze, x, y) -> bool:
    """
    Description
    Checks if tile x,y are in the maze and if the tile at x,y is a non wall

    :param maze: The maze that needs to be checked
    :param x: X position
    :param y: Y position
    :return: If tile is valid
    """
    return (0 <= y < len(maze) and
            0 <= x < len(maze[y]) and
            maze[y][x] != 1)


def maze_solver(maze, x = 0, y = 0, direction = -1) -> list:
    """
    Description
    Solves maze, writes full path in global variable

    :param maze: The 2 dimensional list maze that needs to be solved
    :param x: Current x position
    :param y: Current y position
    :param direction: Direction the function came from
    :return: List with solution path
    """
    global g_full_path

    inverted_dir = inverted_direction(direction)

    # check possible directions (North, East, South, West)
    directions = ((0, -1), (1, 0), (0, 1), (-1, 0))  # x, y
    for i in range(len(directions)):
        direct = directions[i]
        new_pos = (x + direct[0], y + direct[1])  # x, y
        if i != inverted_dir and valid_tile(maze, new_pos[0], new_pos[1]):  # maze[y][x]
            # add step to full path
            g_full_path.append(i)

            # If next tile == finish
            if maze[new_pos[1]][new_pos[0]] == -1:
                return [i]
            else:
                # Next tile is empty so we check that tile recursively
                sol = maze_solver(maze, new_pos[0], new_pos[1], i)
                # If the recursive function found a route return current direction + found solution
                if sol:
                    return [i] + sol

    # add the inverse to full path to backtrack
    g_full_path.append(inverted_dir)

    return []


def fill_maze(maze, solution, x = 0, y = 0, symbol = '.') -> list:
    """
    Description
    Fills maze with solution path

    :param maze: The 2 dimensional list maze that needs to be solved
    :param solution: List with solution
    :param x: X Start position in the maze
    :param y: Y Start position in the maze
    :param symbol: Replace character
    :return: 2 dimensional list with solved maze
    """

    tmp = copy.deepcopy(maze)
    tmp[y][x] = symbol
    for direction in solution:
        if direction == 0:
            y -= 1
        elif direction == 1:
            x += 1
        elif direction == 2:
            y += 1
        elif direction == 3:
            x -= 1

        # Mark maze
        tmp[y][x] = symbol

    return tmp


def print_2d_list(lst):
    """
    Description
    Prints 2 dimensional list to console

    :param lst: 2 dimensional List
    """
    for row in lst:
        for column in row:
            print(column, ' ', end="")
        print()


if __name__ == "__main__":
    small_maze = [
        [0, 1, 1, 0],
        [0, 0, 1, -1],
        [0, 0, 1, 0],
        [0, 0, 0, 0],
    ]

    small_maze_solution = maze_solver(small_maze)
    small_maze_solved = fill_maze(small_maze, small_maze_solution)
    print_2d_list(small_maze_solved)
    print()

    BIG_maze = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0],
        [0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
        [0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, -1]
    ]

    x = 0
    y = 0
    big_maze_solution = maze_solver(BIG_maze, x, y)
    big_maze_solved = fill_maze(BIG_maze, big_maze_solution, x, y)
    print_2d_list(big_maze_solved)
    print()

    huge_maze = [
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, -1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
    ]

    x = 0
    y = 0
    try:
        huge_maze_solution = maze_solver(huge_maze, x, y)
        huge_maze_solved = fill_maze(huge_maze, huge_maze_solution, x, y)
        print_2d_list(huge_maze_solved)
    except:
        print_2d_list(huge_maze)
    print()
