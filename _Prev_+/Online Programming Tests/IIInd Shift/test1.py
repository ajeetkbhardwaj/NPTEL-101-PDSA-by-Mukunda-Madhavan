""" 
Q. Write a function to return maximum value in a list.
Q. Given function code gives incorrect output for some inputs find out?

"""
myinput = ''''''
l = [4, 3, 2, 1]
#########################################################################
def max_num(l):
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

