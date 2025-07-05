class Solution:
    def binary_search(arr, target, l, r):
        left = l
        right = r

        if len(arr[l:r+1]) == 2:
            if arr[l] == target:
                return l
            elif arr[r] == target:
                return r
            else:
                return -1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1  # Element not found

    def search(self, nums: list[int], target: int) -> int:
        length = len(nums)

        # Check if the target is in the left (bigger) half or in the right (smaller) half
        isLeft = False

        if target == nums[0]:
            return 0
        if target > nums[0]:
            isLeft = True

        # Define cursors
        r = length - 1
        l = 0

        # While pointers are not correctly set (left number should be lower than the right number AND target should be between them)
        while (nums[l] > target or nums[r] < target) and r - l >= 2:
            middle_index = (r-l) // 2 + l  # Binary search
            # If we are working with the bigger side, we have to switch the right cursor, so that value on the right cursor is bigger than nums[l] and target
            if isLeft:
                # We are on the right track
                if nums[middle_index] > nums[l]:
                    if nums[middle_index] > target:
                        # We are now fine with switching the right cursor
                        r = middle_index
                    elif nums[middle_index] == target:
                        # Great
                        return middle_index
                    else:
                        # If the value at middle_index is less than the target, although it is bigger than the value on the left cursor
                        # , then we are almost fine, but we gotta switch the left cursor instead ?????
                        l = middle_index
                elif nums[middle_index] == nums[l]:
                    # Great, our cursors are near each other, jsut return this shit
                    return middle_index
                # We are NOT on the right track already, that means that we've reached the drop between two groups (nums[middle_index] < nums[l]), gotta swithc the right side there
                else:
                    r = middle_index
             # If we are working with the smaller side, we have to switch the left cursor, so that value on the left cursor is less than nums[r] and target
            else:
                if nums[middle_index] < nums[r]:
                    # We are on the right track
                    if nums[middle_index] < target:
                        # We are now fine with switching the right cursor
                        l = middle_index
                    elif nums[middle_index] == target:
                        # Great
                        return middle_index
                    else:
                        # If the value at middle_index is bigger than the target, although it is bigger than the value on the left cursor
                        # , then we are almost fine, but we gotta switch the right cursor instead ?????
                        r = middle_index
                elif nums[middle_index] == nums[r]:
                    # Great, our cursors are near each other, jsut return this shit
                    return middle_index
                # We are NOT on the right track already, that means that we've reached the drop between two groups (nums[middle_index] > nums[r]), gotta swithc the left side there
                else:
                    l = middle_index
        print(nums, target, l, r)
        return Solution.binary_search(nums, target, l, r)


sol = Solution()
print(sol.search([4, 5, 6, 7, 8, 9, 0, 1, 2, 3], 2))
print(sol.search([4, 5, 6, 7, 0, 1, 2], 3))
print(sol.search([3, 5, 1], 1))
print(sol.search([3, 5, 1], 3))
