class Solution:
    def find_miss_val_using_sort(self, nums):
        sort = sorted(nums)                             # O(n log n)
        for num in range(0, len(sort) + 1):                   # O(n)
            if num != sort[num]:
                return num                             # n + n log n = O(n log n)

        return "Something is missing out"


    def find_miss_val_using_sum(self, nums):
        total = sum(nums)      # O(n)
        add_miss = sum(range(0, len(nums) + 1))             # O(n)
        return add_miss - total                               # n + n = O(n)


    def find_miss_val_using_dict(self, nums):
        nums_dict = {}                             # O(n)
        for num in nums:                         # O(n)
            nums_dict[num] = True
        for seq in range(0, len(nums) + 1):           # O(n)
            if seq not in nums_dict:
                return seq
        return "Something is missing out"


    def find_miss_val_using_set(self, nums):
        seen = set(nums)
        for num in range(0, len(seen) + 1):
            if num not in seen:
                return num
        return "Something is missing out"

    

result = Solution()
print(result.find_miss_val_using_sort([3, 0, 1]))
print(result.find_miss_val_using_sum([3, 0, 1]))
print(result.find_miss_val_using_dict([3, 0, 1]))
print(result.find_miss_val_using_set([3, 0, 1]))