class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def maximum_sum_any_path(node):
        ms, mp, _, _ = TreeNode.gain_from_subtree(node)
        return ms, mp

    @staticmethod
    def gain_from_subtree(node):
        # Things to return:
        # 1. max sum of a path
        # 2. path associated with that max sum
        # 3. max sum for a Contiguous path upto the node
        # 4. Path associated with that max contiguous path
        if node is None:
            return 0, [], 0, []

        l_max_sum, l_max_path, l_max_cont_sum, l_max_cont_path = TreeNode.gain_from_subtree(node.left)
        r_max_sum, r_max_path, r_max_cont_sum, r_max_cont_path = TreeNode.gain_from_subtree(node.right)
        if l_max_cont_sum > r_max_cont_sum:
            n_cont_sum, n_cont_path = (l_max_cont_sum + node.val, l_max_cont_path + [node])
        else:
            n_cont_sum, n_cont_path = (r_max_cont_sum + node.val, r_max_cont_path + [node])

        gain_options_so_far = [
            l_max_sum if l_max_path else float('-inf'), 
            r_max_sum if r_max_path else float('-inf'),
            node.val, 
            l_max_cont_sum + node.val, 
            r_max_cont_sum + node.val, 
            l_max_cont_sum + r_max_cont_sum + node.val]        
        max_gosf = gain_options_so_far.index(max(gain_options_so_far))
        if max_gosf == 0: # A non contiguous path on the left is the largest
            return l_max_sum, l_max_path, n_cont_sum, n_cont_path
        if max_gosf == 1: # A non contiguous path on the right is the largest
            return r_max_sum, r_max_path, n_cont_sum, n_cont_path
        if max_gosf == 2:
            return node.val, [node], node.val, [node]
        if max_gosf == 3: # A contiguous path going from left upto node is the largest
            return n_cont_sum, n_cont_path, n_cont_sum, n_cont_path
        if max_gosf == 4: # A contiguous path going from the right upto node is the largest
            return n_cont_sum, n_cont_path, n_cont_sum, n_cont_path
        if max_gosf == 5: # A path connecting left and right subtrees (through node) is the largest
            return (
                l_max_cont_sum + r_max_cont_sum + node.val, 
                l_max_cont_path + [node] + r_max_cont_path, 
                n_cont_sum,
                n_cont_path)


if __name__ == '__main__':
    assert TreeNode.maximum_sum_any_path(TreeNode(1, TreeNode(2), TreeNode(3)))[0] == 6
    assert TreeNode.maximum_sum_any_path(TreeNode(-1))[0] == -1
    assert TreeNode.maximum_sum_any_path(TreeNode(2, TreeNode(-1), TreeNode(-2)))[0] == 2
    