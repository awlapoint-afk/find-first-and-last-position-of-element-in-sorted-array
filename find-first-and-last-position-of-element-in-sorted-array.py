class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_len = len(nums)

        left = 0
        right = nums_len - 1
        # search left
        left_result = -1
        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else: # middle equals target
                right = middle - 1
                left_result = middle

        left = 0
        right = nums_len - 1
        # search right
        right_result = -1
        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else: # middle equals target
                left = middle + 1
                right_result = middle

        return [left_result, right_result]

solution = Solution()
print(solution.searchRange([5,7,7,8,8,10], 8))
print(solution.searchRange([5,7,7,8,8,10], 6))
print(solution.searchRange([], 0))
print(solution.searchRange([5,5,5,5,5,5,5,5,5,5,5], 5))
print(solution.searchRange([1,2,3,3,3,3,4,5,9], 3))
print(solution.searchRange([3,3,3], 3))