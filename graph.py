
class Graph:
    def __init__(self):
        self.graph = {}

    def add_dependency(self, task1, task2):
        if task1 not in self.graph:
            self.graph[task1] = []

        if task2 not in self.graph:
            self.graph[task2] = []

        self.graph[task1].append(task2)

    def display(self):
        print("\n===== TASK DEPENDENCY GRAPH =====")

        for task, neighbors in self.graph.items():
            print(task, "->", neighbors)

    def has_cycle(self):
        visited = set()
        recursion_stack = set()

        def dfs(task):
            visited.add(task)
            recursion_stack.add(task)

            for neighbor in self.graph[task]:

                if neighbor not in visited:
                    if dfs(neighbor):
                        return True

                elif neighbor in recursion_stack:
                    return True

            recursion_stack.remove(task)
            return False

        for task in self.graph:
            if task not in visited:
                if dfs(task):
                    return True

        return False


def run_graph():

    project = Graph()

    project.add_dependency("Foundation", "Pillars")
    project.add_dependency("Pillars", "Walls")
    project.add_dependency("Walls", "Roofing")
    project.add_dependency("Walls", "Electrical")
    project.add_dependency("Roofing", "Painting")
    project.add_dependency("Electrical", "Painting")

    project.display()

    print("\n===== CYCLE DETECTION =====")

    if project.has_cycle():
        print("Cycle detected!")
    else:
        print("No cycle detected. Dependencies are valid.")


if __name__ == "__main__":
    run_graph()
