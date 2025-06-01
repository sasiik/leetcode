

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        nums_used = set()
        # print(nums)
        res = []
        for i in range(0, len(nums)):
            x = nums[i]
            if x in nums_used:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                # print('Nums:', x, nums[l], nums[r])
                current_sum3 = x + nums[l] + nums[r]
                if current_sum3 == 0:
                    # print('Current sum = 0 for', x, nums[l], nums[r])
                    res.append([x, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                elif current_sum3 > 0:
                    r -= 1
                else:
                    l += 1
            nums_used.add(x)
        # print('Nums used:', nums_used)
        return res


sol = Solution()
print(sol.threeSum([0, 0, 0, 0]))
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
