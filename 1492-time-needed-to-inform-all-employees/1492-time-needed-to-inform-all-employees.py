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

        queue = collections.deque()
        queue.append((headID, 0))
        t = 0

        while queue:
            boss, time_needed = queue.popleft()
            t = max(t, time_needed)
            
            for subord in tree[boss]:
                queue.append((subord, time_needed + informTime[boss]))

        return t