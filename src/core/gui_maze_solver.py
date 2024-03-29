import time
import PySimpleGUI as sg

def create_GUI_window():
    sg.theme('SystemDefault')
    options_column = sg.Column([
        [sg.Button('Seleccionar laberinto', key="select_maze")],
        [sg.Frame('Seleccionar un algoritmo', [
            [sg.Button('Profundidad', key='depth')],
            [sg.Button('Anchura', key='breadth')],
            [sg.Button('Profundidad iterativa', key='depth_iterative')],
            [sg.Button('Búsqueda de costo uniforme', key='uniform')],
            [sg.Button('Búsqueda greedy', key='greedy')],
            [sg.Button('A*', key='a_star')],
        ])],
        [sg.Button('Imprimir laberinto', key="print_maze")],
        [sg.Button('Exit', key="exit")]])
    image_column = sg.Column([
        [sg.Image('images/maze0.png', key="maze-img")],
        [
            sg.Button('<', key="prev_image"), 
            sg.Button('>', key="next_image"),
            sg.Button('Exportar GIF', key="export_gif"),
        ]
    ],expand_x=True, expand_y=True)

    layout = [[
        options_column,
        image_column 
    ]]
    return sg.Window('Maze Solver',layout)

def update_image(index=0): 
    maze_img = window['maze-img']
    maze_img.update(filename='./images/maze%i.png' % index)

window = create_GUI_window()
