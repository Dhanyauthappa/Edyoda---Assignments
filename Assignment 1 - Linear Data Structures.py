#!/usr/bin/env python
# coding: utf-8

# ### Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?

# In[1]:


from itertools import combinations

def findPairs(lst, K):

    return [pair for pair in combinations(lst, 2) if sum(pair) == K]


lst=list(map(int,input("Enter integer element of an array separated by comma").split(",")))
K = int(input("Enter the sum value"))
print(findPairs(lst, K))


# ### Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

# In[2]:


def reverseArray(A):
    print( A[::-1])

A = list(map(int,input("Enter element of an array separated by comma").split(",")))
print("Original array is")
print(A)
print("Reversed array is")
reverseArray(A)


# ### Q3. Write a program to check if two strings are a rotation of each other?

# In[3]:


def Rotations(string1, string2):
    size1 = len(string1)
    size2 = len(string2)
    temp = ''

    # Check if sizes of two strings are same
    if size1 != size2:
        return 0
    
    temp = string1 + string1

    if (temp.count(string2)> 0):
        return 1
    else:
        return 0

# Driver program to test the above function
string1 = "AACD"
string2 = "ACDA"

if Rotations(string1, string2):
    print("Strings are rotations of each other")
else:
    print("Strings are not rotations of each other")


# ### Q4. Write a program to print the first non-repeated character from a string?

# In[11]:


from collections import Counter

def printNonrepeated(string):
    
    freq = Counter(string)

    for i in string:
        if(freq[i] == 1): 
            print(i)
            break

string = "Nice to Meet You"

printNonrepeated(string)


# ### Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.

# In[14]:


def towerofhanoi(n, A, C, B):
    if n == 0:
        return
    towerofhanoi(n-1, A, B, C)
    print("Move disk", n, "from rod", A, "to rod", C)
    towerofhanoi(n-1, B, C, A)

n = int(input())
towerofhanoi(n, 'A', 'C', 'B')


# ### Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

# In[9]:


def isOperator(x):
    
    if x == "+":
        return True

    if x == "-":
        return True

    if x == "/":
        return True
    
    if x == "*":
        return True

    return False

# Convert postfix to Prefix expression


def postToPre(post_exp):

    d = []

    # length of expression
    length = len(post_exp)

    # reading from right to left
    for i in range(length):

        # check if symbol is operator
        if (isOperator(post_exp[i])):

            # pop two operands from stack
            op1 = d[-1]
            d.pop()
            op2 = d[-1]
            d.pop()

            # concat the operands and operator
            temp = post_exp[i] + op2 + op1

            # Push string temp back to stack
            d.append(temp)

        # if symbol is an operand
        else:

            # push the operand to the stack
            d.append(post_exp[i])


    ans = ""
    for i in d:
        ans += i
    return ans


# Driver Code
if __name__ == "__main__":

    post_exp = "AB+CD-"
    
    # Function call
    print("Prefix : ", postToPre(post_exp))


# ### Q7. Write a program to convert prefix expression to infix expression.

# In[10]:


def prefixToInfix(prefix):
    stack = []

    # read prefix in reverse order
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):

            stack.append(prefix[i])
            i -= 1
        else:
            
            # symbol is operator
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1
    
    return stack.pop()

def isOperator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False

if __name__=="__main__":
    str = "*-A/BC-/DEB"
    print(prefixToInfix(str))


# ### Q8. Write a program to check if all the brackets are closed in a given code snippet.

# In[17]:


def brackets(x):
    d = []
 
    for i in x:
        if i in ["(", "{", "["]:
            d.append(i)
            
        else:
            if not d:
                return False
            temp_char = d.pop()
            if temp_char == '(':
                if i != ")":
                    return False
            if temp_char == '{':
                if i != "}":
                    return False
            if temp_char == '[':
                if i != "]":
                    return False
 
    if d:
        return False
    return True

x = "{()}[(]"
    
if brackets(x):
    print("Balanced")
else:
    print("Not Balanced")


# ### Q9. Write a program to reverse a stack.

# In[18]:


def reverseastack(stack):
    stack = reversed(stack)
    return list(stack)
stack = [11,12,13,14,15]

print("Original Stack", *stack, sep='\n')
print("Reversed Stack", *reverseastack(stack), sep='\n')


# ### Q10. Write a program to find the smallest number using a stack.

# In[21]:


def minvalue(stack):
    x=sorted(stack)
    return x[0]
    
stack=[50,7,4,3,-1]    
minvalue(stack)


# In[ ]:




