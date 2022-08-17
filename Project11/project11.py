'''
Tuoxin Li
CS 5001
04/23/2022
project 11
'''

#class Stack: 
class Stack:
    def __init__(self, size):
        self.data = []
        self.size = size
    
    def push(self, item):
        if len(self.data) < self.size:
            self.data.append(item)           

    def pop(self):
        result = -1

        if self.data != []:
            result = self.data.pop()

        return result

#Class Queue
class Queue:
    def __init__(self, size):
        self.data = ["<EMPTY>"] * size
        self.end = 0
        self.start = 0
        self.size = size
        self.count=0

    def enqueue(self, item):
        if self.end >= len(self.data):
            print("Full!")
            return
        self.data[self.end] = item
        self.end += 1
        self.count+=1
        
    def dequeue(self):
        if self.start == self.end:
            print("Empty!")
            return
        item = self.data[0]
        self.end -= 1
        self.count-=1
        for i in range(0, self.end):
            self.data[i] = self.data[i + 1]

        return item


def operation(a,b,c):
    '''
    function:do operation
    return: number
    '''
    if c =="+":
        return a+b
    if c =="-":
        return a-b
    if c =="*":
        return a*b
    if c =="/":
        return a/b
    if c =="^":
        return a^b
        

def postfix_to_infix(pFix):
    '''
    Function: convert postfix into infix
    Params:String
    Return: Strting
    '''
    result = Stack(15)
    for i in pFix:    
        if i.isnumeric():
            result.push(i)
        else:
            operand1 = result.pop()#read the last number which is pushed
            operand2 = result.pop()#read the last second number which is pushed
            result.push(operand2 + str(i) + operand1)#need change the order so pust operand2 ahead

    return result.pop()
    

def infix_to_postfix(iFix):
    '''
    Function: convert postfix into infix
    Params:String
    Return: Strting
    '''
    result=""
    stack=Stack(15)
    count=0
    for i in iFix:
        if i.isnumeric():
            result+=i
        else:
            stack.push(i)
            count+=1
    for x in range(count):
        result+=stack.pop()

    return result


def postfix_compute(pFix):
    '''
    Function: calculate postfix
    Params:String
    Return: Integer
    '''
    stack=Stack(15)#stack for operators
    queue=Queue(15)#queue for operands
    count=0
    for i in pFix:
        if i.isnumeric():
            queue.enqueue(i)
        else:
            stack.push(i)
            count+=1
    a=int(queue.dequeue())
    b=int(queue.dequeue())
    result=operation(a,b,stack.pop())
    for i in range(count-1):
        result=operation(result,int(queue.dequeue()),stack.pop())
    return result

def infix_compute(iFix):
    '''
    Function: calculate infix
    Params:String
    Return: Integer
    '''
    stack=Stack(15)
    queue=Queue(15)
    count=0
    for i in iFix:
        if i.isnumeric():
            queue.enqueue(i)
        else:
            stack.push(i)
            count+=1
    a=int(queue.dequeue())
    b=int(queue.dequeue())
    result=operation(a,b,stack.pop())
    for i in range(count-1):
        result=operation(result,int(queue.dequeue()),stack.pop())
    return result

def main():
    
    '''
    You know you are done when all of these tests pass
    '''
    
    ''' infix_to_postfix tests '''
    
    print("infix_to_postfix test 1 : ", end="")
    if  infix_to_postfix("2+2") == "22+": print("PASS")
    else: print("FAIL")
    
    print("infix_to_postfix test 2 : ", end="")
    if  infix_to_postfix("1-3+2") == "132+-": print("PASS")
    else: print("FAIL")
    
    print("infix_to_postfix test 3 : ", end="")
    if  infix_to_postfix("1-3+3-4") == "1334-+-": print("PASS")
    else: print("FAIL")
    
    print()
    
    ''' postfix_to_infix tests '''
    
    print("postfix_to_infix test 1 : ", end="")
    if  postfix_to_infix("22+") == "2+2": print("PASS")
    else: print("FAIL")
    
    print("postfix_to_infix test 2 : ", end="")
    if  postfix_to_infix("14456++-+") == "1+4-4+5+6": print("PASS")
    else: print("FAIL")
    
    print("postfix_to_infix test 3 : ", end="")
    if  postfix_to_infix("123++") == "1+2+3": print("PASS")
    else: print("FAIL")
    
    print()
    
    ''' postfix_compute tests '''
    
    print("postfix_compute test 1 : ", end="")
    if  postfix_compute("123++") == 6: print("PASS")
    else: print("FAIL")
    
    print("postfix_compute test 2 : ", end="")
    if  postfix_compute("222-+") == 2: print("PASS")
    else: print("FAIL")
    
    print("postfix_compute test 3 : ", end="")
    if  postfix_compute("105++") == 6: print("PASS")
    else: print("FAIL")

    print()
    ''' infix_compute tests '''
    
    print("infix_compute test 1 : ", end="")
    if  infix_compute("1+2+3") == 6: print("PASS")
    else: print("FAIL")
    
    print("infix_compute test 2 : ", end="")
    if  infix_compute("2+2-2") == 2: print("PASS")
    else: print("FAIL")
    
    print("infix_compute test 3 : ", end="")
    if  infix_compute("1+0+5") == 6: print("PASS")
    else: print("FAIL")
    
   
main()