class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive approach
def invert_tree_recursive(root):
    if not root:
        return None
    root.left, root.right = invert_tree_recursive(root.right), invert_tree_recursive(root.left)
    return root

# Iterative approach using queue (BFS)
from collections import deque

def invert_tree_iterative(root):
    if not root:
        return None
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        node.left, node.right = node.right, node.left  # Swap children
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return root

# Helper function to print level order traversal
def level_order_traversal(root):
    if not root:
        return []
    result, queue = [], deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

# Example Usage
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))

print("Original Tree (Level Order):", level_order_traversal(root))
inverted_root = invert_tree_recursive(root)
print("Inverted Tree (Level Order):", level_order_traversal(inverted_root))
