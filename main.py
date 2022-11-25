# Our take in the popular game - Conway's game of Life

from random import *
import time

grid_size = 10


"""
Builds a 10x10 grid filled with 0.
@return grid: a grid containing only 0's.
"""


def build_empty_grid(r):
    grid = []
    for i in range(r):
        grid.append([0] * r)
    return grid


"""
Builds a grid with nb_cells living cells.
@return grid: a grid containig nb_cells living cells.
"""


def build_first_grid(num, r):
    grid = build_empty_grid(r)
    for i in range(num):
        l = choice(range(r))
        c = choice(range(r))
        while grid[l][c] == 1:
            l = choice(range(r))
            c = choice(range(r))
        grid[l][c] = 1

    return grid


"""
Displays the grid passed as parameter.
@param grid: the grid to be displayed.
"""


def display_grid(grid):
    for line in grid:
        for i in line:
            print("|", end="")
            if i == 1:
                print("*", end="")
            else:
                print(" ", end="")
        print("|")
        # print("-"*21)


"""
Counts the number of cells alive in the grid.
@param grid: the grid in which we are looking for living cells.
@return the number of cells alive in this grid.
"""


def nb_cells(grid):
    cells = 0
    for i in grid:
        for f in i:
            if f == 1:
                cells += 1

    return cells


"""
Tests if two grids are identical.
@param grid1: one of the two grids to be tested.
@param grid2: one of the two grids to be tested.
@return True if both girds are identical, False otherwise.
"""


def equal_grids(grid1, grid2):
    if grid1 == grid2:
        return True
    else:
        return False


"""
Check the neighbors around a given cell.
Does it for all cells.
"""


def neighbor_checker(grid, i, ii):
    # Bad solution but the first one that came to mind
    num = 0

    try:
        if grid[i][ii] == 1:
            num += 1

        if grid[i][ii+1] == 1 and ii != 9:
            num += 1

        if grid[i][ii-1] == 1 and ii != 0:
            num += 1

        if grid[i+1][ii] == 1 and i != 9:
            num += 1

        if grid[i+1][ii+1] == 1 and i != 9 and ii != 9:
            num += 1

        if grid[i+1][ii-1] == 1 and i != 9 and ii != 0:
            num += 1

        if grid[i-1][ii] == 1 and i != 0:
            num += 1

        if grid[i-1][ii+1] == 1 and i != 0 and ii != 9:
            num += 1

        if grid[i-1][ii-1] == 1 and i != 0 and ii != 0:
            num += 1

    except IndexError:
        pass

    return num


"""
Computes the new generation of cells following the rules of the game of life.
@param grid: the grid containing the cells (living or not) at the current generation.
@return new_gen, the grid containing the cells (living or not) at the next generation.
"""


def new_generation(grid):
    new_gen = build_empty_grid(grid_size)
    index = 0
    for f in grid:
        inner_index = 0
        for i in f:
            neighbor_num = neighbor_checker(grid, index, inner_index)

            if grid[index][inner_index] == 1:
                if neighbor_num >= 1:
                    # dies
                    new_gen[index][inner_index] = 0
                elif neighbor_num == 2 or neighbor_num == 3:
                    # lives
                    new_gen[index][inner_index] = 1
                else:
                    # dies
                    new_gen[index][inner_index] = 0
            else:
                if neighbor_num == 3:
                    # born
                    new_gen[index][inner_index] = 1
                else:
                    # stays dead
                    new_gen[index][inner_index] = 0

            inner_index += 1
        index += 1

    return new_gen


# -------------------------------------------------------------------------------
# Main game loop
# -------------------------------------------------------------------------------
def start_game():
    print("Eyo, Welcome to this game!")
    time.sleep(1)

    try:
        file = open("pattern.txt", "r")
        grid = build_empty_grid(grid_size)
        index = 0
        for line in file:
            length = len(line)
            for inner_index in range(min(length, grid_size)):
                if line[inner_index] == "0" or line[inner_index] == "D":
                    grid[index][inner_index] = 0
                elif line[inner_index] == "1" or line[inner_index] == "L":
                    grid[index][inner_index] = 1
                else:
                    grid[index][inner_index] = 0

            if index > grid_size:
                print("----------------------------------------")
                print("Invalid File!")
                print("----------------------------------------")
                file.close()
                break
            else:
                index += 1
        file.close()


    except:
        num = int(input("Choose how many cells will be alive: "))
        if num > grid_size * grid_size:
            print("----------------------------------------")
            print("Cell number too big! Defaulting to 30.")
            print("----------------------------------------")
            grid = build_first_grid(30, grid_size)
        else:
            grid = build_first_grid(num, grid_size)

    while True:
        display_grid(grid)
        print("Number of living cells = ", nb_cells(grid))
        new_grid = new_generation(grid)

        # If the grid does not change between one iteration and another, stop the
        # simulation and informs that we have reached what is called a stable configuration.
        if equal_grids(grid, new_grid) is True:
            print("----------------------------------------")
            print("Stable configuration!")
            print("----------------------------------------")
            break
        grid = new_grid
        answer = input("Continue?").lower
        if answer == "y" or answer == "yes":
            time.sleep(1)
        else:
            print("----------------------------------------")
            print("Goodbye!")
            print("----------------------------------------")
            break


start_game()
