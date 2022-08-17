'''
Demo file for recursion for 5001
10/27/2021
Editted: 3/8/22

-Dr. G

'''

'''
Recursion is easy to explain, but sometimes hard to grasp. The key is remembering
what's happening on the stack when a function is called. 
'''

'''
Recursion involves a base case and a recursive call. Consider this function. 
Predict how many times it will run and then call it from main.
Draw out what's happening with the stack. 

What's the base case?
What's the recursive call?
'''

def recursivePrint(max, current):
    print("Woot")
    if current < max : recursivePrint(max, current+1)
    
'''
Recursion is NOT more efficient. In fact, recursion is always less efficient. 
However, it can just be more elagant and better model some problems.
Consider this example. Here recursion makes it more complex. 
'''
#Create a method that uses recursion to return the maximum 
#number in a list

def findMax(numList, current, max):
    print("Finding Max")
   
'''
Breakout 01 : Warm up with a simple pattern part 1

In your breakout groups, finish printPattern1 so that it prints the below pattern.

Step 1: Consider how each row is changing. What variable is controlling that?
Step 2: With each successive call how should the variable change?
Step 3: Consider your base case. What should you do/not do when you reach it?
        If you don't include a base case, you'll create infinite recursion.
Step 4: You likely have half the pattern now. How can you take advantage of 
        returning from recursion to print the other half? (Tip: how is num
        changed at each level of recursion?)

****
***
**
*
*
**
***
****

'''

def printPattern1(num):
    
    for i in range(num):
        print("*",end="")
    print()
    
'''
Breakout 1 : Test your understanding

In your breakout group walk through this code and see if you can explain the 
output to each other or your duck.
'''

def printThis(initial, maximum):
    
    print("Call 1 : ", initial)
    
    if(initial < maximum):
        printThis(initial + 1, maximum)
    
    print("Call 2 : ", initial)
    
'''
Breakout 2 : Convert a non-recursive solution to a recursive one, simple

In your breakout group walk through this code then see if you can implement a 
recursive solution. 

 The recursive solution goes something like this: 
   
    Step 1 : if you are at the base case return 1
    Step 2 : other wise return the current num multiplied by the factorial of 
    the previous number
'''
#Factorial of n = n * factorial(n - 1)
#Base case: Factorial of 0 = 1
#Base case: Factorial of 1 = 1
#Study the provided non-recursive solution
#Comment it out and implement a recursive solution

def factorial(num):    
    if(num <= 1):
        return 1
    else:
        return num * factorial(num - 1) 
    

'''
    The recursive solution goes something like this: 
   
    Step 1 : if you are at the base case return 1
    Step 2 : other wise return the current num multiplied by the factorial of the previous number
    '''
   
'''
    SOLUTION
    if(num <= 1):
        return 1
    else:
    return num * factorial(num - 1)
'''
   
'''
Breakout 3 Convert a non-recursive solution to a recursive one, intermediate

Fibonacci Series 
The fibonacci series is a pattern of numbers that often shows up in math
and biology. Do a quick web search to learn more.
	
Except for 0 and 1 every number is the sum of the fibonacci of the previous 2
fib(0) = 0; fib(1) = 1; fib(num) = fib(n-1) + fib(n-2)
Fib Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
	
//This function returns the fibonacci at a given position

	#The recursive solution is actually much simpler
	1. check the base case(s)
    2. return the fibonacci of the previous plus the fibonacci of 2 previous
	
	After you've figured out the solution draw it out on paper to check your
	understanding. 
	
	Remember recursion eliminates the need for a loop.

'''

