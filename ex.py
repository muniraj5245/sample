
# # # # # # # # # # # # # # # # # # # MAX_CHAR = 26
# # # # # # # # # # # # # # # # # # # def arrangeString(string):
# # # # # # # # # # # # # # # # # # # 	char_count = [0] * MAX_CHAR
# # # # # # # # # # # # # # # # # # # 	s = 0
# # # # # # # # # # # # # # # # # # # 	for i in range(len(string)):
# # # # # # # # # # # # # # # # # # # 		if string[i] >= "A" and string[i] <= "Z":
# # # # # # # # # # # # # # # # # # # 			char_count[ord(string[i]) - ord("A")] += 1
# # # # # # # # # # # # # # # # # # # 		else:
# # # # # # # # # # # # # # # # # # # 			s += ord(string[i]) - ord("0")
# # # # # # # # # # # # # # # # # # # 	res = ""
# # # # # # # # # # # # # # # # # # # 	for i in range(MAX_CHAR):
# # # # # # # # # # # # # # # # # # # 		ch = chr(ord("A") + i)
# # # # # # # # # # # # # # # # # # # 		while char_count[i]:
# # # # # # # # # # # # # # # # # # # 			res += ch
# # # # # # # # # # # # # # # # # # # 			char_count[i] -= 1
# # # # # # # # # # # # # # # # # # # 	if s > 0:
# # # # # # # # # # # # # # # # # # # 		res += str(s)
# # # # # # # # # # # # # # # # # # # 	return res
# # # # # # # # # # # # # # # # # # # string = input()
# # # # # # # # # # # # # # # # # # # print(arrangeString(string))

# # # # # # # # # # # # # # # # # # # n=int(input())
# # # # # # # # # # # # # # # # # # # m=[]
# # # # # # # # # # # # # # # # # # # for i in range(n):
# # # # # # # # # # # # # # # # # # # 	l=list(map(int,input().split()))
# # # # # # # # # # # # # # # # # # # 	m.append(l)
# # # # # # # # # # # # # # # # # # # temp = [sum(i) for i in zip(*m)]
# # # # # # # # # # # # # # # # # # # res=[]
# # # # # # # # # # # # # # # # # # # for ele in temp:
# # # # # # # # # # # # # # # # # # #     res.append(ele / len(m))
# # # # # # # # # # # # # # # # # # # minpos=res.index(min(res))
# # # # # # # # # # # # # # # # # # # for i in m:
# # # # # # # # # # # # # # # # # # # 	if type(i)==list:
# # # # # # # # # # # # # # # # # # # 		for j in i:
# # # # # # # # # # # # # # # # # # # 			del i[minpos]
# # # # # # # # # # # # # # # # # # # print(m)



# # # # # # # # # # # # # # # # # # # n=int(input())
# # # # # # # # # # # # # # # # # # # l=[]
# # # # # # # # # # # # # # # # # # # for i in range(n):
# # # # # # # # # # # # # # # # # # #   a=int(input())
# # # # # # # # # # # # # # # # # # #   l.append(a)
# # # # # # # # # # # # # # # # # # # sum=0
# # # # # # # # # # # # # # # # # # # for i in l:
# # # # # # # # # # # # # # # # # # #   p=i/10
# # # # # # # # # # # # # # # # # # #   q=i%10
# # # # # # # # # # # # # # # # # # #   sum+=p**q
# # # # # # # # # # # # # # # # # # # print(sum)

# # # # # # # # # # # # # # # # # # # Python program to convert a
# # # # # # # # # # # # # # # # # # # number from any base to decimal

# # # # # # # # # # # # # # # # # # # To return value of a char.
# # # # # # # # # # # # # # # # # # # For example, 2 is returned
# # # # # # # # # # # # # # # # # # # for '2'. 10 is returned for 'A',
# # # # # # # # # # # # # # # # # # # 11 for 'B'

# # # # # # # # # # # # # # # # # # # def val(c):
# # # # # # # # # # # # # # # # # # #  if c >= '0' and c <= '9':
# # # # # # # # # # # # # # # # # # #   return ord(c) - ord('0')
# # # # # # # # # # # # # # # # # # #  else:
# # # # # # # # # # # # # # # # # # #   return ord(c) - ord('A') + 10
# # # # # # # # # # # # # # # # # # # def reVal(num):
# # # # # # # # # # # # # # # # # # #     if (num >= 0 and num <= 9):
# # # # # # # # # # # # # # # # # # #         return chr(num + ord('0'));
# # # # # # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # # # # # #         return chr(num - 10 + ord('A'));
# # # # # # # # # # # # # # # # # # # def toDeci(str,base):

# # # # # # # # # # # # # # # # # # #   llen = len(str)
# # # # # # # # # # # # # # # # # # #   power = 1
# # # # # # # # # # # # # # # # # # #   num = 0
# # # # # # # # # # # # # # # # # # #   for i in range(llen - 1, -1, -1):
# # # # # # # # # # # # # # # # # # #    num += val(str[i]) * int(power)
# # # # # # # # # # # # # # # # # # #    power = int(power) * base
# # # # # # # # # # # # # # # # # # #   return num
# # # # # # # # # # # # # # # # # # # def fromDeci(res, base, inputNum):
# # # # # # # # # # # # # # # # # # #     index = 0
# # # # # # # # # # # # # # # # # # #     while (inputNum > 0):
# # # # # # # # # # # # # # # # # # #         res+= reVal(inputNum % base)
# # # # # # # # # # # # # # # # # # #         inputNum = int(inputNum / base)
# # # # # # # # # # # # # # # # # # #     res = res[::-1]
# # # # # # # # # # # # # # # # # # #     return res
# # # # # # # # # # # # # # # # # # # a,b=map(str,input().split())
# # # # # # # # # # # # # # # # # # # p,q=map(str,input().split())
# # # # # # # # # # # # # # # # # # # n=int(input())
# # # # # # # # # # # # # # # # # # # dec1=toDeci(a,b)
# # # # # # # # # # # # # # # # # # # dec2=toDeci(p,q)
# # # # # # # # # # # # # # # # # # # dec=dec1*dec2
# # # # # # # # # # # # # # # # # # # res=""
# # # # # # # # # # # # # # # # # # # ans=fromDeci(res,n,dec)
# # # # # # # # # # # # # # # # # # # print(ans)


# # # # # # # # # # # # # # # # # # # Python program to convert infix expression to postfix

# # # # # # # # # # # # # # # # # # # Class to convert the expression


# # # # # # # # # # # # # # # # # # class Conversion:


# # # # # # # # # # # # # # # # # #  def __init__(self, capacity):
# # # # # # # # # # # # # # # # # #   self.top = -1
# # # # # # # # # # # # # # # # # #   self.capacity = capacity
# # # # # # # # # # # # # # # # # #   # This array is used a stack
# # # # # # # # # # # # # # # # # #   self.array = []
# # # # # # # # # # # # # # # # # #   # Precedence setting
# # # # # # # # # # # # # # # # # #   self.output = []
# # # # # # # # # # # # # # # # # #   self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

# # # # # # # # # # # # # # # # # #  # check if the stack is empty
# # # # # # # # # # # # # # # # # #  def isEmpty(self):
# # # # # # # # # # # # # # # # # #   return True if self.top == -1 else False

# # # # # # # # # # # # # # # # # #  # Return the value of the top of the stack
# # # # # # # # # # # # # # # # # #  def peek(self):
# # # # # # # # # # # # # # # # # #   return self.array[-1]

# # # # # # # # # # # # # # # # # #  # Pop the element from the stack
# # # # # # # # # # # # # # # # # #  def pop(self):
# # # # # # # # # # # # # # # # # #   if not self.isEmpty():
# # # # # # # # # # # # # # # # # #    self.top -= 1
# # # # # # # # # # # # # # # # # #    return self.array.pop()
# # # # # # # # # # # # # # # # # #   else:
# # # # # # # # # # # # # # # # # #    return "$"

# # # # # # # # # # # # # # # # # #  # Push the element to the stack
# # # # # # # # # # # # # # # # # #  def push(self, op):
# # # # # # # # # # # # # # # # # #   self.top += 1
# # # # # # # # # # # # # # # # # #   self.array.append(op)

# # # # # # # # # # # # # # # # # #  # A utility function to check is the given character
# # # # # # # # # # # # # # # # # #  # is operand
# # # # # # # # # # # # # # # # # #  def isOperand(self, ch):
# # # # # # # # # # # # # # # # # #   return ch.isalpha()

# # # # # # # # # # # # # # # # # #  # Check if the precedence of operator is strictly
# # # # # # # # # # # # # # # # # #  # less than top of stack or not
# # # # # # # # # # # # # # # # # #  def notGreater(self, i):
# # # # # # # # # # # # # # # # # #   try:
# # # # # # # # # # # # # # # # # #    a = self.precedence[i]
# # # # # # # # # # # # # # # # # #    b = self.precedence[self.peek()]
# # # # # # # # # # # # # # # # # #    return True if a <= b else False
# # # # # # # # # # # # # # # # # #   except KeyError:
# # # # # # # # # # # # # # # # # #    return False

# # # # # # # # # # # # # # # # # #  # The main function that
# # # # # # # # # # # # # # # # # #  # converts given infix expression
# # # # # # # # # # # # # # # # # #  # to postfix expression
# # # # # # # # # # # # # # # # # #  def infixToPostfix(self, exp):

# # # # # # # # # # # # # # # # # #   # Iterate over the expression for conversion
# # # # # # # # # # # # # # # # # #   for i in exp:
# # # # # # # # # # # # # # # # # #    # If the character is an operand,
# # # # # # # # # # # # # # # # # #    # add it to output
# # # # # # # # # # # # # # # # # #    if self.isOperand(i):
# # # # # # # # # # # # # # # # # #     self.output.append(i)

# # # # # # # # # # # # # # # # # #    # If the character is an '(', push it to stack
# # # # # # # # # # # # # # # # # #    elif i == '(':
# # # # # # # # # # # # # # # # # #     self.push(i)

# # # # # # # # # # # # # # # # # #    # If the scanned character is an ')', pop and
# # # # # # # # # # # # # # # # # #    # output from the stack until and '(' is found
# # # # # # # # # # # # # # # # # #    elif i == ')':
# # # # # # # # # # # # # # # # # #     while((not self.isEmpty()) and
# # # # # # # # # # # # # # # # # #      self.peek() != '('):
# # # # # # # # # # # # # # # # # #      a = self.pop()
# # # # # # # # # # # # # # # # # #      self.output.append(a)
# # # # # # # # # # # # # # # # # #     if (not self.isEmpty() and self.peek() != '('):
# # # # # # # # # # # # # # # # # #      return -1
# # # # # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # # # # #      self.pop()

# # # # # # # # # # # # # # # # # #    # An operator is encountered
# # # # # # # # # # # # # # # # # #    else:
# # # # # # # # # # # # # # # # # #     while(not self.isEmpty() and self.notGreater(i)):
# # # # # # # # # # # # # # # # # #       # this is to pass cases like a^b^c
# # # # # # # # # # # # # # # # # #      # without if ab^c^
# # # # # # # # # # # # # # # # # #      # with if abc^^
# # # # # # # # # # # # # # # # # #      if i == "^" and self.array[-1] == i:
# # # # # # # # # # # # # # # # # #       break
# # # # # # # # # # # # # # # # # #      self.output.append(self.pop())
# # # # # # # # # # # # # # # # # #     self.push(i)

# # # # # # # # # # # # # # # # # #   # pop all the operator from the stack
# # # # # # # # # # # # # # # # # #   while not self.isEmpty():
# # # # # # # # # # # # # # # # # #    self.output.append(self.pop())

# # # # # # # # # # # # # # # # # #   print ("".join(self.output))


# # # # # # # # # # # # # # # # # # # Driver's code

# # # # # # # # # # # # # # # # # # exp = input()
# # # # # # # # # # # # # # # # # # obj = Conversion(len(exp))

# # # # # # # # # # # # # # # # # #  # Function call
# # # # # # # # # # # # # # # # # # obj.infixToPostfix(exp)

# # # # # # # # # # # # # # # # # # # This code is contributed by Nikhil Kumar Singh(nickzuck_007)



