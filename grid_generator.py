
from src.algorithms.a_star import a_star_search,a_star_search_modified
import numpy as np
import matplotlib.pyplot as plt
import os
import numpy as np


import numpy as np

def save_grid_to_csv(grid, filename):
    np.savetxt(filename, grid, fmt='%d', delimiter=',')


def generate_grid(n, num_walls):

    # Crea un arreglo de tamaño nxn lleno de ceros
    
    grid = np.zeros((n, n), dtype=int)
    
    # Asigna los bordes como 1
    grid[0, :] = grid[-1, :] = grid[:, 0] = grid[:, -1] = 1
    
    # Genera paredes aleatorias
    for _ in range(num_walls):
        row = np.random.randint(1, n - 1)
        col = np.random.randint(1, n - 1)
        grid[row, col] = 1
    
    # Genera puntos aleatorios clasificados como 3
    list_aproach_nodes = []
    num_points = np.random.randint(1, int(n/3))
    for _ in range(num_points):
        row = np.random.randint(1, n - 1)
        col = np.random.randint(1, n - 1)
        while grid[row, col] != 0:
            row = np.random.randint(1, n - 1)
            col = np.random.randint(1, n - 1)
        grid[row, col] = 3
        list_aproach_nodes.append([row,col])
    
    # Genera un punto de inicio aleatorio clasificado como 4
    # start_row = np.random.randint(1, n - 1)
    # start_col = np.random.randint(1, n - 1)
    # while grid[start_row, start_col] != 0:
    #     start_row = np.random.randint(1, n - 1)
    #     start_col = np.random.randint(1, n - 1)
    # grid[start_row, start_col] = 4
    #grid[0, 1] = 4
    start = (0, 1)
    grid[start] = 4
    
    # Genera un punto final aleatorio clasificado como 5
    # end_row = np.random.randint(1, n - 1)
    # end_col = np.random.randint(1, n - 1)
    # while grid[end_row, end_col] != 0:
    #     end_row = np.random.randint(1, n - 1)
    #     end_col = np.random.randint(1, n - 1)
    # grid[end_row, end_col] = 5
    end = (n-1, n-2)
    grid[end] = 4
    
    return grid,start,end, list_aproach_nodes