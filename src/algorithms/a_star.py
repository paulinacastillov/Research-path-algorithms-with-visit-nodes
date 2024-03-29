from collections import deque
from src.core.graph import expand_node, get_node_number, get_node_coordinates
from src.core.print_maze import get_maze_step, print_maze
from src.core.tree import Tree_maze
from src.core.utils import find_node
import math


def a_star_search(maze,goal_node):


    export_tree = len(maze) <= 6
    
    index_maze_step = 1
   
    cur_path = [1]
    
    if export_tree:
        
        Tree_maze.add_root(1)
    # cambiar para un punto aleatorio del mapa
    objective_node = get_node_number(maze,goal_node[0] ,goal_node[1])
    cordinates_objetive = get_node_coordinates(maze,objective_node)
    frontier = deque([cur_path])
    node_frontier = deque([cur_path[-1]])
    reached  = cur_path
    reached_paths = [cur_path]


    if(cur_path[-1] == objective_node): 
        return cur_path

    child_values1 = {}
    child_values2 = {}
    path_value = 0
    cordenadaP= get_node_coordinates(maze,cur_path[-1])
    h_padre = sum(list(map(lambda x,y: abs(x-y) , cordenadaP, cordinates_objetive)))
    child_values1[cur_path[-1]]=h_padre
    child_values2[cur_path[-1]]=0
    
    while frontier:
        
        cur_path = frontier.pop()
        cur_node = cur_path[-1]
        node_frontier.pop()
        children = expand_node(maze, cur_path[-1])
        
        if(len(children)>0):

            cordenadaP= get_node_coordinates(maze,cur_path[-1])
            c_padre= child_values2[cur_path[-1]] 
    
            for child in children:
                child_path = cur_path + [child]
                cordenadaS = get_node_coordinates(maze,child) #calcula la coordenada del hijo
                c = c_padre + 1 #cálcula el costo de llegar hasta el hijo
                h = sum(list(map(lambda x,y: abs(x-y) , cordenadaS, cordinates_objetive))) #calcula la distancia manhattan
                child_values1[child] = h + c
                child_values2[child] = c
                
                if export_tree:
                    Tree_maze.add_node(child, cur_node)

                if(child == objective_node):
                    Tree_maze.clear_generated_tree(export_tree)
                    reached.append(child)
                    reached_paths.append(child_path)
                    #print_maze(get_maze_step(maze, reached, list(node_frontier),child_path), index_maze_step)
                    print(sum(child_values2.values()))

                    
                    return child_path

                if find_node(reached, child): 
                    del child_values1[child]
                
                if not find_node(reached, child): 
                    reached.append(child)
                    reached_paths.append(child_path)
                    frontier.appendleft(child_path)
                    node_frontier.appendleft(child)
            del child_values1[cur_node] #elimina el valor del padre
            next_node = min(child_values1, key=child_values1.get) #encuentro el nodo con distancia manhattan mas chiki
                
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
    Tree_maze.clear_generated_tree(export_tree)

def a_star_search_modified(maze,goal_node,aproach_nodes):


    export_tree = len(maze) <= 6
    
    index_maze_step = 1
   
    cur_path = [1]
    
    if export_tree:
        
        Tree_maze.add_root(1)

    objective_node = get_node_number(maze,goal_node[0] ,goal_node[1])
    cordinates_objetive = get_node_coordinates(maze,objective_node)
    frontier = deque([cur_path])
    node_frontier = deque([cur_path[-1]])
    reached  = cur_path
    reached_paths = [cur_path]


    if(cur_path[-1] == objective_node): 
        return cur_path
    path_value = 0
    child_values1 = {1:0}
    child_values2 = {1:0}
    cordenadaP= get_node_coordinates(maze,cur_path[-1])
    h_padre = sum(list(map(lambda x,y: abs(x-y) , cordenadaP, cordinates_objetive)))
    child_values1[cur_path[-1]]=h_padre
    child_values2[cur_path[-1]]=0
    
    while frontier:
        
        cur_path = frontier.pop()
        cur_node = cur_path[-1]
        node_frontier.pop()
        children = expand_node(maze, cur_path[-1])
        
        if(len(children)>0):

            cordenadaP= get_node_coordinates(maze,cur_path[-1])
            c_padre= child_values2[cur_path[-1]] 
    
            for child in children:
                child_path = cur_path + [child]
                cordenadaS = get_node_coordinates(maze,child) #calcula la coordenada del hijo
                c = c_padre + 1 #cálcula el costo de llegar hasta el hijo
                h = sum(list(map(lambda x,y: abs(x-y) , cordenadaS, cordinates_objetive))) #calcula la distancia manhattan
                extra = 0
                for node in aproach_nodes:
                    extra += sum(list(map(lambda x,y: abs(x-y) , cordenadaS, node))) # distancia manhatan

                child_values1[child] = 0.3*h + 0.3*c + 0.3*extra
                child_values2[child] = c

                
                if export_tree:
                    Tree_maze.add_node(child, cur_node)

                if(child == objective_node):
                    Tree_maze.clear_generated_tree(export_tree)
                    reached.append(child)
                    reached_paths.append(child_path)
                    #print_maze(get_maze_step(maze, reached, list(node_frontier),child_path), index_maze_step)
                    # for ch in child_path:
                    #     path_value += child_values1[ch]
                    print(sum(child_values2.values()))
                    
                    return child_path

                if find_node(reached, child): 
                    del child_values1[child]
                
                if not find_node(reached, child): 
                    reached.append(child)
                    reached_paths.append(child_path)
                    frontier.appendleft(child_path)
                    node_frontier.appendleft(child)
            del child_values1[cur_node] #elimina el valor del padre
            next_node = min(child_values1, key=child_values1.get) #encuentro el nodo con distancia manhattan mas chiki
                
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
    Tree_maze.clear_generated_tree(export_tree)