# # # # # # # # # # # # # # # # # import re
# # # # # # # # # # # # # # # # # PRECEDENCE = {
# # # # # # # # # # # # # # # # #     '^': 4, 
# # # # # # # # # # # # # # # # #     '*': 3,
# # # # # # # # # # # # # # # # #     '/': 3,
# # # # # # # # # # # # # # # # #     '+': 2,
# # # # # # # # # # # # # # # # #     '-': 2,
# # # # # # # # # # # # # # # # #     '(': 1,
# # # # # # # # # # # # # # # # # }
# # # # # # # # # # # # # # # # # def infixToPostfix(expr):
# # # # # # # # # # # # # # # # #     tokens = re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\^\+\*\-\/])", expr)
# # # # # # # # # # # # # # # # #     stack = []
# # # # # # # # # # # # # # # # #     postfix = []    
# # # # # # # # # # # # # # # # #     for token in tokens:6
# # # # # # # # # # # # # # # # #         if token.isalnum():
# # # # # # # # # # # # # # # # #             postfix.append(token)
# # # # # # # # # # # # # # # # #         elif token == '(':
# # # # # # # # # # # # # # # # #             stack.append(token)
# # # # # # # # # # # # # # # # #         elif token == ')':
# # # # # # # # # # # # # # # # #             top = stack.pop()
# # # # # # # # # # # # # # # # #             while top != '(':
# # # # # # # # # # # # # # # # #                 postfix.append(top)
# # # # # # # # # # # # # # # # #                 top = stack.pop()
# # # # # # # # # # # # # # # # #         else:
# # # # # # # # # # # # # # # # #             while stack and (PRECEDENCE[stack[-1]] >= PRECEDENCE[token]):
# # # # # # # # # # # # # # # # #                 postfix.append(stack.pop())
# # # # # # # # # # # # # # # # #             stack.append(token)
# # # # # # # # # # # # # # # # #     while stack:
# # # # # # # # # # # # # # # # #         postfix.append(stack.pop())
# # # # # # # # # # # # # # # # #     return ''.join(postfix)
# # # # # # # # # # # # # # # # # inf=input()
# # # # # # # # # # # # # # # # # print(infixToPostfix(inf))



 

# # # # # # # # # # # # # # # # def infix_to_postfix(expression):
# # # # # # # # # # # # # # # #     stack = [] 
# # # # # # # # # # # # # # # #     output = '' 
# # # # # # # # # # # # # # # #     OPERATORS = set(['+', '-', '*', '/', '(', ')', '^'])
# # # # # # # # # # # # # # # #     PRIORITY = {'+':1, '-':1, '*':2, '/':2, '^':3} 
# # # # # # # # # # # # # # # #     for ch in expression:
# # # # # # # # # # # # # # # #         if ch not in OPERATORS:  
# # # # # # # # # # # # # # # #             output+= ch
# # # # # # # # # # # # # # # #         elif ch=='(': 
# # # # # # # # # # # # # # # #             stack.append('(')
# # # # # # # # # # # # # # # #         elif ch==')':
# # # # # # # # # # # # # # # #             while stack and stack[-1]!= '(':
# # # # # # # # # # # # # # # #                 output+=stack.pop()
# # # # # # # # # # # # # # # #             stack.pop()
# # # # # # # # # # # # # # # #         else:  
# # # # # # # # # # # # # # # #             while stack and stack[-1]!='(' and PRIORITY[ch]<=PRIORITY[stack[-1]]:
# # # # # # # # # # # # # # # #                 output+=stack.pop()
# # # # # # # # # # # # # # # #             stack.append(ch)
# # # # # # # # # # # # # # # #     while stack:
# # # # # # # # # # # # # # # #         output+=stack.pop()
# # # # # # # # # # # # # # # #     return output
# # # # # # # # # # # # # # # # inf=input()
# # # # # # # # # # # # # # # # print(infix_to_postfix(inf))

# # # # # # # # # # # # # # # def allCharactersSame(s) :
# # # # # # # # # # # # # # #     n = len(s)
# # # # # # # # # # # # # # #     for i in range(1, n) :
# # # # # # # # # # # # # # #         if s[i] != s[0] :
# # # # # # # # # # # # # # #             return False
# # # # # # # # # # # # # # #     return True
# # # # # # # # # # # # # # # n=int(input())
# # # # # # # # # # # # # # # l=[]
# # # # # # # # # # # # # # # for i in range(n):
# # # # # # # # # # # # # # #   a=input()
# # # # # # # # # # # # # # #   l.append(a)
# # # # # # # # # # # # # # # count=0
# # # # # # # # # # # # # # # for j in l:
# # # # # # # # # # # # # # #   for i in range(len(j)):
# # # # # # # # # # # # # # #     p=0
# # # # # # # # # # # # # # #     if j[i]!=j[i+1]:
# # # # # # # # # # # # # # #       p=i
# # # # # # # # # # # # # # #       break
# # # # # # # # # # # # # # #     str1=j[0:p]
# # # # # # # # # # # # # # #     if (allCharactersSame(str1)):
# # # # # # # # # # # # # # #       str2=j[p+1:n-1]
# # # # # # # # # # # # # # #       if (allCharactersSame(str2)):
# # # # # # # # # # # # # # #         count+=1
# # # # # # # # # # # # # # # print(count)

# # # # # # # # # # # # # # temp=0
# # # # # # # # # # # # # # for i in range(input1):
# # # # # # # # # # # # # #   for j in range(i+1,input1):
# # # # # # # # # # # # # #     if input3[i]<input3[j]:
# # # # # # # # # # # # # #       temp=input3[i]
# # # # # # # # # # # # # #       input3[i]=input3[j]
# # # # # # # # # # # # # #       input3[j]=temp
# # # # # # # # # # # # # #   if (i+1==input2):
# # # # # # # # # # # # # #     break
# # # # # # # # # # # # # # return imput3[i]



# # # # # # # # # # # # # n=int(input())
# # # # # # # # # # # # # # m=int(input())
# # # # # # # # # # # # # # o=int(input())
# # # # # # # # # # # # # # if n>m and n>o:
# # # # # # # # # # # # # #   print("A")
# # # # # # # # # # # # # # elif m>n and m>o:
# # # # # # # # # # # # # #   print("B")ekj
# # # # # # # # # # # # # # else:
# # # # # # # # # # # # # #   print("C")
# # # # # # # # # # # # # factorial = 1
# # # # # # # # # # # # # if n < 0:
# # # # # # # # # # # # #    print("Sorry, factorial does not exist for negative numbers")
# # # # # # # # # # # # # elif n == 0:
# # # # # # # # # # # # #    print("The factorial of 0 is 1")
# # # # # # # # # # # # # else:
# # # # # # # # # # # # #    for i in range(1,n+1):
# # # # # # # # # # # # #       factorial = factorial*i
# # # # # # # # # # # # #    print("The factorial of",n,"is",factorial)

# # # # # # # # # # # # # n=int(input())
# # # # # # # # # # # # # m=int(input())
# # # # # # # # # # # # # print("Before swapping :",n,m)
# # # # # # # # # # # # # n,m=m,n
# # # # # # # # # # # # # print("After swapping :",n,m)

# # # # # # # # # # # # # a=input()
# # # # # # # # # # # # # s=""
# # # # # # # # # # # # # for i in a :
# # # # # # # # # # # # #   s=s+i
# # # # # # # # # # # # # print(s)


# # # # # # # # # # # # # n=int(input())
# # # # # # # # # # # # # a,b=0,1
# # # # # # # # # # # # # print(a,b,endl="")
# # # # # # # # # # # # # for i in range(2,n+1):
# # # # # # # # # # # # #   print(a+b)
  


# # # # # # # # # # # # keyMatrix = [[0] * 3 for i in range(3)]
# # # # # # # # # # # # messageVector = [[0] for i in range(3)]
# # # # # # # # # # # # cipherMatrix = [[0] for i in range(3)]
# # # # # # # # # # # # def getKeyMatrix(key):
# # # # # # # # # # # #  k = 0
# # # # # # # # # # # #  for i in range(3):
# # # # # # # # # # # #   for j in range(3):
# # # # # # # # # # # #    keyMatrix[i][j] = ord(key[k]) % 65
# # # # # # # # # # # #    k += 1
# # # # # # # # # # # # def encrypt(messageVector):
# # # # # # # # # # # #  for i in range(3):
# # # # # # # # # # # #   for j in range(1):
# # # # # # # # # # # #    cipherMatrix[i][j] = 0
# # # # # # # # # # # #    for x in range(3):
# # # # # # # # # # # #     cipherMatrix[i][j] += (keyMatrix[i][x] *
# # # # # # # # # # # #          messageVector[x][j])
# # # # # # # # # # # #    cipherMatrix[i][j] = cipherMatrix[i][j] % 26
# # # # # # # # # # # # def HillCipher(message, key):
# # # # # # # # # # # #  getKeyMatrix(key)
# # # # # # # # # # # #  for i in range(3):
# # # # # # # # # # # #   messageVector[i][0] = ord(message[i]) % 65
# # # # # # # # # # # #  encrypt(messageVector)
# # # # # # # # # # # #  CipherText = []
# # # # # # # # # # # #  for i in range(3):
# # # # # # # # # # # #   CipherText.append(chr(cipherMatrix[i][0] + 65))
# # # # # # # # # # # #  print("Ciphertext: ", "".join(CipherText))

