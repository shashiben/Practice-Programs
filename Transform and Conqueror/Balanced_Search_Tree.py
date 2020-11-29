class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def sortArrayToBST(arr):
    if not arr:
        return None
    mid = len(arr)//2
    root = TreeNode(arr[mid])
    root.left = sortArrayToBST(arr[:mid])
    root.right = sortArrayToBST(arr[mid+1:])
    return root


def preOrder(node):
    if not node:
        return
    print(node.data, end=" --> ")
    preOrder(node.left)
    preOrder(node.right)


arr = list(map(int, input("Enter values in 1 2 3 4 format:").split()))
root = sortArrayToBST(arr)
preOrder(root)
