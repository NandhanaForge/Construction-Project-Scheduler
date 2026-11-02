
# STEP 4: BINARY SEARCH TREE

class Node:

    def __init__(self, deadline, task_name):

        self.deadline = deadline
        self.task_name = task_name

        self.left = None
        self.right = None


# Insert a task into BST
def insert(root, deadline, task_name):

    if root is None:
        return Node(deadline, task_name)

    if deadline < root.deadline:

        root.left = insert(
            root.left, deadline, task_name
        )

    else:

        root.right = insert(
            root.right, deadline, task_name
        )

    return root


# Display tasks in sorted order
def inorder(root):

    if root is not None:

        inorder(root.left)

        print(
            root.task_name,
            "- Deadline:",
            root.deadline,
            "days"
        )

        inorder(root.right)


# Main program
# Main program
if __name__ == "__main__":

    root = None

    print("===== BST TASK SCHEDULER =====")

    root = insert(root, 10, "Foundation")
    root = insert(root, 5, "Pillars")
    root = insert(root, 20, "Walls")
    root = insert(root, 15, "Roofing")
    root = insert(root, 25, "Painting")

    print("\nTasks Sorted by Deadline:\n")

    inorder(root)