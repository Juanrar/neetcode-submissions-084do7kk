class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i:[] for i in range(n)}
        for value, connection in edges:
            graph[value].append(connection)
            graph[connection].append(value)
        
        visit = set()
        def dfs(node, prev):
            if node in visit:
                return False
            
            visit.add(node)
            for connection in graph[node]:
                if connection == prev:
                    continue
                if dfs(connection, node) == False:
                    return False
            return True

        return dfs(0,-1) and n == len(visit)
