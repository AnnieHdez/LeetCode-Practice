class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return 0
        answer = defaultdict(list)
        maxi = 0
        mini = 10001
        q = [root]
        values = [0]
        while len(q)>0:
            n = len(q)
            level = defaultdict(list)
            for i in range(n):
                current = q.pop(0)
                parent = values.pop(0)
                if parent > maxi:
                    maxi = parent
                if parent < mini:
                    mini = parent
                level[parent].append(current.val)
                if current.left != None:
                    values.append(parent-1)
                    q.append(current.left)
                if current.right != None:
                    values.append(parent+1)
                    q.append(current.right)
            for val in level:
                level[val].sort()
                answer[val]+=level[val]
        ret = [0]*((maxi-mini)+1)
        # ret=[]
        for val in answer:
            ret[val-mini]=answer[val]
            
        return ret