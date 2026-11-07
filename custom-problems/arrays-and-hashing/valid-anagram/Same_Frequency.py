class Solution:
    def same_freq(self, characters):
        sa_freq = {}
        for char in characters:
            if char in sa_freq:
                sa_freq[char] += 1
            else:
                sa_freq[char] = 1
        for key, value in list(sa_freq.items()):
            if value == 1:
                del sa_freq[key]
            

        return sa_freq


    def same_freq_using_multi_dict(self, characters):
        same_dict_1 = {}
        for char in characters:
            if char in same_dict_1:
                same_dict_1[char] += 1
            else:
                same_dict_1[char] = 1

        removing_singles = {}
        for key, value in same_dict_1.items():
            if value > 1:
                removing_singles[key] = value


        return removing_singles



        
result = Solution()
print(result.same_freq("banana"))
print(result.same_freq_using_multi_dict("banana"))