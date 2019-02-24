# Problem 1
for x in range(151):
    print (x)


# Problem 2
for y in range(5,100,5):
    print(y)


# Problem 3
for z in range(1,100):
    if(z % 10 == 0):
        print("codingdojo")
    elif(z%5 == 0):
        print("coding")
    else:
        print(z)

# Problem 4
sum = 0
for a in range(0,500000):
    if(a % 2 == 1):
        sum = sum + a
print(sum)

# Problem 5 
for b in range(2018,1,-4):
    print(b)

# Problem 6
lowNum = 2
highNum = 9
mult = 3
for c in range(lowNum,highNum + 1):
    if(c%mult == 0):
        print (c)

