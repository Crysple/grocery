class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        if not N: return 0
        graph = [[] for _ in range(N+1)]
        prerequisite = [set() for _ in range(N+1)]
        queue = set(range(1, N+1))
        for conn in relations:
            graph[conn[0]].append(conn[1])
            prerequisite[conn[1]].add(conn[0])
            queue.discard(conn[1])
        semester = 0
        while queue:
            nqueue = []
            for src in queue:
                for dst in graph[src]:
                    prerequisite[dst].discard(src)
                    if not prerequisite[dst]:
                        nqueue.append(dst)
            queue = nqueue
            semester += 1
        if any(p for p in prerequisite): return -1
        return semester
