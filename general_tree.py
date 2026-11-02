
class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def display_tree(node, level=0):
    print("  " * level + "|-- " + node.name)

    for child in node.children:
        display_tree(child, level + 1)


def run_general_tree():
    root = TreeNode("Construction Project")

    foundation = TreeNode("Foundation Phase")
    building = TreeNode("Building Phase")
    finishing = TreeNode("Finishing Phase")

    root.add_child(foundation)
    root.add_child(building)
    root.add_child(finishing)

    foundation.add_child(TreeNode("Excavation"))
    foundation.add_child(TreeNode("Concrete Work"))

    building.add_child(TreeNode("Pillars"))
    building.add_child(TreeNode("Walls"))
    building.add_child(TreeNode("Roofing"))

    finishing.add_child(TreeNode("Painting"))
    finishing.add_child(TreeNode("Electrical Work"))

    print("\n===== CONSTRUCTION PROJECT HIERARCHY =====")
    display_tree(root)


if __name__ == "__main__":
    run_general_tree()
