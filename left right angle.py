height=int(input("Enter height of a left right angle triangle: "))
for i in range(0,height+1):
    for j in range(0,height+1):
        print(' ',end='')
    height=height-1
    print('*'*i)