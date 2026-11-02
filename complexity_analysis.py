
def linear_search(tasks, target):
    for i in range(len(tasks)):
        if tasks[i] == target:
            return i
    return -1


def binary_search(tasks, target):
    left = 0
    right = len(tasks) - 1

    while left <= right:
        mid = (left + right) // 2

        if tasks[mid] == target:
            return mid
        elif tasks[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def display_complexity():
    print("\n===== COMPLEXITY ANALYSIS =====")

    print("\n1. Linear Search")
    print("Recurrence: T(n) = T(n-1) + O(1)")
    print("Time Complexity: O(n)")

    print("\n2. Binary Search")
    print("Recurrence: T(n) = T(n/2) + O(1)")
    print("Time Complexity: O(log n)")

    print("\n3. Binary Search Tree (BST)")
    print("Balanced BST: O(log n) search")
    print("Worst Case BST: O(n) search")

    print("\n4. Graph Algorithms")
    print("Cycle Detection: O(V + E)")
    print("Topological Sorting: O(V + E)")
    print("Critical Path Analysis: O(V + E)")

    print("\n5. General Tree")
    print("Tree Traversal: O(n)")

    print("\n6. Expression Tree")
    print("Expression Evaluation: O(n)")

    print("\nV = Number of vertices")
    print("E = Number of edges")
    print("n = Number of elements")


def run_complexity_analysis():
    display_complexity()


if __name__ == "__main__":
    run_complexity_analysis()
