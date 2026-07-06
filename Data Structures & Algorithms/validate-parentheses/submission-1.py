class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            elif len(stack) != 0 and (c == ')' and stack[-1] == '('):
                stack.pop()
            elif len(stack) != 0 and (c == '}' and stack[-1] == '{'):
                stack.pop()
            elif len(stack) != 0 and (c == ']' and stack[-1] == '['):
                stack.pop()
            else:
                return False
        if len(stack) > 0:
            return False
        return True