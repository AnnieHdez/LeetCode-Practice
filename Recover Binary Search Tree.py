# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(root, inorderAr):
            if root.left:
                inorder(root.left,inorderAr)
            
            inorderAr.append(root.val)
            
            if root.right:
                inorder(root.right,inorderAr)
                
        def swap(val, newVal, root, count):
            if root.val == val and count>0:
                root.val = newVal
                count-=1
            
            elif root.val == newVal and count>0:
                root.val = val
                count-=1    
            
            
            if root.left:
                swap(val, newVal, root.left, count)
            
            if root.right:
                swap(val, newVal, root.right, count)
            
        
        inorderAr = []
        inorder(root, inorderAr)
        sortedInorder = inorderAr.copy()
        sortedInorder.sort()
        n = len(inorderAr)
        
        first = 0
        second = 0
        
        firtstfound = False
        
        for i in range(n):
            if inorderAr[i] != sortedInorder[i]:
                if firtstfound:
                    second = inorderAr[i]
                    break
                else:
                    first = inorderAr[i]
                    firtstfound = True 
        swap(first, second, root, 2)
        return