# # # # # # # # # # # # n=int(input())
# # # # # # # # # # # # message = input("Enter string of given length : ")
# # # # # # # # # # # # key = "GYBNQKURP"
# # # # # # # # # # # # HillCipher(message, key)


# # # # # # # # # # # # alpha = [chr(i) for i in range(97,123)]



# # # # # # # # # # # P = int(input("Public key-1 : "))
# # # # # # # # # # # G = int(input("Public key-2 : "))
# # # # # # # # # # # a = int(input("Private key-1 : "))
# # # # # # # # # # # b = int(input("Private key-1 : "))
# # # # # # # # # # # x = int(pow(G,a,P))
# # # # # # # # # # # y = int(pow(G,b,P))
# # # # # # # # # # # ka = int(pow(y,a,P))
# # # # # # # # # # # kb = int(pow(x,b,P))
# # # # # # # # # # # print('Secret key-1 : ',ka)
# # # # # # # # # # # print('Secret Key-2 : ',kb)


# # # # # # # # # # # Python3 program for the above approach

# # # # # # # # # # # Function to segregate
# # # # # # # # # # def segregate(a, n):
	
# # # # # # # # # # 	i = 0
# # # # # # # # # # 	j = (n - 1)

# # # # # # # # # # 	# Iterate while j >= i
# # # # # # # # # # 	while (j >= i):
	
# # # # # # # # # # 		# Check is a[i] is even
# # # # # # # # # # 		# or odd
# # # # # # # # # # 		if (a[i] % 2 != 0):
# # # # # # # # # # 			if (a[j] % 2 == 0):
				
# # # # # # # # # # 				# Swap a[i] and a[j]
# # # # # # # # # # 				a[i], a[j] = a[j], a[i]
# # # # # # # # # # 				i += 1
# # # # # # # # # # 				j -= 1
			
# # # # # # # # # # 			else:
# # # # # # # # # # 				j -= 1
# # # # # # # # # # 		else:
# # # # # # # # # # 			i += 1;
			
# # # # # # # # # # 	for i in range(n):
# # # # # # # # # # 		print(a[i], end = " ")

# # # # # # # # # # # Driver Code
# # # # # # # # # # a = [ 24,13,68,79,46,77]
# # # # # # # # # # n = len(a)

# # # # # # # # # # segregate(a, n)

# # # # # # # # # # # This code is contributed by rag2127


# # # # # # # # # # Python program to segregate even and odd elements of array

# # # # # # # # # def segregateEvenOdd(arr):

# # # # # # # # # 	# Initialize left and right indexes
# # # # # # # # # 	left,right = 0,len(arr)-1

# # # # # # # # # 	while left < right:

# # # # # # # # # 		# Increment left index while we see 0 at left
# # # # # # # # # 		while (arr[left]%2==0 and left < right):
# # # # # # # # # 			left += 1

# # # # # # # # # 		# Decrement right index while we see 1 at right
# # # # # # # # # 		while (arr[right]%2 == 1 and left < right):
# # # # # # # # # 			right -= 1

# # # # # # # # # 		if (left < right):
# # # # # # # # # 			# Swap arr[left] and arr[right]*/
# # # # # # # # # 			arr[left],arr[right] = arr[right],arr[left]
# # # # # # # # # 			left += 1
# # # # # # # # # 			right = right-1


# # # # # # # # # # Driver function to test above function
# # # # # # # # # arr = [24,13,68,79,46,77]
# # # # # # # # # segregateEvenOdd(arr)
# # # # # # # # # print ("Array after segregation "),
# # # # # # # # # for i in range(0,len(arr)):
# # # # # # # # # 	print (arr[i],)
# # # # # # # # # # This code is contributed by Devesh Agrawal


