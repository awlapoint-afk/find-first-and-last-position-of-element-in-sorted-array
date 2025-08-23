class Solution(object):
    def search_left(self, nums, start, end, target):
        left = start
        right = end

        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] == target:
                right = middle - 1
                if right < start:
                    return right + 1
            else:
                left = middle + 1

        return left

    def search_right(self, nums, start, end, target):
        left = start
        right = end - 1

        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] == target:
                left = middle + 1
                if left > end:
                    return left - 1
            else:
                right = middle - 1

        return right

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_len = len(nums)
        left = 0
        right = nums_len - 1
        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else: # middle equals target
                left = self.search_left(nums, 0, middle, target)
                right = self.search_right(nums, middle, nums_len, target)
                return [left,right]

        return [-1, -1]

solution = Solution()
print(solution.searchRange([5,7,7,8,8,10], 8))
print(solution.searchRange([5,7,7,8,8,10], 6))
print(solution.searchRange([], 0))
print(solution.searchRange([5,5,5,5,5,5,5,5,5,5,5], 5))
print(solution.searchRange([1,2,3,3,3,3,4,5,9], 3))
print(solution.searchRange([3,3,3], 3))