
from collections import deque


class Graph:
    def __init__(self):
        self.graph = {}

    def add_dependency(self, task1, task2):
        if task1 not in self.graph:
            self.graph[task1] = []

        if task2 not in self.graph:
            self.graph[task2] = []

        self.graph[task1].append(task2)

    def topological_sort(self):

        indegree = {
            task: 0 for task in self.graph
        }

        for task in self.graph:
            for neighbor in self.graph[task]:
                indegree[neighbor] += 1

        queue = deque()

        for task in indegree:
            if indegree[task] == 0:
                queue.append(task)

        order = []

        while queue:
            current = queue.popleft()
            order.append(current)

            for neighbor in self.graph[current]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(order) != len(self.graph):
            print("Cycle detected! No valid task order.")
            return

        print("\n===== CONSTRUCTION TASK ORDER =====")

        for number, task in enumerate(order, start=1):
            print(number, ".", task)


def run_topological_sort():

    project = Graph()

    project.add_dependency("Foundation", "Pillars")
    project.add_dependency("Pillars", "Walls")
    project.add_dependency("Walls", "Roofing")
    project.add_dependency("Walls", "Electrical")
    project.add_dependency("Roofing", "Painting")
    project.add_dependency("Electrical", "Painting")

    project.topological_sort()


if __name__ == "__main__":
    run_topological_sort()

