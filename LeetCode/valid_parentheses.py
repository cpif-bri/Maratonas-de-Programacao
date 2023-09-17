class Solution:
    def isValid(s: str) -> bool:

        dict = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        stack = []

        for c in s:
            if len(stack) == 0 or c == '[' or c == '(' or c == '{':
                stack.append(c)
            else:
                if dict[c] == stack[len(stack) - 1]:
                    stack.pop()
                else:
                    return False
                
        return len(stack) == 0

print(Solution.isValid('[(])'))