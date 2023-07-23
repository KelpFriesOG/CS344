class Graph:

    def __init__(self, vertices):
        self.V= vertices #No. of vertices
        self.graph = [] # default dictionary to store graph
        self.edges = [[]] * vertices
        self.v_edges = [None] * vertices
        self.priority = [None] * vertices

	# function to add an edge to graph
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])

	# A utility function to find set of an element i
	# (uses path compression technique)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

	# A function that does union of two sets of x and y
	# (uses union by rank)
    
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

		# Attach smaller rank tree under root of high rank tree
		# (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
		#If ranks are same, then make one as root and increment
		# its rank by one
        else :
            parent[yroot] = xroot
            rank[xroot] += 1

    def jarnik(self):
        
        return
    

    def jarnik_init(self, s):
        
        V = self.V
        E = self.edges
        
        for i in range(len(V)):
            if V[i] == s:
                continue
            
            else:
                try:
                    self.v_edges[i] = E[i][s]
                    self.priority[i] = E[i][s][1] 
                except:
                    self.v_edges[i] = None
                    self.priority[i] = 1000000
                    continue
        
                
        
        

def main():
    
    g = Graph(5)
    
    return

if __name__ == '__main__':
    main()