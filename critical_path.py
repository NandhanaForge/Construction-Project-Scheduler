
class Project:
    def __init__(self):
        self.graph = {}
        self.duration = {}

    def add_task(self, task, duration):
        self.graph[task] = []
        self.duration[task] = duration

    def add_dependency(self, task1, task2):
        self.graph[task1].append(task2)

    def calculate_critical_path(self):
        indegree = {task: 0 for task in self.graph}

        for task in self.graph:
            for neighbor in self.graph[task]:
                indegree[neighbor] += 1

        queue = [
            task for task in indegree
            if indegree[task] == 0
        ]

        topological_order = []

        while queue:
            task = queue.pop(0)
            topological_order.append(task)

            for neighbor in self.graph[task]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(topological_order) != len(self.graph):
            print("Error: Dependency cycle detected!")
            return

        earliest_start = {
            task: 0 for task in self.graph
        }

        parent = {
            task: None for task in self.graph
        }

        for task in topological_order:
            earliest_finish = (
                earliest_start[task] + self.duration[task]
            )

            for neighbor in self.graph[task]:
                if earliest_finish > earliest_start[neighbor]:
                    earliest_start[neighbor] = earliest_finish
                    parent[neighbor] = task

        last_task = max(
            self.graph,
            key=lambda task: earliest_start[task] + self.duration[task]
        )

        project_duration = (
            earliest_start[last_task] + self.duration[last_task]
        )

        critical_path = []
        current = last_task

        while current is not None:
            critical_path.append(current)
            current = parent[current]

        critical_path.reverse()

        print("\n===== CRITICAL PATH ANALYSIS =====")
        print("Critical Path:", " -> ".join(critical_path))
        print("Total Project Duration:", project_duration, "days")


def run_critical_path():
    project = Project()

    # Add construction tasks and their durations
    project.add_task("Foundation", 5)
    project.add_task("Pillars", 4)
    project.add_task("Walls", 6)
    project.add_task("Roofing", 3)
    project.add_task("Electrical", 4)
    project.add_task("Painting", 2)

    # Add task dependencies
    project.add_dependency("Foundation", "Pillars")
    project.add_dependency("Pillars", "Walls")
    project.add_dependency("Walls", "Roofing")
    project.add_dependency("Walls", "Electrical")
    project.add_dependency("Roofing", "Painting")
    project.add_dependency("Electrical", "Painting")

    project.calculate_critical_path()


if __name__ == "__main__":
    run_critical_path()
