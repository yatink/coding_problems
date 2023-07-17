class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_path_sum(root):
    if root is None:
        return 0, []
    # left path
    l_max, l_path = max_path_sum(root.left)
    l_max += root.val
    l_path.append(root.val)

    # right path
    r_max, r_path = max_path_sum(root.right)
    r_max += root.val
    r_path.append(root.val)

    if l_max > r_max:
        return l_max, l_path
    else:
        return r_max, r_path


left = TreeNode(1)
right = TreeNode(3)
r = TreeNode(5, left, right)


print(max_path_sum(r))
    
