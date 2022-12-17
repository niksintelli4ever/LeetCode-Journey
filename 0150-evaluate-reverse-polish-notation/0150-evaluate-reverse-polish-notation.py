class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i=="*":
                stack.append(int(stack.pop())*int(stack.pop()))
            elif i=='+':
                stack.append(stack.pop()+stack.pop())
            elif i=='-':
                a=stack.pop()
                b=stack.pop()
                stack.append(b-a)
            elif i=="/":
                a=stack.pop()
                b=stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(i))
        
        return stack[0]
                
        