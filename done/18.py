class Solution:
    def fourSumDebug(self, nums: list[int], target: int) -> list[list[int]]:
        '''
            In a sorted array, choosing on 2 digit and then trying
            to calculate last 2 digits sum using 2 pointers technique.
            We compare, where the sum is placed on the x axis relatively
            to the target, and based on that,
            we switch either l or r cursors right or left correspondingly

            This will continue until l and r cursors take the same spot
            in the array or go beyond each other

            for each while loop, there is min_diff and best_sum. After we go through while loop, we also compare
            min_diff for the while loop with global min_diff, and then change the global best_sum to the while loop best_sum if needed
        '''
        nums.sort()
        print('Sorted nums:', nums)
        nums_used = set()
        res = []

        if len(nums) < 4:
            return []
        else:
            lowest_sum = nums[0] + nums[1] + nums[2] + nums[3]
            highest_sum = nums[-4] + nums[-3] + nums[-2] + nums[-1]
            if lowest_sum > target or highest_sum < target:
                return []

        for i in range(0, len(nums)-3):
            for j in range(i+1, len(nums)-2):
                highest_sum_curr = nums[i] + nums[j] + nums[-2] + nums[-1]
                if highest_sum_curr < target:
                    continue
                if (nums[i], nums[j]) in nums_used or (nums[j], nums[i]) in nums_used:
                    print(
                        f'I think that this nums[i]: {nums[i]} and nums[j]: {nums[j]} have already been used, skipping this..')
                    continue
                print(f'Looping {i}/{len(nums)}, {j}/{len(nums)}..')

                l, r = j + 1, len(nums) - 1
                while l < r:
                    print(
                        f'Nums[i]: {nums[i]}, Nums[j]: {nums[j]} Nums[l]: {nums[l]}, Nums[r]: {nums[r]}')
                    current_sum4 = nums[i] + nums[j] + nums[l] + nums[r]
                    print(f'Target: {target}')
                    print('Current sum:', current_sum4)
                    diff = abs(target - current_sum4)
                    print('Current diff:', diff)
                    if diff == 0:
                        print(
                            f'Diff is 0, adding numbers: {(nums[i], nums[j], nums[l], nums[r])}')
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            print(
                                f'Nums[l] is the same as Nums[l-1]: {nums[l-1]}, skipping to the next..')
                            l += 1
                    elif current_sum4 > target:
                        print(
                            'Diff is bigger than 0 and sum is bigger than target, lowering the sum, switching r cursor..')
                        r -= 1
                    else:
                        print(
                            'Diff is bigger than 0 and sum is less than or equal to target, increasing the sum, switching l cursor..')
                        l += 1
                nums_used.add((nums[i], nums[j]))
        return res

    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        nums_used = set()
        res = []
        if len(nums) < 4:
            return []
        else:
            lowest_sum = nums[0] + nums[1] + nums[2] + nums[3]
            highest_sum = nums[-4] + nums[-3] + nums[-2] + nums[-1]
            if lowest_sum > target or highest_sum < target:
                return []
        for i in range(0, len(nums)-3):
            for j in range(i+1, len(nums)-2):
                highest_sum_curr = nums[i] + nums[j] + nums[-2] + nums[-1]
                if highest_sum_curr < target:
                    continue
                if (nums[i], nums[j]) in nums_used or (nums[j], nums[i]) in nums_used:
                    continue
                l, r = j + 1, len(nums) - 1
                while l < r:
                    current_sum4 = nums[i] + nums[j] + nums[l] + nums[r]
                    diff = abs(target - current_sum4)
                    if diff == 0:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif current_sum4 > target:
                        r -= 1
                    else:
                        l += 1
                nums_used.add((nums[i], nums[j]))
        return res


sol = Solution()
print(sol.fourSumDebug([-2, -1, -1, 1, 1, 2, 2], 0))
print('----------------------------------')
