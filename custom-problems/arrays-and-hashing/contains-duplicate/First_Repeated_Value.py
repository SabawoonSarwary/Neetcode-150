class Solution:
    def fir_rep_val(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return None


result = Solution()
print(result.fir_rep_val([4, 7, 2, 7, 9, 2]))
print(result.fir_rep_val([1, 2, 3, 4]))