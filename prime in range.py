b=[]
count=0
upper=int(input("enter upper:"))
for a in range(2,upper+1):
    if a>1:
        for i in range(2,a):
            if a%i==0:
                break
        else:
           print(a)
           b.append(a)
           
print(b)
z=len(b)
print("There are",z,"numbers present in your given input" )


            
        
