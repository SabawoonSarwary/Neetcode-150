class Solution:
    # First approach
    def unique_values_count(self, nums):
        seen = set()
        for num in nums:
            seen.add(num)
        return len(seen)

    # Second approach
    def Unique_Values_Count(self, nums):
        return len(set(nums))
        

result = Solution()
print(result.unique_values_count([4, 4, 7, 2, 7, 9, 9, 9]))
print(result.Unique_Values_Count([4, 4, 7, 2, 7, 9, 9, 9]))


