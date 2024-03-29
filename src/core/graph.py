from src.core.utils import print_matrix

def expand_node(maze, nodeNumber): 
    i, j = get_node_coordinates(maze, nodeNumber)
    adjacentNodes = []

    # Checks up
    if(i - 1 >= 0 and maze[i-1][j] != 1):
        adjacentNodes.append(get_node_number(maze,i-1,j)) 
    # Checks down
    if(i + 1 < len(maze) and maze[i+1][j] != 1):
        adjacentNodes.append(get_node_number(maze,i+1,j)) 
    # Checks left
    if(j - 1 >= 0 and maze[i][j-1] != 1):
        adjacentNodes.append(get_node_number(maze,i,j-1))
    # Checks right
    if(j + 1 < len(maze[i]) and maze[i][j+1] != 1):
        adjacentNodes.append(get_node_number(maze,i,j+1))

    return  adjacentNodes

def get_node_number(maze, i, j):
    return (i*len(maze)) + j

def get_node_coordinates(maze, nodeNumber):
   i = nodeNumber // len(maze[0]) 
   j = nodeNumber % len(maze[0])
   return [i, j]
