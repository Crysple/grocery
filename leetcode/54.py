class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def rotate(matrix):
            return [*zip(*matrix)][::-1]
        res = []
        while matrix:
            res.extend(matrix.pop(0))
            matrix = rotate(matrix)
        return res
            
