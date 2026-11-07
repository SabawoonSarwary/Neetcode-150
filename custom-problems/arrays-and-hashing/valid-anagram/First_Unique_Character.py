class Solution:
    def first_unique(self, word):
        fir_uniq = {}
        for char in word:
            if char in fir_uniq:
                fir_uniq[char] += 1
            else:
                fir_uniq[char] = 1


        
        for key, value in fir_uniq.items():
            if value == 1:
                return key
        return None
        


result = Solution()
print(result.first_unique('leetcode'))