class Solution(object):
    def longestCommonPrefix(self,strs):
        prefix = strs[0]
        for words in strs[1:]:
            while not words.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

            