#Reivew what the fibbonacci series is
#Study the non-recursive solution below and implement a recursive one 
def fib(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fib(num-1)+fib(num-2)


'''
	SOLUTION
	if (num == 0 or num == 1):
		return num 
	else:
		return fib(num-1) + fib(num-2)
	'''

	
'''
Breakout 4 Convert a non-recursive solution to a recursive one, intermediate+

A palindrome is a word that reads the same backwards as forwards. 
Example: 
racecar tacocat bob

This method returns true if something is a palindrome and false otherwise

A recursive solution would work something like this: 

	1. Check to see if the current string is only 1 character or 0 characters
	   this is your base case. If you've reached this point you have a palindrome
	2. Check the first character and the last character of the current string
	   to see if they match. If they do, call the method again, but with the 
	   smaller string
	3. If your first and last characters don't ever match, it's not a palindrome
	
	Tip: recursion replaces the loop.
	
'''
def palindromeCheck(data):
    #Non-recursive solution
    # length = len(data)
    # substring = data

    # while(length > 1):
    #     if (substring[0] == substring[length -1]):
    #         substring = substring[1 : (len(substring) - 1)]
    #         length = len(substring)
    #     else: return False
	
    # return True

    # base case 
	if(len(data) == 0 or len(data) == 1): 
	    return True
	    
	if(data[0] == data[len(data)-1]): 
	    return palindromeCheck(data[1 : (len(data)-1)])


	    
print(palindromeCheck("bouob"))


'''
Breakout 5 : Bonus round. This one is advanced...

Give this a shot as well, but we'll go over the solution in class. 

'''
#This method produces the correct sequence of moves to successfully complete the 
# tower of hanoi puzzle
# I'm not going to provide the non-recursive solution this time

# Before you begin play the game a few times to make sure you understand it: 
# https://www.mathsisfun.com/games/towerofhanoi.html

#5. Using the provided instructions code up a Tower's of Hanoi Solver
def solveTowers(disks, sourcePeg, destPeg, tempPeg):
    print("Towers Solver")
    #You have three pegs 1 2 3
    #disks is how many disks you have to move
    #sourcePeg is the peg you are moving to 1, 2, or 3
    #tempPeg is a holding location 1, 2, or 3
    #Use the simulator from above to visualize what the numbers really mean
    
    #The solution has 6 lines of code, and two recursive calls


    #1. if there is only 1 disk move it to the destination peg and you are done. 
    #   Prove this to yourself by solving for 1 peg.
    
    # print(sourcePeg , "---->" , destPeg)

    #2. if there is more than one peg we need to solve the problem for one less
    #   disk, but we need to swap our destPeg and tempPeg cause we want to store
    #   this peg temporarily on our destination spot. Prove this to yourself
    #   by walking through a case of two disks.

    #  Now we have to start thinking recursively.

    #3. When you get down to 1 disk, your recursion will end, (see step 1) and 
    #   you'll know which peg should be your destination for the top disk.
    
    #4. You'll also know where the disk that's left on top should go. It can't 
    #   go on top of the disk that was moved because that disk is smaller, but 
    #   when we come back from the recursive call the temp and destination will 
    #   be restored to the previous call. 
    
    # print(sourcePeg , "---->" , destPeg)

    #5. Now that you've moved those two disks the problem is the same as before, 
    #   but what you need to do is figure out how to move the disks that are
    #   currently on the temp peg to the destination. So recursively call it
    #   again, but your temp is your source and your source is your temp. Why
    #   can you use your source as your temp? Because you know what?
    
    
    #SOLUTION
    if(disks == 1):
        print(sourcePeg , "---->" , destPeg)
        return
    
    solveTowers(disks - 1, sourcePeg, tempPeg, destPeg)
    print(sourcePeg , "---->" , destPeg)
    solveTowers(disks - 1 , tempPeg, destPeg, sourcePeg)

        
        
def printThis(thing):
    print(thing)
        
def main():
    printThis("Begin main")
    
    #recursivePrint(3, 0)
    #print(findMax([1,9,3,4],0,0))
    
    #0. warm up
    #printPattern1(4)

    #1. intial test
    #printThis(0,4)
    
    #2. calculate the factorial
    #print(factorial(4))
    
    #3. Determine the fibonacci value
    #print(fib(3))
    
    #4. Check to see if something is a palindrome
    #print(palindromeCheck("bob"))
    
    #5. Problem of hanoi solver
    #parem1 -> number of disks
    #parem2 -> current source peg
    #parem3 -> current destination peg
    #parem4 -> current temporary holding peg
    #solveTowers(3,1,3,2)
    
main()
        
        



