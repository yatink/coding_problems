class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def max_diameter(node):
        if node is None:
            return 0, 0

        l_max_length_so_far, l_max_contiguous_length = TreeNode.max_diameter(node.left)
        r_max_length_so_far, r_max_contiguous_length = TreeNode.max_diameter(node.right)

        # Diameter of Path that includes the current node
        max_length_including_node = l_max_contiguous_length + r_max_contiguous_length + 1 

        # Max diameter of path calculated so far
        max_length_so_far = max(l_max_length_so_far, r_max_length_so_far)

        # Max contiguous path including the current node
        max_path_till_node = max(l_max_contiguous_length, r_max_contiguous_length) + 1
        if max_length_including_node > max_length_so_far: 
            # If the max diameter is the path the passes through the current node
            return max_length_including_node, max_path_till_node
        # It's a different path 
        return max_length_so_far, max_path_till_node
    

if __name__ == "__main__":
    assert TreeNode.max_diameter(TreeNode(13)) == 1, 1