# # # # # # # # def Solve(N):
# # # # # # # #     res=2**N
# # # # # # # #     return getSum(res)
# # # # # # # # def getSum(numb):
# # # # # # # #     sum=0
# # # # # # # #     while numb>0:
# # # # # # # #         rem=numb%10
# # # # # # # #         sum+=rem
# # # # # # # #         numb=numb//10
# # # # # # # #     if sum>9:
# # # # # # # #         sum=getSum(sum)
# # # # # # # #     return sum
# # # # # # # # n=int(input())
# # # # # # # # N=int(input())
# # # # # # # # print(Solve(N))


# # # # # # # l=list(map(int,input().split()))
# # # # # # # m=[]
# # # # # # # for i in range(len(l)):
# # # # # # #     count=0
# # # # # # #     for j in range(i,len(l)):
# # # # # # #         if l[i]==l[j]:
# # # # # # #             count+=1
# # # # # # #         count1=count
# # # # # # #     if count1>count:
# # # # # # #         m.pop()
# # # # # # #         m.append(count1)
# # # # # # # print(*m)
    

# # # # # # # str=input()
# # # # # # # l=['a','e','i','o','u']
# # # # # # # str.replace(" ","")
# # # # # # # str.lower()
# # # # # # # count=0
# # # # # # # for i in l:
# # # # # # #     if i in str:
# # # # # # #         count+=1
# # # # # # # if count==5:
# # # # # # #     print("Yes")
# # # # # # # else:
# # # # # # #     print("No")


# # # # # # # a=input()
# # # # # # # b=input()
# # # # # # # c=""
# # # # # # # d=""
# # # # # # # for i in a:
# # # # # # #     if i not in c:
# # # # # # #         c=c+i
# # # # # # # for i in b:
# # # # # # #     if i not in d:
# # # # # # #         d=d+i
# # # # # # # count=0
# # # # # # # for i in c:
# # # # # # #     if i in d:
# # # # # # #         count+=1
# # # # # # # print(count)

# # # # # # # a=input()
# # # # # # # l={}
# # # # # # # for i in a:
# # # # # # #     if i in l:
# # # # # # #         l[i]+=1
# # # # # # #     if i  not in l:
# # # # # # #         l[i]=1
# # # # # # # print(l)


# # # # # # # n=input()
# # # # # # # s="!@#$%^&*()_{}[]:;|\<>?/"
# # # # # # # n.split()
# # # # # # # count=0
# # # # # # # for i in n:
# # # # # # #     if i in s:
# # # # # # #         count+=1
# # # # # # # if count==0:
# # # # # # #     print("Yes")
# # # # # # # else:
# # # # # # #     print("No")

# # # # # # from itertools import permutations
# # # # # # str=input()
# # # # # # l=[]
# # # # # # per=permutations(str)
# # # # # # for i in list(per):
# # # # # #     l.append(''.join(i))
# # # # # # print(*l,sep=" ")


# # # # # # Python program to find number of distinct
# # # # # # permutations of a string.

# # # # # MAX_CHAR = 26
# # # # # def factorial(n) :
# # # # # 	fact = 1;
# # # # # 	for i in range(2, n + 1) :
# # # # # 		fact = fact * i;
# # # # # 	return fact
# # # # # def countDistinctPermutations(st) :
# # # # # 	length = len(st)
# # # # # 	freq = [0] * MAX_CHAR
# # # # # 	for i in range(0, length) :
# # # # # 		if (st[i] >= 'a') :
# # # # # 			freq[(ord)(st[i]) - 97] = freq[(ord)(st[i]) - 97] + 1;
# # # # # 	fact = 1
# # # # # 	for i in range(0, MAX_CHAR) :
# # # # # 		fact = fact * factorial(freq[i])
# # # # # 	return factorial(length) // fact
# # # # # st = input()
# # # # # print (countDistinctPermutations(st))


# # # # def max1(arr):
# # # # 	maxi=-1e8
# # # # 	for i in range(len(arr)):
# # # # 		curr=0
# # # # 		for j in range(i,len(arr)):
# # # # 			curr+=arr[j]
# # # # 			if curr>maxi:
# # # # 				maxi=curr
# # # # 	return maxi
# # # # arr=list(map(int,input().split()))
# # # # print(max1(arr))

# # # # Python3 Program to print BFS traversal
# # # # from a given source vertex. BFS(int s)
# # # # traverses vertices reachable from s.
# # # from collections import defaultdict

