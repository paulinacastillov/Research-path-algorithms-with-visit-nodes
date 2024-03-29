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

def main():
    maze = read_maze_default()
    print_maze(maze)
    exitSolver = False

    while not exitSolver:
        event, values = window.read()
        if event == 'select_maze':

            maze = read_maze()
            
        if event == 'print_maze':
            
            print_maze(maze)   
        if event == 'a_star':
            tracemalloc.start() #comienza a ver cuanto cuesta
            st = time.process_time() # get the start time
            clear_maze_print(maze)
            a_star_search(maze)
            
            print(f'La memoria utilizada fue: {tracemalloc.get_traced_memory()[1]} MiB') #imprime despues de ejecutar el algoritmo cuanto costó hasta este momento
            tracemalloc.stop() #cierra el conteo
            # get the end time
            et = time.process_time()

            # get execution time
            res = et - st
            print('El tiempo de CPU utilizado fue:', res, 'segundos')
        if event == 'depth': 
            tracemalloc.start()
            st = time.process_time() # get the start time
            clear_maze_print(maze) 
            depth_search(maze)
            print(f'La memoria utilizada fue: {tracemalloc.get_traced_memory()[1]} MiB') #imprime despues de ejecutar el algoritmo cuanto costó hasta este momento
            tracemalloc.stop() 
            # get the end time
            et = time.process_time()

            # get execution time
            res = et - st
            print('El tiempo de CPU utilizado fue:', res, 'segundos')
        if event == 'breadth':
            tracemalloc.start()
            st = time.process_time() # get the start time
            clear_maze_print(maze)
            breadth_search(maze)
            print(f'La memoria utilizada fue: {tracemalloc.get_traced_memory()[1]} MiB') #imprime despues de ejecutar el algoritmo cuanto costó hasta este momento
            tracemalloc.stop() 
            # get the end time
            et = time.process_time()

            # get execution time
            res = et - st
            print('El tiempo de CPU utilizado fue:', res, 'segundos')
        if event == 'depth_iterative':
            tracemalloc.start() 
            st = time.process_time() # get the start time
            clear_maze_print(maze)
            depth_iterative_search(maze)
            print(f'La memoria utilizada fue: {tracemalloc.get_traced_memory()[1]} MiB') #imprime despues de ejecutar el algoritmo cuanto costó hasta este momento
            tracemalloc.stop() 
            # get the end time
            et = time.process_time()

            # get execution time
            res = et - st
            print('El tiempo de CPU utilizado fue:', res, 'segundos')
        if event == 'uniform':
            tracemalloc.start()
            st = time.process_time() # get the start time
            clear_maze_print(maze)
            uniform_search(maze)
            print(f'La memoria utilizada fue: {tracemalloc.get_traced_memory()[1]} MiB') #imprime despues de ejecutar el algoritmo cuanto costó hasta este momento
            tracemalloc.stop() 
             # get the end time
            et = time.process_time()

            # get execution time
            res = et - st
            print('El tiempo de CPU utilizado fue:', res, 'segundos')
        if event == 'greedy':
            tracemalloc.start()
            st = time.process_time() # get the start time
            clear_maze_print(maze)
            greedy_search(maze)
            print(f'La memoria utilizada fue: {tracemalloc.get_traced_memory()[1]} MiB') #imprime despues de ejecutar el algoritmo cuanto costó hasta este momento
            tracemalloc.stop() 
            # get the end time
            et = time.process_time()

            # get execution time
            res = et - st
            print('El tiempo de CPU utilizado fue:', res, 'segundos')
        if event == 'exit':
            exitSolver = True
        if event == 'update_image':
           update_image() 
        if event == 'prev_image':
           Animation.show_prev_frame(maze)
        if event == 'next_image':
           Animation.show_next_frame(maze)
        if event == 'export_gif':
           Animation.export_gif(maze)
        if event == sg.WIN_CLOSED:
            exitSolver = True

    window.close()

if __name__ == "__main__":
    main()

