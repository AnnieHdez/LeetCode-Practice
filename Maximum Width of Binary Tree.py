# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if root == None:
            return 0
        answer = -1
        left = 1
        rigth = 1
        root.val = 1
        q = [root]
        
        while len(q)>0:
            n = len(q)
            answer = max(answer,(q[n-1].val-q[0].val)+1)
            for i in range(n):
                current = q.pop(0)
                if current.left != None:
                    current.left.val = current.val * 2
                    q.append(current.left)
                if current.right != None:
                    current.right.val = (current.val * 2)+1
                    q.append(current.right)
                    
        return answer