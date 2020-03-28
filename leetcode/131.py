class Solution:
    def __init__(self):
        self.d = {"": [[]]}
    def partition(self, s: str) -> List[List[str]]:
        
        # Implementation 2: return list of list: might be O()
        partitions = list()
        def _partition(path, substr):
            if not substr:
                partitions.append(path)
            for i in range(1, len(substr)+1):
                if substr[:i] == substr[:i][::-1]:
                    _partition(path+[substr[:i]], substr[i:])
        _partition([], s)
        return partitions

        # Implementation 1: return list of list: might be O()
        if s in self.d:
            return self.d[s]
        self.d[s] = list()
        for i in range(1, len(s)+1):
            if s[:i] == s[:i][::-1]:
                substr_partitions = self.partition(s[i:])
                self.d[s].extend([[s[:i]]+partition for partition in substr_partitions])
        return self.d[s]
