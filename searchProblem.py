from queue import PriorityQueue


class SearchProblem:

    def getStartState(self):
        util.raiseNotDefined()

    def isGoalState(self, state):
        util.raiseNotDefined()

    def getSuccessors(self, state):
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        util.raiseNotDefined()


    def depthFirstSearch(graph, start, goal):
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




