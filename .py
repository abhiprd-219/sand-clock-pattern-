def printLine(nums):
    print(space, end='')
    for i in nums:
        print(i,end='', sep='')
    print()
        

MAX = int(input())
space = ""
num = [i for i in range(1,MAX)] + [i for i in range(MAX, 0, -1)]

for i in range(2*MAX):
    if i < MAX:
        printLine(num[i:2*MAX-i-1])
        space += " "
    elif i==MAX:
        space = space[1:]
    elif i> MAX:
        space = space[1:]
        printLine(num[2*MAX-i-1:i])
