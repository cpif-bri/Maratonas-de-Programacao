class Solution:
    def lengthOfLongestSubstring(s: str) -> int:
        letters = set()

        contMax = 0
        cont = 0
        left = 0

        for right in range(len(s)):
            if s[right] in letters:
                while s[left] != s[right]:
                    letters.remove(s[left])
                    left += 1
                left += 1  
                
            letters.add(s[right])
            cont = right - left + 1  
            contMax = max(contMax, cont)

        return contMax
        
print(Solution.lengthOfLongestSubstring('c') == 1)
print(Solution.lengthOfLongestSubstring('dvdf') == 3)
print(Solution.lengthOfLongestSubstring('bbbbb') == 1)
print(Solution.lengthOfLongestSubstring('abcabcbb') == 3)
print(Solution.lengthOfLongestSubstring('pwwkew') == 3)
print(Solution.lengthOfLongestSubstring(' ') == 1)