class ArrayStack:
    def __init__(self, name=''):
        self.data = []

    def size(self):
        print(len(self.data))
        return(len(self.data))

    def is_empty(self):
        if self.data != []:
            return False
        else:
            return True

    def push(self, input_data):
        self.data.append(input_data)

    def pop(self):
        if self.data == []:
            print('Underflow: Cannot pop data from an empty list')
            return None
        else:
            return self.data.pop()

    def stackTop(self):
        if self.data == []:
            return None
        else:
            return self.data[-1]

    def printStack(self):
        print(self.data)

#Lab 4.1
def is_parentheses_matching(expression):
    match_stack = ArrayStack()
    for char in expression:
        if char in ['(', '[', '{' ]:
            match_stack.push(char)
        elif char in [')', ']' , '}']:
            if match_stack.is_empty():
                return False
            elif char == '(' and match_stack.stackTop == ')':
                match_stack.pop()
            elif char == '[' and match_stack.stackTop == ']':
                match_stack.pop()
            elif char == '{' and match_stack.stackTop == '}':
                match_stack.pop()
            else:
                return False
    return match_stack.is_empty()

#lab 4.2
def copyStack(stack1, stack2):
    stack3 = ArrayStack()
    stack4 = ArrayStack()
    while stack2.is_empty() != True:
        stack2.pop()
    if stack1.is_empty == True: 
        return None
    else:
        while stack1.is_empty() != True:
            z = stack1.stackTop()
            stack4.push(z)
            x = stack1.pop()
            stack3.push(x)
        while stack3.is_empty() != True:
            y = stack3.pop()
            stack2.push(y)
        while stack4.is_empty() != True:
            t = stack4.pop()
            stack1.push(t)
    return stack1, stack2
            
#lab 4.3
def infixToPostfix(expression):
    operator = ArrayStack()
    postfix = ArrayStack()
    for char in expression:
        print(char)
        if char not in ['*', '+', '/', '-']:
            postfix.push(char)
        else:
            if char == '*' or char ==  '/':
                if operator.stackTop() == '*' or operator.stackTop() ==  '/': 
                    while operator.is_empty() != True:
                        x = operator.pop()
                        postfix.push(x)
                    operator.push(char)
                else:
                    operator.push(char)
            elif char == '+' or char ==  '-':
                if operator.is_empty() == True:
                    operator.push(char)
                else:
                    while operator.is_empty() != True:
                        x = operator.pop()
                        postfix.push(x)
                    operator.push(char)
            else:
                postfix.push(char)
    if operator.is_empty() != True:
        while operator.is_empty() != True:
            x = operator.pop()
            postfix.push(x)
    ans = str(postfix.data)
    ans = ans.replace('[', '').replace(']', '').replace(',', '').replace("'", '').replace(" ", '')
    return ans
exp = "A+B*C-D/E"
Postfix = infixToPostfix(exp)
print("Postfix of", exp, "is", Postfix)

# s1 = ArrayStack() 
# s1.push(10)
# s1.push(20)
# s1.push(30)

# s2 = ArrayStack()
# s2.push(15)

# copyStack(s1, s2)

# s1.printStack()
# s2.printStack()




