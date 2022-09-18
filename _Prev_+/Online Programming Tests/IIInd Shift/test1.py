""" 
Q. Write a function to return maximum value in a list.
Q. Given function code gives incorrect output for some inputs find out?

"""
myinput = [4, 3, 2, 1]
#########################################################################
def max_bad(l):
    max = [-1]
    for i in range(-1, -len(l), -1):
        if l[i] > max:
            max = l[i]
        return(max)
    
########################################################################
import ast

try:
    myarg = ast.literal_eval(myinput.strip())
except:
    print(False)
else:
    try:
        print(max(myarg) != max(myarg))
    except:
        print(False)


q7

# emplty list declaration for appending lines
lines = []
# Input lines as text
line = input()

while(line):
  lines.append(line)
  line = input()

for i in range(0,len(lines),2):
  print(lines[i])
for i in range(1,len(lines),2):
  print(lines[i])


q6
q8 

def aboveaverage(l):
  aggregate = {}
  innings = {}
  totalscore = 0
  totalinnings = 0
  for (name,score) in l:
    totalscore += score
    totalinnings += 1
    try:
      aggregate[name] += score
      innings[name] += 1
    except KeyError:
      aggregate[name] = score
      innings[name] = 1

  overallaverage = totalscore/totalinnings

  aboveaverage = []
    
  for name in aggregate.keys():
    average = aggregate[name]/innings[name]
    if average >= overallaverage: 
      aboveaverage.append(name)
      
  return(sorted(aboveaverage))

q1
[-1,-2,-4,-5,-5]
q2 
[1,1,2,2,3,3]
q3
  if x >= y and x <= z:
       mymedian = x
  if y <= x and y >= z:
        mymedian = y
  if y >= x and y <= z:
        mymedian = y
  if z <= x and z >= y:
        mymedian = z
  if z >= x and z <= y:
        mymedian = z
q4
            l[0] > l[1] and decreasing(l[1:])
q5

# cube function

def cube(n):
    for i in range(1,n+1):
        if n == i**3:
            return(True)
    return(False)
# sum of cubes
def sum3cubes(n):
    for i in range(1,n-1):
        for j in range (1,n-i):
            k = n - (i+j)
            if cube(i) and cube(j) and cube(k):
                return(True)
    return(False)