import random

def randInt():
    x = random.random()*100
    return int(x)
x = randInt()
print(x)

def randInt(max):
    x = random.random()*max
    return int(x)
y = randInt(50)
print(y)

def randInt2():
    x = random.random()*50
    x = x+50
    return int(x)
z = randInt2()
print(z)


def randInt3():
    '''
    x = random.random()*50
    y = random.random()*500
    x = x + 50
    y = y + 50
    z = x
    if(y > 50 and y < 500):
        z = y
    return int(z)
    '''
    x = random.random()*450
    x = x + 50
    return int(x)
g = randInt3()
print(g)

