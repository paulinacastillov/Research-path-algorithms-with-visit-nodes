from collections import deque

from src.core.graph import expand_node, get_node_number, get_node_coordinates

from src.core.print_maze import get_maze_step, print_maze

from src.core.tree import Tree_maze

from src.core.utils import find_node
import math


def uniform_search(maze):


    export_tree = len(maze) <= 6
    
    index_maze_step = 1
   
    cur_node = 1
    cur_path = [1]
    child_values = {}
    child_values[cur_node]=0
    
    if export_tree:
        
        Tree_maze.add_root(1)


#goal
    objective_node = get_node_number(maze,len(maze) - 1 ,len(maze[0])-2)
    frontier = deque([cur_path])
    node_frontier = deque([cur_path[-1]])
    reached  = cur_path
    reached_paths = [cur_path]
    if(cur_node == objective_node): 
        return cur_path
    i=0
    
    while frontier:
        cur_path = frontier.pop()
        cur_node = cur_path[-1]
        node_frontier.pop()
        children = expand_node(maze, cur_path[-1])
        
        if(len(children)>0):
    
            for child in children:
                child_path = cur_path + [child]
                value = child_values[cur_path[-1]] + 1 #le suma 1 al costo del padre para obtener el costo de cada uno de los hijos
                child_values[child] = value 
                
                if export_tree:
                    Tree_maze.add_node(child, cur_node)

                if(child == objective_node):
                   
                    Tree_maze.clear_generated_tree(export_tree)
                    reached.append(child)
                    reached_paths.append(child_path)
                    print_maze(get_maze_step(maze, reached, list(node_frontier),child_path), index_maze_step)
                    return child_path
                
                if find_node(reached, child): 
                    del child_values[child]

                if not find_node(reached, child): 
                    reached_paths.append(child_path)
                    reached.append(child)
                    frontier.append(child_path)
                    node_frontier.append(child)
            del child_values[cur_node] #elimina el valor del padre

            next_node = min(child_values, key=child_values.get) #encuentro el nodo con distancia manhattan mas chiki

            node_frontier.remove(next_node) #elimino el elemento con menor valor para agregarlo en ultima posicion para que sea el siguiente a explorar
            node_frontier.append(next_node)
            frontier_copy=frontier.copy()
            for path in frontier_copy:
                last_of_path=path[-1]
                if last_of_path==next_node:
                    frontier.remove(path) #elimino el elemento con menor valor para agregarlo en ultima posicion para que sea el siguiente a explorar
                    frontier.append(path)
        
        print_maze(get_maze_step(maze, reached, list(node_frontier)), index_maze_step)
        # Incrementar el indice usado para imprimir archivos en maze(i).png
        index_maze_step+=1
    # En caso de no encontrar el nodo objetivo sobreescribir el archivo tree.tx 
    # si y solo export_tree es True
    Tree_maze.clear_generated_tree(export_tree)
    