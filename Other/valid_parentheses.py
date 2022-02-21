class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []

        for c in s:
            # opening brackets
            if c == '(' or c == '[' or c == '{':
                stack.append(c)

            # if it starts off with a closing bracket
            elif len(stack) == 0:
                return False

            # closing brackets
            elif pairs[c] != stack[-1]:
                return False

            else:
                stack.pop()

        if len(stack) == 0:
            return True

        return False

    def isValidLessLines(self, s):
        stack = [0]
        mapping = {0: None, '(': ')', '[': ']', '{': '}'}
        for c in s:
            if c in mapping:
                stack.append(c)
            else:
                if mapping[stack.pop()] != c: return False
        return stack == [0]