'''
    Todos los nodos de la grafica son numerados de esta forma:

    |1|2|3| 
    |4|5|6| 
    |7|8|9| 

    el valor del nodo es guardado como NodeNumber
'''

from collections import deque

from src.core.graph import expand_node, get_node_number, get_node_coordinates

from src.core.print_maze import get_maze_step, print_maze

from src.core.tree import Tree_maze

from src.core.utils import find_node
import math


def greedy_search(maze,approach_nodes):



    
    index_maze_step = 1
   
    cur_node = 1
    cur_path = [1]
    
    
    objective_node = get_node_number(maze,len(maze)  - 1 ,len(maze[0])-2)
    cordinates_objetive = get_node_coordinates(maze,objective_node)
    frontier = deque([cur_path])
    node_frontier = deque([cur_path[-1]])
    reached  = cur_path
    reached_paths = [cur_path]

    if(cur_node == objective_node): 
        return cur_path
    
    while frontier:
        
        cur_path = frontier.pop()
        cur_node = cur_path[-1]
        node_frontier.pop()
        children = expand_node(maze, cur_path[-1])
        
        if(len(children)>0):
            
            child_values = {}
            for child in children:
                child_path = cur_path + [child]
                cordenada = get_node_coordinates(maze,child) #calcula la coordenada
                value = sum(list(map(lambda x,y: abs(x-y) , cordenada, cordinates_objetive))) #calcula la distancia manhattan
                extra = 0
                child_values[child] = value # agrega al diccionario los hijos con sus respectivas distancias Manhattan
                
                

                if(child == objective_node):
                   
                   
                    reached.append(child)
                    reached_paths.append(child_path)
                    #print_maze(get_maze_step(maze, reached, list(node_frontier),child_path), index_maze_step)
                    return child_path

                if find_node(reached, child): 
                    del child_values[child]
                
                if not find_node(reached, child): 
                    reached.append(child)
                    reached_paths.append(child_path)
                    frontier.append(child_path)
                    node_frontier.append(child)
            if(len(child_values)>0):          
                next_node = min(child_values, key=child_values.get) #encuentro el nodo con distancia manhattan mas chiki
                if next_node in node_frontier:
                    node_frontier.remove(next_node) #elimino el elemento con menor valor para agregarlo en ultima posicion para que sea el siguiente a explorar
                    node_frontier.append(next_node)
                    frontier_copy=frontier.copy()
                    for path in frontier_copy:
                        last_of_path=path[-1]
                        if last_of_path==next_node:
                          frontier.remove(path) #elimino el elemento con menor valor para agregarlo en ultima posicion para que sea el siguiente a explorar
                          frontier.append(path)
        
        #print_maze(get_maze_step(maze, reached, list(node_frontier)), index_maze_step)

        # Incrementar el indice usado para imprimir archivos en maze(i).png
        index_maze_step+=1
    # En caso de no encontrar el nodo objetivo sobreescribir el archivo tree.tx 
    # si y solo export_tree es True
  


def greedy_search_mod(maze,aproach_nodes):



    
    index_maze_step = 1
   
    cur_node = 1
    cur_path = [1]
    
    
    objective_node = get_node_number(maze,len(maze)  - 1 ,len(maze[0])-2)
    cordinates_objetive = get_node_coordinates(maze,objective_node)
    frontier = deque([cur_path])
    node_frontier = deque([cur_path[-1]])
    reached  = cur_path
    reached_paths = [cur_path]

    if(cur_node == objective_node): 
        return cur_path
    
    while frontier:
        
        cur_path = frontier.pop()
        cur_node = cur_path[-1]
        node_frontier.pop()
        children = expand_node(maze, cur_path[-1])
        
        if(len(children)>0):
            
            child_values = {}
            for child in children:
                child_path = cur_path + [child]
                cordenada = get_node_coordinates(maze,child) #calcula la coordenada
                value = sum(list(map(lambda x,y: abs(x-y) , cordenada, cordinates_objetive))) #calcula la distancia manhattan
                extra = 0
                for node in aproach_nodes:
                    extra += sum(list(map(lambda x,y: abs(x-y) , cordenada, node)))

                child_values[child] = 0.5 *value + 0.5*extra # agrega al diccionario los hijos con sus respectivas distancias Manhattan

                if(child == objective_node):
                   
                   
                    reached.append(child)
                    reached_paths.append(child_path)
                    #print_maze(get_maze_step(maze, reached, list(node_frontier),child_path), index_maze_step)
                    print('guardo cambios')
                    return child_path

                if find_node(reached, child): 
                    del child_values[child]
                
                if not find_node(reached, child): 
                    reached.append(child)
                    reached_paths.append(child_path)
                    frontier.append(child_path)
                    node_frontier.append(child)
            if(len(child_values)>0):          
                next_node = min(child_values, key=child_values.get) #encuentro el nodo con distancia manhattan mas chiki
                if next_node in node_frontier:
                    node_frontier.remove(next_node) #elimino el elemento con menor valor para agregarlo en ultima posicion para que sea el siguiente a explorar
                    node_frontier.append(next_node)
                    frontier_copy=frontier.copy()
                    for path in frontier_copy:
                        last_of_path=path[-1]
                        if last_of_path==next_node:
                          frontier.remove(path) #elimino el elemento con menor valor para agregarlo en ultima posicion para que sea el siguiente a explorar
                          frontier.append(path)
        
        #print_maze(get_maze_step(maze, reached, list(node_frontier)), index_maze_step)

        # Incrementar el indice usado para imprimir archivos en maze(i).png
        index_maze_step+=1
    # En caso de no encontrar el nodo objetivo sobreescribir el archivo tree.tx 
    # si y solo export_tree es True
  
