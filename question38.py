from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def right_view(root):
    if not root:
        return []

    queue = deque([root])
    result = []

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == level_size - 1:  # Add the last node of each level
                result.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result

# Example Usage
root = TreeNode(1, 
                TreeNode(2, None, TreeNode(5)), 
                TreeNode(3, None, TreeNode(4)))

print("Right View of Binary Tree:", right_view(root))
