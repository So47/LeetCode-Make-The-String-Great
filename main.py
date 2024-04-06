class Solution:
    def makeGood(self, s: str) -> str:
        # stack = []
        # for char in s:
        #     if stack and abs(ord(stack[-1]) - ord(char)) == 32: # # ASCII difference between uppercase and lowercase is 32
        #         stack.pop()
        #     else:
        #         stack.append(char)
        # return ''.join(stack)            

        stack = []
        for char in s:
            if stack and (char.lower() == stack[-1].lower()) and char != stack[-1]: # Making sure that one is upper and second is lower as they won't equal each other
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)            
