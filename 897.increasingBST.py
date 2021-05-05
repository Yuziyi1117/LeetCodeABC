# -*- coding:utf-8 -*-

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        root = TreeNode()
        self.res = []
        self.inOrder(root)
        if not self.res:
            return
        dummy = TreeNode(-1)
        cur = dummy
        for node in self.res:
            node.left = node.right = None
            cur.right = node
            cur = cur.right
        return dummy.right
        #中序遍历递归先左再右
    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        self.res.append(root)
        self.inOrder(root.right)


if __name__ == "__main__":

    null =None

    root = [5, 3, 6, 2, 4, null, 8, 1, null, null, null, 7, 9]
    root1 = TreeNode(root)
    print(root1.val)
    abc = Solution()
    abc1 =abc.increasingBST(root1)
    print(abc1.val)