
class ExpressionNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def evaluate(node):
    if node.left is None and node.right is None:
        return float(node.value)

    left_value = evaluate(node.left)
    right_value = evaluate(node.right)

    if node.value == "+":
        return left_value + right_value
    elif node.value == "-":
        return left_value - right_value
    elif node.value == "*":
        return left_value * right_value
    elif node.value == "/":
        return left_value / right_value


def run_expression_tree():
    # Expression: (50000 + 30000 + 20000) * 1.10

    root = ExpressionNode("*")

    addition = ExpressionNode("+")
    addition.left = ExpressionNode(100000)
    addition.right = ExpressionNode(0)

    root.left = addition
    root.right = ExpressionNode(1.10)

    result = evaluate(root)

    print("\n===== CONSTRUCTION COST CALCULATOR =====")
    print("Base Construction Cost: Rs.", result / 1.10)
    print("Additional Cost: 10%")
    print("Total Construction Cost: Rs.", result)


if __name__ == "__main__":
    run_expression_tree()
