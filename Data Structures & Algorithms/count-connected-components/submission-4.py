class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graphs = {i:[] for i in range(n)}
        for val,con in edges:
            graphs[val].append(con)
            graphs[con].append(val)
        
        visit = [False] * n
        def dfs(node):
            for con in graphs[node]:
                if not visit[con]:
                    visit[con] = True
                    dfs(con)
            

        result = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                result += 1
        return result
