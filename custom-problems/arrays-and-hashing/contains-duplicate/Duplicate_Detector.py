class Solution:
    def duplicate_detector(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False



result = Solution()
print(result.duplicate_detector([4, 7, 3, 9, 2, 3, 8, 1]))




