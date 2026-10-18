class Solution:
    def frequency_count(self, nums):
        freq_count = {}
        for num in nums:
            if num in freq_count:
                freq_count[num] += 1
            else:
                freq_count[num] = 1


        return freq_count


result = Solution()
print(result.frequency_count([2, 5, 2, 7, 5, 2, 9]))