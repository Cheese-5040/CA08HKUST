from collections import defaultdict

class Graph: 
    # constructor
    def __init__(self):
        self.graph = defaultdict(list)

    # add edge to Graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def breathFirstSearch(self,s):
        # mark all unvisited vertex
        visited = [False]*(max (self.graph)+1)
        # create queue for BFS
        queue=[]

        # add to queue once the node is visited
        #enwueue it (add to queue)
        queue.append(s)

        visited[s]=True

        while queue:
            # dequeue vertex from queue, print it 
            s=queue.pop(0)
            print (s, end =" ")

            for i in self.graph[s]: 
                if visited[i] == False: 
                    queue.append(i)
                    visited[i] = True

from collections import deque


def find_path_bfs(maze):
    start, goal = (1, 1), (len(maze) - 2, len(maze[0]) - 2)
    queue = deque([("", start)])
    visited = set()
    graph = maze2graph(maze)
    while queue:
        path, current = queue.popleft()
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for direction, neighbour in graph[current]:
            queue.append((path + direction, neighbour))
    return "NO WAY!"
# main code 
# create graph 
g = Graph()
g.addEdge(0,1)#from 0, you can go to 1
g.addEdge(0,2)#from 0, you can go to 2
g.addEdge(1,2)#from 1, you can go to 2
g.addEdge(2,0)#from 2, you can go to 0
g.addEdge(2,3)
g.addEdge(3,3)

# g.addEdge(1,2)
# g.addEdge(1,3)
# g.addEdge(2,4)
# g.addEdge(2,5)
# g.addEdge(3,5)
# g.addEdge(4,5)
# g.addEdge(4,6)
# g.addEdge(5,6)

print("breath first search from vertex 2")
g.breathFirstSearch(2)

