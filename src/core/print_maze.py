import os
import glob
import time
import posixpath as path
import matplotlib.pyplot as plt
import PySimpleGUI as sg
import matplotlib as matplotlib
from src.core.gui_maze_solver import window 
from src.core.graph import get_node_coordinates, get_node_number
from src.core.animation import Animation
from copy import deepcopy
import multiprocessing as mp
import os

matplotlib.use('tkAgg')
colormap = plt.cm.Set2
normalize = matplotlib.colors.Normalize(vmin=0, vmax=6)
plt.axis('off') 

def save_maze(maze, index=0):
    try:
        plt.imshow(maze, cmap=colormap, norm=normalize)
        plt.savefig('./images/maze%i.png'%index)
    except Exception:
        pass 

def print_maze(maze, index=0):
    # Cambiar a mp.Pool() para max eficiencia. 
    # mp.Pool(4) se mantiene por razones de compatibilidad
    pool = mp.Pool(4)
    pool.apply_async(save_maze, args = (maze, index))

def get_maze_step(maze, reached, frontier, path=None):
    n_maze = deepcopy(maze)
    sentinel = object()
    for node in reached:
        i,j = get_node_coordinates(maze, node)
        n_maze[i][j] = 4

    for node in frontier:
        i,j = get_node_coordinates(maze, node)
        n_maze[i][j] = 3

    if path is not None: 
        for node in path:
            i,j = get_node_coordinates(maze, node)
            n_maze[i][j] = 5
        
    return n_maze

def clear_maze_print(maze):
    Animation.clear_frame_count()
    dirname = path.dirname(__file__)
    image_path = path.join(dirname.split('/src', 1)[0], 'images/*')
    files = glob.glob(image_path)
    for f in files:
        os.remove(f)
    print_maze(maze)
    
