class Solution:
    
    def ispar(self, x):
        stack = []
        
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in x:
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'
                
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)
        
        return not stack