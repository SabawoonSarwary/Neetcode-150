class Solution:
    def hasDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False



result = Solution()
print(result.hasDuplicate([1, 2, 3, 3]))



