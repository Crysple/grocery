class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n_satisfied_customers = sum([c*(g^1) for c, g in zip(customers, grumpy)])
        
        start = end = ans = 0
        for end in range(len(customers)):
            if grumpy[end] == 1:
                    n_satisfied_customers += customers[end]
            if end >= X:
                if grumpy[start] == 1:
                    n_satisfied_customers -= customers[start]
                start += 1
            ans = max(ans, n_satisfied_customers)
        
        return ans
