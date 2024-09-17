class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        tree = collections.defaultdict(list)
        for i in range(n):
            if manager[i] != -1 :
                tree[manager[i]].append(i)

        def dfs(boss):
            if not tree[boss]:
                return 0
            
            max_time = 0
            for subordinate in tree[boss]:
                max_time = max(max_time, dfs(subordinate))
            
            return informTime[boss] + max_time
        
        # headID에서 시작하여 총 걸린 시간을 계산
        return dfs(headID)