# # # # This class represents a directed graph
# # # # using adjacency list representation
# # # class Graph:

# # # 	# Constructor
# # # 	def __init__(self):

# # # 		# default dictionary to store graph
# # # 		self.graph = defaultdict(list)

# # # 	# function to add an edge to graph
# # # 	def addEdge(self,u,v):
# # # 		self.graph[u].append(v)

# # # 	# Function to print a BFS of graph
# # # 	def BFS(self, s):

# # # 		# Mark all the vertices as not visited
# # # 		visited = [False] * (len(self.graph))

# # # 		# Create a queue for BFS
# # # 		queue = []

# # # 		# Mark the source node as
# # # 		# visited and enqueue it
# # # 		queue.append(s)
# # # 		visited[s] = True

# # # 		while queue:

# # # 			# Dequeue a vertex from
# # # 			# queue and print it
# # # 			s = queue.pop(0)
# # # 			print (s, end = " ")

# # # 			# Get all adjacent vertices of the
# # # 			# dequeued vertex s. If a adjacent
# # # 			# has not been visited, then mark it
# # # 			# visited and enqueue it
# # # 			for i in self.graph[s]:
# # # 				if visited[i] == False:
# # # 					queue.append(i)
# # # 					visited[i] = True

# # # # Driver code

# # # # Create a graph given in
# # # # the above diagram
# # # g = Graph()
# # # g.addEdge(0, 1)
# # # g.addEdge(0, 2)
# # # g.addEdge(1, 2)
# # # g.addEdge(2, 0)
# # # g.addEdge(2, 3)
# # # g.addEdge(3, 3)

# # # print ("Following is Breadth First Traversal"
# # # 				" (starting from vertex 2)")
# # # g.BFS(2)

# # # # This code is contributed by Neelam Yadav


# # # Python3 program to for tree traversals

# # # A class that represents an individual node in a
# # # Binary Tree


# # class Node:
# # 	def __init__(self, key):
# # 		self.left = None
# # 		self.right = None
# # 		self.val = key


# # # A function to do inorder tree traversal
# # def printInorder(root):

# # 	if root:

# # 		# First recur on left child
# # 		printInorder(root.left)

# # 		# then print the data of node
# # 		print(root.val),

# # 		# now recur on right child
# # 		printInorder(root.right)


# # # Driver code
# # if __name__ == "__main__":
# # 	root = Node(1)
# # 	root.left = Node(2)
# # 	root.right = Node(3)
# # 	root.left.left = Node(4)
# # 	root.left.right = Node(5)

# # 	# Function call
# # 	print ("\nInorder traversal of binary tree is")
# # 	printInorder(root)


# # l=list(map(int,input().split()))
# # n=len(l)
# # result=0
# # for i in range(0,n):
# # 	temp=0
# # 	for j in range(i,n):
# # 		temp+=l[j]
# # 		result+=temp
# # print(result)

# from collections import deque
# n=int(input())
# m=int(input())
# s=input()
# x=list(map(int,input().split()))
# y=list(map(int,input().split()))

# degree=[0 for i in range(n)]
# graph={i:[] for i in range(n)}
# for i in range(m):
# 	x[i]-=1
# 	y[i]-=1
# 	graph[x[i]].append(y[i])
# 	degree[y[i]]+=1
# q=deque()
# for i in range(n):
# 	if degree[i]==0:
# 		q.append(i)
# count=0
# ans=0
# dp=[[0 for i in range(26)]for i in range(n)]
# while count<n and q:
# 	a=q.popleft()
# 	count+=1
# 	dp[a][ord(s[a])-97]+=1
# 	for i in graph[a]:
# 		for j in range(26):
# 			dp[i][j]=max(dp[i][j],dp[a][j])
# 		degree[i]-=1
# 		if degree[i]==0:
# 			q.append(i)
# if count!=n:
# 	print(-1)
# else:
# 	ans=0
# 	for i in range(n):
# 		ans=max(ans,max(dp[i]))
# 	print(ans)



# # maxcount=0
# # for i in range(len(s)):
# # 	count1=0
# # 	for j in range(len(s)):
# # 		if s[i]==s[j]:
# # 			count1+=1
# # 	if count1>maxcount:
# # 		maxcount=count1
# # if maxcount==1:
# # 	print(-1)
# # else:
# # 	print(maxcount)




