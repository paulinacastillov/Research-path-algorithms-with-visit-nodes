import PySimpleGUI as sg
import tracemalloc
import time
from src.core.read_maze import read_maze, read_maze_default
from src.core.gui_maze_solver import window, update_image
from src.core.print_maze import print_maze, clear_maze_print
from src.core.animation import Animation
from src.algorithms.a_star import a_star_search
from src.algorithms.breadth import breadth_search
from src.algorithms.depth import depth_search
from src.algorithms.depth_iterative import depth_iterative_search 
from src.algorithms.greedy import greedy_search
from src.algorithms.uniform import uniform_search

maze = read_maze_default()
#tracemalloc.start() #comienza a ver cuanto cuesta
#st = time.process_time() # get the start time
#clear_maze_print(maze)
path = a_star_search(maze)
print(path)     
#print(f'La memoria utilizada fue: {tracemalloc.get_traced_memory()[1]} MiB') #imprime despues de ejecutar el algoritmo cuanto costó hasta este momento
#tracemalloc.stop() #cierra el conteo
# get the end time
#et = time.process_time()

# get execution time
#res = et - st
#print('El tiempo de CPU utilizado fue:', res, 'segundos')