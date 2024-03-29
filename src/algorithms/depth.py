#Usa esto para la estructura de datos de cola y fila, NUNCA usen queue
from collections import deque
#expand_node: dado un nodo y el laberinto les regresa los vecinos 
#get_node_number: dadas las coordenadas i,j regresa el NodeNumber
from src.core.graph import expand_node, get_node_number
#get_maze_step: Obtiene el laberinto dados como parametros la frontera y los nodos visitados y un 
#print_maze: Imprime el laberinto dado con indice i que nombra el archivo .png exportado maze(i).png
#   los archivos maze(i) son usados para generar la animacion
from src.core.print_maze import get_maze_step, print_maze
#Tree_maze estructura de datos que permite imprimir el arbol. 
#   add_root: Agrega la raiz del arbol dado un nodo
#   add_node: Agrega un nodo hijo al padre add_node(padre, hijo)
from src.core.tree import Tree_maze
#   Dado un vector y un nodo regresa True si se encuentra el nodo en es vector y False de lo contrario
from src.core.utils import find_node



def depth_search(maze):
    # Solo se exporta el arbol para cuadriculas de 6x6 o menos (de acuerdo a specs)
    export_tree = len(maze) <= 6
    # Indice usado para imprimir el paso en el archivo maze(i).png
    index_maze_step = 1
    # Nodo actual, todos los laberintos empieza en el nodo (0,1) el cual es el nodeNumber 1
    cur_node = 1
    cur_path = [1]
    # Se ejecuta solo si se debe exportar el arbol
    if export_tree:
        # Agrega el nodo 1 como la raiz (Siempre agregar esto al inicio 
        # del algoritmo antes de agregar nodos)
        Tree_maze.add_root(1)
    # El nodo objetivo siempre es el penultimo de la cuadricula, este paso regresa el nodeNumber
    objective_node = get_node_number(maze,len(maze) - 1 ,len(maze[0])-2)
    # La frontera del algoritmo. SIEMPRE usar deque
    frontier = deque([cur_path])
    node_frontier = deque([cur_path[-1]])
    reached  = cur_path
    reached_paths = [cur_path]
    # Si el nodo actual es el objetivo regresar el actual. Ya estamos en el objetivo
    if(cur_node == objective_node): 
        return cur_path
    # Si la frontera esta vacia entonces todavia hay nodos no expandidos
    while frontier:
        # Explorar el ultimo nodo agregado
        cur_path = frontier.pop()
        node_frontier.pop()
        children = expand_node(maze, cur_path[-1])
        # Explorar los hijos del nodo expandidos solamente si existen
        if(len(children)>0):
            # Examinar todos los hijos del nodo cur_node
            for child in children: 
                # Si se debe exportar un arbol entonces agregar el nodo actual 
                # como hijo de cur_node en el arbol
                child_path = cur_path + [child]
                if export_tree:
                    Tree_maze.add_node(child, cur_node)
                # Si el hijo es el nodo objetivo entonces SIEMPRE:
                if(child == objective_node):
                    Tree_maze.clear_generated_tree(export_tree)
                    reached.append(child)
                    reached_paths.append(child_path)
                    print_maze(get_maze_step(maze, reached, list(node_frontier),child_path), index_maze_step)
                    return child_path
                # Si este nodo no ha sido visitado colocarlo en la frontera y en los nodos ya visitados
                if not find_node(reached, child): 
                    reached_paths.append(child_path)
                    reached.append(child)
                    frontier.append(child_path)
                    node_frontier.append(child)
        # Imprimir esta paso en archivo maze(i).png
        print_maze(get_maze_step(maze, reached, list(node_frontier)), index_maze_step)
        # Incrementar el indice usado para imprimir archivos en maze(i).png
        index_maze_step+=1
    # En caso de no encontrar el nodo objetivo sobreescribir el archivo tree.tx 
    # si y solo export_tree es True

    Tree_maze.clear_generated_tree(export_tree)
