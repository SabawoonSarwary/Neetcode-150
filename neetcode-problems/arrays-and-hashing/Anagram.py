class Solution:
    def valid_anagram(self, word1, word2):
        if len(word1) != len(word2):
            return False

        dict_1 = {}
        dict_2 = {}

        for char in word1:
            if char in dict_1:
                dict_1[char] += 1
            else:
                dict_1[char] = 1


        for lett in word2:
            if lett in dict_2:
                dict_2[lett] += 1
            else:
                dict_2[lett] = 1

        if dict_1 == dict_2:
            return True
        return False



result = Solution()
print(result.valid_anagram("listen", "silent"))
print(result.valid_anagram("Ab", "ab"))

