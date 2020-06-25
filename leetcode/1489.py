class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        parent = [i for i in range(n)]
        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            xp, yp = find(x), find(y)
            parent[xp] = yp
        
        weight = {}
        edge2idx = {}
        for idx, edge in enumerate(edges):
            weight.setdefault(edge[2], []).append(edge[:2])
            edge2idx[tuple(edge[:2])] = idx
        pseudo_critical = set()
        critical = set()
        def dfs(node, cur_depth):
            if depth[node]: return depth[node]
            min_depth = depth[node] = cur_depth
            for neighbor in tedges[node]:
                if depth[neighbor] == cur_depth - 1:
                    continue
                res = dfs(neighbor, cur_depth+1)
                if res <= cur_depth:
                    pseudo_critical.add(tedge2idx[node, neighbor])
                elif tedge2idx[(node, neighbor)] not in pseudo_critical:
                    critical.add(tedge2idx[node, neighbor])
                min_depth = min(min_depth, res)
            return min_depth
        for w in sorted(weight.keys()):
            tedges = {}
            tedge2idx = {}
            nodes = set()
            for src, dst in weight[w]:
                find(src)
                find(dst)
                if parent[src] == parent[dst]: continue
                if parent[src] in tedges.get(parent[dst], {}):
                    pseudo_critical.add(edge2idx[src, dst])
                    pseudo_critical.add(tedge2idx[parent[src], parent[dst]])
                    continue
                tedges.setdefault(parent[src], set()).add(parent[dst])
                tedges.setdefault(parent[dst], set()).add(parent[src])
                tedge2idx[parent[src], parent[dst]] = tedge2idx[parent[dst], parent[src]] = edge2idx[src, dst]
                nodes |= {parent[src], parent[dst]}
            #print(tedges, tedge2idx)
            depth = {node:0 for node in nodes}
            for node in nodes:
                dfs(node, 2)
            for src in tedges:
                for dst in tedges[src]:
                    if find(src) != find(dst):
                        union(src, dst)
        return critical, pseudo_critical
