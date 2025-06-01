class Solution:
    def threeSumClosestDebug(self, nums: list[int], target: int) -> int:
        '''
            In a sorted array, choosing on 1 digit and then trying
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
        best_sum3 = float('inf')
        min_diff = abs(target - best_sum3)
        nums_used = set()
        for i in range(0, len(nums)):
            if nums[i] in nums_used:
                print(
                    f'I think that this nums[i]: {nums[i]} has already been used, skipping this..')
                continue
            print(f'Looping {i}/{len(nums)}..')

            l, r = i + 1, len(nums) - 1
            while l < r:
                print(
                    f'Nums[i]: {nums[i]}, Nums[l]: {nums[l]}, Nums[r]: {nums[r]}')
                current_sum3 = nums[i] + nums[l] + nums[r]
                print(f'Target: {target}')
                print('Current sum:', current_sum3)
                diff = abs(target - current_sum3)
                print('Current diff:', diff)
                if diff == 0:
                    print('Diff is 0, returning the sum immediately..')
                    return current_sum3
                elif current_sum3 > target:
                    print(
                        'Diff is bigger than 0 and sum is bigger than target, lowering the sum, switching r cursor..')
                    r -= 1
                else:
                    print(
                        'Diff is bigger than 0 and sum is less than or equal to target, increasing the sum, switching l cursor..')
                    l += 1
                if diff < min_diff:
                    print(
                        'Diff is less than minimal diff, changing min_diff and best_sum..')
                    min_diff = diff
                    best_sum3 = current_sum3
                    print(
                        f'Best sum now for current while loop: {best_sum3} with difference: {min_diff}')
            nums_used.add(nums[i])
        return best_sum3

    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        best_sum3 = float('inf')
        min_diff = abs(target - best_sum3)
        nums_used = set()
        for i in range(0, len(nums)-2):
            x = nums[i]
            if x in nums_used:
                continue

            lowest_sum = x + nums[i + 1] + nums[i + 2]
            if lowest_sum > target:
                if lowest_sum - target < min_diff:
                    min_diff = lowest_sum - target
                    best_sum3 = lowest_sum
                break
            highest_sum = x + nums[-1] + nums[-2]
            if highest_sum < target:
                if target - highest_sum < min_diff:
                    min_diff = target - highest_sum
                    best_sum3 = highest_sum
                continue
            l, r = i + 1, len(nums) - 1

            while l < r:
                current_sum3 = nums[i] + nums[l] + nums[r]
                diff = abs(target - current_sum3)
                if diff == 0:
                    return current_sum3
                elif current_sum3 > target:
                    r -= 1
                else:
                    l += 1
                if diff < min_diff:
                    min_diff = diff
                    best_sum3 = current_sum3
            nums_used.add(nums[i])
        return best_sum3


sol = Solution()
print(sol.threeSumClosestDebug([4, 0, 5, -5, 3, 3, 0, -4, -5], -2))
print('----------------------------------')
