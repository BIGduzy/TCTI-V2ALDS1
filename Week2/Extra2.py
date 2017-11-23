def maze_solver(maze, x = 0, y = 0, direction = -1):
    """
    Description
    Solves maze

    :param maze: The 2 dimensional list maze that needs to be solved
    :param x: Current x position
    :param y: Current y position
    :param direction: Direction the function came from
    :return: List with solution path
    """

    # check possible directions
    # North
    if direction != 2 and y - 1 >= 0 and maze[y - 1][x] != 1:
        # print('North possible')
        if maze[y - 1][x] == -1:
            # print('Won')
            return [0]  # return direction to finish
        else:
            sol = maze_solver(maze, x, y - 1, 0)  # Do the same for next tile
            # if the next tile has a solution
            if sol:
                return [0] + sol  # chain solution to found solution
    # East
    if direction != 3 and x + 1 < len(maze[y]) and maze[y][x + 1] != 1:
        # print('East possible')
        if maze[y][x + 1] == -1:
            # print('Won')
            return [1]  # return direction to finish
        else:
            sol = maze_solver(maze, x + 1, y, 1)  # Do the same for next tile
            # if the next tile has a solution
            if sol:
                return [1] + sol  # chain solution to found solution
    # South
    if direction != 0 and y + 1 < len(maze) and maze[y + 1][x] != 1:
        # print("South possible")
        if maze[y + 1][x] == -1:
            # print('Won')
            return [2]  # return direction to finish
        else:
            sol = maze_solver(maze, x, y + 1, 2)  # Do the same for next tile
            if sol:
                return [2] + sol  # chain solution to found solution
    # West
    if direction != 1 and x - 1 >= 0 and maze[y][x - 1] != 1:
        # print("West possible")
        if maze[y][x - 1] == -1:
            # print('Won')
            return [3]  # return direction to finish
        else:
            sol = maze_solver(maze, x - 1, y, 3)  # Do the same for next tile
            # if the next tile has a solution
            if sol:
                return [3] + sol  # chain solution to found solution

    return []


def fill_maze(maze, solution, x = 0, y = 0, symbol = '.'):
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

    maze[y][x] = symbol
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
        maze[y][x] = symbol

    return maze


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
