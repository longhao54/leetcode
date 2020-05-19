class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        # C 是数组 nums 元素的上限，C3 是 C 的立方根
        C, C3 = 100000, 46

        isprime = [True] * (C + 1)
        primes = list()

        # 埃拉托斯特尼筛法
        for i in range(2, C + 1):
            if isprime[i]:
                primes.append(i)
            for j in range(i + i, C + 1, i):
                isprime[j] = False
        
        # 欧拉筛法
        """
        for i in range(2, C + 1):
            if isprime[i]:
                primes.append(i)
            for prime in primes:
                if i * prime > C:
                    break
                isprime[i * prime] = False
                if i % prime == 0:
                    break
        """
        
        # 通过质数表构造出所有的四因数
        factor4 = dict()
        for prime in primes:
            if prime <= C3:
                factor4[prime**3] = 1 + prime + prime**2 + prime**3
        for i in range(len(primes)):
            for j in range(i + 1, len(primes)):
                if primes[i] * primes[j] <= C:
                    factor4[primes[i] * primes[j]] = 1 + primes[i] + primes[j] + primes[i] * primes[j]
                else:
                    break
        
        ans = 0
        for num in nums:
            if num in factor4:
                ans += factor4[num]
        return ans

