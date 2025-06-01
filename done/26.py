class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # print(nums)
        lennums = len(nums)
        if lennums < 3:
            if lennums == 2 and nums[0] == nums[1]:
                return 1
            return lennums

        swap_pos = 1
        for _ in range(swap_pos, len(nums)):
            if nums[swap_pos] > nums[swap_pos - 1]:
                swap_pos += 1
            else:
                break
        for cur in range(swap_pos + 1, len(nums)):
            if nums[cur] != nums[cur-1]:
                nums[swap_pos] = nums[cur]
                swap_pos += 1
        # print(nums)
        return swap_pos


sol = Solution()
print(sol.removeDuplicates([1, 2, 3]))
