class Solution:
    def countInterestingSubarrays(self, nums: list[int], modulo: int, k: int) -> int:
        import collections
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + ((x % modulo) == k))
        f = collections.Counter()
        count = 0
        # print(prefix)
        for x in prefix:
            count += f[(x-k) % modulo]
            f[x % modulo] += 1
        return count


sol = Solution()
print(sol.countInterestingSubarrays([3, 2, 4], 2, 1))
print(sol.countInterestingSubarrays([3, 1, 9, 6], 3, 0))
