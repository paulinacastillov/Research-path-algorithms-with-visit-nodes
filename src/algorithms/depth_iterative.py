

from collections import deque
from src.core.graph import expand_node, get_node_number
from src.core.print_maze import get_maze_step, print_maze
from src.core.tree import Tree_maze
from src.core.utils import find_node

def depth_iterative_search(maze):
   
    export_tree = len(maze) <= 6
    index_maze_step = 1
    cur_path = [1]
    cur_node=1
    
    
    if export_tree:    
        Tree_maze.add_root(1)
        
    objective_node = get_node_number(maze,len(maze) - 1 ,len(maze[0])-2)
    frontier = deque([cur_path])
    node_frontier = deque([cur_path[-1]])
    reached  = cur_path
    reached_paths = [cur_path]
    
    if(cur_path == objective_node): 
        return cur_path
    
    jump = 3 #que tan profundo quiero que escarbe
    nodes_values = {}
    nodes_values[cur_node] = 0 #Esto me dará la altura del nodo
    hight = 0
    
    while frontier:
       
        cur_path = frontier.pop()
        cur_node = cur_path[-1]
        node_frontier.pop()
        children = expand_node(maze, cur_path[-1])

        if(len(children)>0):
            for child in children:
                child_path = cur_path + [child]
                nodes_values[child] = nodes_values[cur_node] + 1 
                 
                if export_tree:
                    Tree_maze.add_node(child, cur_node)
                    
                if(child == objective_node):
                    
                    Tree_maze.clear_generated_tree(export_tree)
                    reached.append(child)
                    reached_paths.append(child_path)
                    print_maze(get_maze_step(maze, reached, list(node_frontier),child_path), index_maze_step)
                    return child_path
                
                if not find_node(reached, child):
                    reached_paths.append(child_path)
                    reached.append(child)
                    if nodes_values[child] <= hight :
                        node_frontier.append(child)
                        frontier.append(child_path)
                    else:
                        frontier.appendleft(child_path)
                        node_frontier.appendleft(child)
        
                else:
                    nodes_values.pop(child)

            nodes_values.pop(cur_node)

            #print(nodes_values)
        #print(nodes_values[min(nodes_values, key=nodes_values.get)])
        if nodes_values[min(nodes_values, key=nodes_values.get)] == hight+1 :
            hight += jump
    
        #print(hight)

        print_maze(get_maze_step(maze, reached, list(node_frontier)), index_maze_step)

        index_maze_step+=1
        
        
    
    Tree_maze.clear_generated_tree(export_tree)
