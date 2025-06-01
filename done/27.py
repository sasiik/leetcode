class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        lennums = len(nums)
        i = 0
        while i < lennums:
            if nums[i] == val:
                nums.pop(i)
                lennums -= 1
            else:
                i += 1
        return lennums

    def removeElement2(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


sol = Solution()
print(sol.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
