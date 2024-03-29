from collections import deque
from src.core.graph import expand_node, get_node_number
from src.core.print_maze import get_maze_step, print_maze
from src.core.tree import Tree_maze
from src.core.utils import find_node

def breadth_search(maze):
    export_tree = len(maze) <= 6
    index_maze_step = 1
    cur_path = [1]
    if export_tree:
        Tree_maze.add_root(1)
    objective_node = get_node_number(maze,len(maze) - 1 ,len(maze[0])-2)
    frontier = deque([cur_path])
    node_frontier = deque([cur_path[-1]])
    reached  = cur_path
    reached_paths = [cur_path]
    if(cur_path[-1] == objective_node):
        return cur_path
    try:
        while frontier:
            cur_path = frontier.pop()
            node_frontier.pop()
            children = expand_node(maze, cur_path[-1])
            if(len(children)>0):
                for child in children:
                    child_path = cur_path + [child]
                    if export_tree:
                        Tree_maze.add_node(child, cur_path[-1])
                    if(child == objective_node):
                        Tree_maze.clear_generated_tree(export_tree)
                        reached.append(child)
                        reached_paths.append(child_path)
                        print_maze(get_maze_step(maze, reached, list(node_frontier),child_path), index_maze_step)
                        return child_path
                    if not find_node(reached, child): 
                        reached_paths.append(child_path)
                        reached.append(child)
                        frontier.appendleft(child_path)
                        node_frontier.appendleft(child)
            print_maze(get_maze_step(maze, reached, list(node_frontier)), index_maze_step)
            index_maze_step+=1
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    Tree_maze.clear_generated_tree(export_tree)
