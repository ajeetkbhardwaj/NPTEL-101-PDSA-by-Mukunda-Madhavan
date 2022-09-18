q1
myinput='''
[4,3,2,1]
'''

def minbad(l):
  mymin = l[-len(l)]
  for i in range(-len(l),-1):
    if l[i] < mymin:
       mymin = l[i]
  return(mymin)

import ast

try:
   myarg =  ast.literal_eval(myinput.strip())
except:
   print(False)
else:
  try:
     print(minbad(myarg) != min(myarg))
  except:
     print(False)
q2

myinput = '''
[(2,3),(5,4),(3,4),(0,1)]
'''

def stablesortbad(l):
  for j in range(len(l)-1):
    for i in range(len(l)-1):
      if l[i][1] >= l[i+1][1]:
        (l[i],l[i+1]) =  (l[i+1],l[i])
  return(l)    
    
def stablesortgood(l):
  for j in range(len(l)-1):
    for i in range(len(l)-1):
      if l[i][1] > l[i+1][1]:
        (l[i],l[i+1]) =  (l[i+1],l[i])
  return(l)    
    
import ast

try:
   myarg =  ast.literal_eval(myinput.strip())
except:
   print(False)
else:
  try:
     print(stablesortbad(myarg[:]) != stablesortgood(myarg[:]))
  except:
     print(False)
     
     
     q3
     
def thirdmax(l):
  (mymax,mysecondmax,mythirdmax) = (0,0,0)
  for i in range(len(l)):
  # Your code below this line

    if l[i] > mymax:
      (mymax,mysecondmax,mythirdmax) = (l[i],mymax,mysecondmax)
    elif l[i] > mysecondmax:
      (mysecondmax,mythirdmax) = (l[i],mysecondmax)
    elif l[i] > mythirdmax:
      mythirdmax = l[i]

  # Your code above this line
  return(mythirdmax)
import ast

def tolist(inp):
  inp = ast.literal_eval(inp)
  return(inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "thirdmax":
  arg = tolist(farg)
  print(thirdmax(arg))
  
  
quit

def mod3pos(l):
  if len(l) == 0:
    return([])
  else:
    return(
       # Complete the recursive call below this line
        [l[0]] + mod3pos(l[3:])
       # Complete the recursive call above this line
    )

import ast

def tolist(inp):
  inp = ast.literal_eval(inp)
  return(inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "mod3pos":
  arg = tolist(farg)
  print(mod3pos(arg))
  
  quit
  
import math
def squarefree(n):
  for i in range(2,1+math.ceil(math.sqrt(n))):
    if n%(i*i) == 0:
      return(False)
  return(True)
import ast

def toint(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "squarefree":
  arg = toint(farg)
  print(squarefree(arg))
  
  q6

def disjointlist(l1,l2):
  s1 = set(l1)
  s2 = set(l2)
  return(s1 & s2 == set())
import ast

def topairoflists(inp):
  inp = "["+inp+"]"
  inp = ast.literal_eval(inp)
  return (inp[0],inp[1])

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "disjointlist":
  (arg1,arg2) = topairoflists(farg)
  print(disjointlist(arg1,arg2))
  
  
q7

 inputlines = []
inputline = input()
while(inputline):
  inputlines.append(inputline)
  inputline = input()

n = len(inputlines)//2
for i in range(n,len(inputlines)):
  print(inputlines[i])
for i in range(n):
  print(inputlines[i]) 
  
  
  q8
def maxdifference(l):
  maximum = {}
  minimum = {}
  for (name,score) in l:
    try:
      maximum[name] = max(maximum[name],score)
      minimum[name] = min(minimum[name],score)
    except KeyError:
      maximum[name] = score
      minimum[name] = score
      
  maxdiff = -1
  maxlist = []

  for name in maximum.keys():
    thisdiff = maximum[name] - minimum[name]
    if thisdiff == maxdiff:
      maxlist.append(name)
    if thisdiff > maxdiff:
      maxdiff = thisdiff
      maxlist = [name]
      
  return(sorted(maxlist))

import ast

def tolist(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "maxdifference":
  arg = tolist(farg)
  print(maxdifference(arg))

