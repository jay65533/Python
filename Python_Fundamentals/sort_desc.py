num = [-3,1,-2,6,10,-1]

num.sort(reverse = True)
for i in range(len(num)):
    if(num[len(num)-1] < 0):
        num.pop()
num.sort()
print(num)