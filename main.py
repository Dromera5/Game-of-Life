# Our take in the popular game - Conway's game of Life

from random import *
import time

"""
Builds a 10x10 grid filled with 0.
@return grid: a grid containig only 0's.
"""
#This function is already written. Don't modify it!
def build_empty_grid():
    grid = []
    for i in range(10):
        grid.append([0]*10)
    return grid

"""
Builds a grid with nb_cells living cells.
@return grid: a grid containig nb_cells living cells.
"""
#This function is already written. You can modify it if you want to build
#specific grids to begin the simulation, instead of a random one.
def build_first_grid(nb_cells):
    grid = build_empty_grid()
    for i in range(nb_cells):
        l = choice(range(10))
        c = choice(range(10))
        while grid[l][c]==1:
            l = choice(range(10))
            c = choice(range(10))
        grid[l][c]=1

    return grid

"""
Displays the grid passed as parameter.
@param grid: the grid to be displayed.
"""
#This function is already written. You can modify it if you want a more beautiful printing.
def display_grid(grid):
    for line in grid:
        for i in line:
            print("|", end="")
            if i==1:
                print("*", end="")
            else:
                print(" ", end="")
        print("|")
        #print("-"*21)

"""
This function returns a list of cells, in the grid, that are around a given
cell. Each cell is represented as its coordinates (line_neighbor, col_neighbor).
Hence, the return type of this function is a list of couples.
@param grid: the grid in which we are looking for neighbors. Of course,
       since we are always working on a 10x10 grid, it is possible to write this
       function without using this variable. However, in the case where we
       modify the game to have a bigger grid, we have to take care of its sizes.
@param line: the line of the cell for which we are looking for neighbors.
@param col: the column of the cell for which we are looking for neighbors.
@return list: the list of couples of the form (line_neighbor, col_neighbor) of
        the cells that are around the cell at coordinates (line, col).
"""
#This function is only partially written, you have to complete it.
def cells_around(grid, line, col):
    list = []
    #To be completed
    return list

"""
Counts the number of cells alive in the grid.
@param grid: the grid in which we are looking for living cells.
@return the number of cells alive in this grid.
"""
#This function is not written, you have to write it (remove "pass" and write your code).
def nb_cells(grid):
    cells = 0
    for i in grid:
        print(i)
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
#This function is not written, you have to write it (remove "pass" and write your code).
def equal_grids(grid1, grid2):
    pass


# Haha, logic go brrrrr
def neighbor_checker(grid, state, index):
    print(index)

"""
Computes the new generation of cells following the rules of the game of life.
@param grid: the grid containing the cells (living or not) at the current generation.
@return new_gen, the grid containing the cells (living or not) at the next generation.
"""
#This function is only partially written, you have to complete it.
def new_generation(grid):
    new_gen = build_empty_grid()
    for f in grid:
        for i in f:
            neighbors = neighbor_checker(grid, f)

    return new_gen


#-------------------------------------------------------------------------------
# Main game loop.
# Can be improved, don't hesitate!
#-------------------------------------------------------------------------------
grid = build_first_grid(70)
print(grid)
print(grid[1])
print(grid[1][1])
while True:
    display_grid(grid)
    print("Number of living cells = ", nb_cells(grid))
    new_grid = new_generation(grid)

    # If the grid does not change between one iteration and another, stop the
    # simulation and informs that we have reached what is called a stable configuration.
    if equal_grids(grid, new_grid):
        print("Stable configuration.")
        break
    grid = new_grid
    input("Continue? ")
    time.sleep(2)
