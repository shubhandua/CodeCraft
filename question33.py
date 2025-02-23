class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_path_sum(root):
    max_sum = float('-inf')  # Global variable to store max sum

    def dfs(node):
        nonlocal max_sum
        if not node:
            return 0
        
        # Compute left and right max path sum (ignore negatives)
        left = max(dfs(node.left), 0)
        right = max(dfs(node.right), 0)
        
        # Update max path sum with the current node as root
        max_sum = max(max_sum, node.val + left + right)
        
        # Return max single path sum
        return node.val + max(left, right)

    dfs(root)
    return max_sum

# Example Usage
root = TreeNode(10, 
                TreeNode(2, TreeNode(20), TreeNode(1)), 
                TreeNode(10, None, TreeNode(-25, TreeNode(3), TreeNode(4))))

print("Maximum Path Sum:", max_path_sum(root))
