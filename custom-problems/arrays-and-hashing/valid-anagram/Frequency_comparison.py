class Solution:
    def freq_comparing(self, word1, word2):
        freq_count_word1 = {}
        freq_count_word2 = {}

        for char in word1:
            if char in freq_count_word1:
                freq_count_word1[char] += 1
            else:
                freq_count_word1[char] = 1


        for lett in word2:
            if lett in freq_count_word2:
                freq_count_word2[lett] += 1
            else:
                freq_count_word2[lett] = 1


        if freq_count_word1 == freq_count_word2:
            return True
        return False



result = Solution()
print(result.freq_comparing("listen", "silent"))