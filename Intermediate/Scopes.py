var = 2


def mult_by_var(x):
    return x * var


print(mult_by_var(7))    # outputs: 14

#Example 2

def mult(x):
    var = 5
    return x * var


print(mult(7))    # outputs: 35

#Example 3

def mult(x):
    var = 7
    return x * var


var = 3
print(mult(7))    # outputs: 49

#Example 4

def adding(x):
    var = 7
    return x + var


print(adding(4))    # outputs: 11
print(var)    # NameError

#Example 5

var = 2
print(var)    # outputs: 2


def return_var():
    global var
    var = 5
    return var


print(return_var())    # outputs: 5
print(var)    # outputs: 5

