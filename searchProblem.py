from queue import PriorityQueue
import threading, queue
from abc import ABC, abstractmethod


class SearchProblem(ABC):

    @abstractmethod
    def getStartState(self):
        util.raiseNotDefined()

    @abstractmethod
    def isGoalState(self, state):
        util.raiseNotDefined()

    @abstractmethod
    def getSuccessors(self, state):
        util.raiseNotDefined()


    def depthFirstSearch(graph, start, goal):
        visited = []
        path = []
        q = []
        q.append((start,path))
        while not len(q)==0:
            current_node, path = q.pop()
            if current_node == goal:
                return path + [current_node]
            visited = visited + [current_node]
            child_nodes = graph[current_node]
            for node in child_nodes:
                if node not in visited:
                    if node == goal:
                        return path + [node]
                    q.append((node, path + [node]))
        return path
        

    def breadthFirstSearch(graph, start, goal):
        visited = []
        path = []
        q = queue.Queue()
        q.put((start,path))
        while not q.empty():
            current_node, path = q.get()
            if current_node == goal:
                return path + [current_node]
            visited = visited + [current_node]
            child_nodes = graph[current_node]
            for node in child_nodes:
                if node not in visited:
                    if node == goal:
                        return path + [node]
                    q.put((node, path + [node]))
        return path
