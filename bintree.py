class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_tree(start, space=0, t=0):
    count = 3

    if start is None:
        return
    space += count
    print_tree(start.right, space, 1)
    for x in range(count, space):
        print(" ", end="")
    if t == 1:
        print("/", start.data)
    elif t == 2:
        print("\\", start.data)
    else:
        print(start.data)

    print_tree(start.left, space, 2)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print_tree(root)
