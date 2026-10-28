class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        while s:
            match (s[0]):
                case '(' | '{' | '[':
                    stack.append(s[0])
                case ')':
                    if not stack: return False
                    top = stack.pop()
                    if top != '(': return False
                case '}':
                    if not stack: return False
                    top = stack.pop()
                    if top != '{': return False
                case ']':
                    if not stack: return False
                    top = stack.pop()
                    if top != '[': return False
            s = s[1:]
        return not stack