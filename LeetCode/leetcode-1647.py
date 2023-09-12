class Solution:
    def minDeletions(s: str) -> int:
        lettersUsed = [0] * 26
        conjunto = set()
        elementos_retirados = 0

        for letra in s:
            lettersUsed[ord(letra) - ord('a')] += 1

        for num in lettersUsed:
            while num in conjunto:
                elementos_retirados += 1
                num -= 1
            if num > 0:
                conjunto.add(num)

        return elementos_retirados
            
print(Solution.minDeletions('aab') == 0)
print(Solution.minDeletions('aaabbbcc') == 2)
print(Solution.minDeletions('ceabaacb') == 2)
print(Solution.minDeletions('abcabc') == 3)
print(Solution.minDeletions('bbcebab') == 2)