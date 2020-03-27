class Solution:

    def sumFourDivisors(self, nums: List[int]) -> int:
        def get_primes(n: int) -> int:
            is_primes = [1] * n
            primes = []
            for i in range(2, int(n**0.5+1)):
                if is_primes[i]:
                    is_primes[i*i:n:i] = [0] * len(is_primes[i*i:n:i])
                    primes += i,
            return primes
        ans = 0
        primes = get_primes(max(nums))
        for n in nums:
            divisor = set([1, n])
            for p in primes:
                if len(divisor) > 4:
                    break;
                if n%p == 0:
                    divisor.add(p)
                    divisor.add(n)
                    while n%p == 0 and len(divisor) <= 4:
                        n //= p
                        divisor.add(n)
            #print(divisor)
            if len(divisor) == 4:
                ans += sum(divisor)
        return ans
