# Adjacency Matrix representation in Python

class Graph(object):

    # Initialize the matrix
    def __init__(self, size):
        self.v = size
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    # Add edges
    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = 1
        #self.adjMatrix[v2][v1] = 1

    # Remove edges
    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        #self.adjMatrix[v2][v1] = 0

    def __len__(self):
        return self.size

    # Print the matrix
    def print_matrix(self):
        for row in self.adjMatrix:
            print(row)            
    
    # Function to perform DFS on the graph
    def dfs(self, start, visited, nodes):    
        # Print current node        
        #print(start, end = ' ')
        nodes.append(start)
 
        # Set current node as visited
        visited[start] = True
 
        # For every node of the graph
        for i in range(self.v):
             
            # If some node is adjacent to the
            # current node and it has not
            # already been visited
            if (self.adjMatrix[start][i] == 1 and
                    (not visited[i])):
                self.dfs(i, visited, nodes)
        
        

def main():
    nodes, relations, tests =  input().split()
    nodes, relations, tests = [int(nodes),int(relations),int(tests)]
    names_list = []
    relations_list = []
    #print(nodes,relations,tests)
    for i in range(relations):
        a,b,c = input().split()
        relations_list.append([a,b,c]) 
        names_list.append(a) 
        names_list.append(b) 
        names_list.append(c) 
        #print(i)

    #print(relations)
    #print()
    #print(names_list)
    #print()
    names_list = list(set(names_list))
    names_list.sort()
    #print(names_list)
    #print(names_list.index('Bob'))
    g = Graph(nodes)
    for i in range(relations):
        #print(relations_list[i])
        #print(names_list.index(relations_list[i][0]))
        #print(names_list.index(relations_list[i][1]))
        #print(names_list.index(relations_list[i][2]))
        g.add_edge(names_list.index(relations_list[i][2]),
                   names_list.index(relations_list[i][0]))
        g.add_edge(names_list.index(relations_list[i][2]),
                   names_list.index(relations_list[i][1]))
        
    #g.print_matrix()
    #print(len(g.adjMatrix))
    for i in range(tests):
        a,b = input().split()
        # Perform DFS for a
        visited = [False] * nodes   
        nodes_a = []        
        g.dfs(names_list.index(a), visited, nodes_a)
        
        # Perform DFS for b
        visited = [False] * nodes    
        nodes_b = []      
        g.dfs(names_list.index(b), visited, nodes_b)
        
        result = len(set(nodes_a).intersection(set(nodes_b))) > 0
        if result:
            print('verdadeiro\n')
        else:
            print('falso\n')
        


if __name__ == '__main__':
    main()