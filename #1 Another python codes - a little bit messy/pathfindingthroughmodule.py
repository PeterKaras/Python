# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 14:50:57 2020

@author: petko
"""

#pip install pathfinding
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

matrix = [
  [1, 1, 1],
  [1, 10, 1],
  [1, 1, 1]
]
grid = Grid(matrix=matrix)

start = grid.node(2, 2)
end = grid.node(0, 0)

finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
path, runs = finder.find_path(start, end, grid)
print(path)

print('operations:', runs, 'path length:', len(path))
print(grid.grid_str(path=path, start=start, end=end))