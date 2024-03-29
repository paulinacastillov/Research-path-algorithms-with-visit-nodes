#Used in debug
def print_matrix(matrix):
    for j in range(len(matrix[0])):
        if(j<10):
            print(j, end = '  ')
        else:
            print(j, end = ' ')
    print('')
    for j in range(len(matrix[0])):
        print('_', end='  ')
    print('')
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end = '  ')
        print('| ', i)

def find_node(list, node): 
    for item in list:
        if item == node:
            return True
    return False
