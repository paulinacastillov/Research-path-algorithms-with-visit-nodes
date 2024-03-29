import os
import glob
from treelib import Node, Tree
import posixpath as path

class Tree_maze:
    root = None
    tree = Tree()

    def add_root(root):
        Tree_maze.tree.create_node('%i'%root,'%i'%root) 

    def add_node(child, parent):
        try: 
            Tree_maze.tree.create_node('%i'%child, '%i'%child, parent='%i'%parent)
        except: 
            return
    
    def print_tree():
        dirname = path.dirname(__file__)
        tree_files_path = path.join(dirname.split('\\src', 1)[0], 'tree/*')    
        files = glob.glob(tree_files_path)
        for f in files:
            os.remove(f)
        Tree_maze.tree.save2file('tree/tree.txt')
        Tree_maze.tree.show()

    def clear_tree():
        Tree_maze.tree = Tree()

    def clear_generated_tree(export_tree):
        if export_tree:
            Tree_maze.print_tree()
            Tree_maze.clear_tree()

