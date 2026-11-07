class Solution:
    def char_freq(self, characters):
        char_counter = {}
        for char in characters:
            if char in char_counter:
                char_counter[char] += 1
            else:
                char_counter[char] = 1

        return char_counter


result = Solution()
print(result.char_freq("banana"))