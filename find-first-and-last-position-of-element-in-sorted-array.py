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
        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] < target:
                left += 1
            elif nums[middle] > target:
                right -= 1
            else: # middle equals target
                left = right = middle
                # find far left
                while (left - 1) >= 0 and nums[left - 1] == nums[middle]:
                    left -= 1
                # find far right
                while (right + 1) <= nums_len - 1 and nums[right + 1] == nums[middle]:
                    right += 1

                return [left, right]

        return [-1, -1]

solution = Solution()
print(solution.searchRange([5,7,7,8,8,10], 8))
print(solution.searchRange([5,7,7,8,8,10], 6))
print(solution.searchRange([], 0))
