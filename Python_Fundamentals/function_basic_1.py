# 1. This should print 5
def a():
    return 5
print(a())     

# 2. This should print 10
def a():
    return 5
print(a()+a())     

# 3. This should print 5
def a():
    return 5
    return 10
print(a())     

# 4. This should print 5 since the return statement will be executed before print(10)
def a():
    return 5
    print(10)
print(a())     

# 5. This should print null since the function has no return statement
def a():
    print(5)
x = a()
print(x)  

# 6. This should give an error since the function has no return statement
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))   

# 7. This should give an error since there is no function called str (prediction)
# Actually returns the string '25' since str(b) converts 2 into a string and str(c) converts 5 to string
# the + concats them together.
def a(b,c):
    return str(b)+str(c)
print(a(2,5))

# 8. Prints 100 then 10
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())  

# 9. Prints 7, 14,21
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

# 10. Returns the addition of b and c and prints it
def a(b,c):
    return b+c
    return 10
print(a(3,5))

# 11. Prints 500 twice then goes into the function and prints 300 then prints 500
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

# 12. Prints 500 twice then goes into the function, prints 300, returns 300 then prints 500 
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)  

# 13. Prints 500 twice then goes into the function, prints 300, returns 300 then prints 300 again
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

# 14. Prints 1, goes into function b and prints 3 then prints 2
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

# 15. Y is a function call to a, function a will print 1, x is a function call to b, b will print 3
# and return 5, x will be assigned 5, 5 will be printed, a will return 10, Y is equal to 10, and 10
# gets printed
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)