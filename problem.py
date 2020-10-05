from queue import PriorityQueue
import pygame
vec = pygame.math.Vector2


def dfs(graph, start, goal):
    visited = []
    path = []
    fringe = PriorityQueue()
    fringe.put((0, start, path, visited))

    while not fringe.empty():
        depth, current_node, path, visited = fringe.get()

        if current_node == goal:
            return path + [current_node]

        visited = visited + [current_node]

        child_nodes = graph[current_node]
        for node in child_nodes:
            if node not in visited:
                if node == goal:
                    return path + [node]
                depth_of_node = len(path)
                fringe.put((-depth_of_node, node, path + [node], visited))

    return path
  

walls = []
free = []

with open("walls.txt", 'r') as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char == '1':
                        walls.append(vec(xidx, yidx))
                        
                    elif char == "0":
                        free.append(vec(xidx, yidx))

le=27
hi=30


g = {}

pair = (0,0)
for vec in free:
    s = set()
    v = pygame.math.Vector2
    if (vec.x-1 >= 0):
        if (v(vec.x - 1, vec.y) in free):
            pair = (vec.x - 1, vec.y)
            s.add(pair)
    if (vec.y-1 >= 0):
        if (v(vec.x, vec.y-1) in free):
            pair = (vec.x, vec.y - 1)
            s.add(pair)
    if (vec.x+1 <= le):
        if (v(vec.x + 1, vec.y) in free):
            pair = (vec.x + 1, vec.y)
            s.add(pair)
    if (vec.y+1 <= hi):
        if (v(vec.x, vec.y+1) in free):
            pair = (vec.x, vec.y+1)
            s.add(pair)

    pair  = (vec.x, vec.y)    
    g[pair] = s


path = dfs(g, (1,1), (1,5))
print("path", path) # ==> [(1,2), (2,2), (2,3)]












