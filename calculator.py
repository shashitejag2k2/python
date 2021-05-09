a=int(input("Enter A:"))
b=int(input("Enter B:"))
ops_list=['-','+','*','/','**','//','%']
choice=input("['+','-','*','/','**','//','%']\nEnter your choice\n")

if '+' in ops_list:
    print("ADDITION OF",a,"&",b,"is",a+b)
elif choice=='-':
    if '-' in ops_list:
     print("subtraction OF",a,"&",b,"is",a-b)   
elif choice=='*':
    if '*' in ops_list:
     print("multiplication OF",a,"&",b,"is",a*b)
elif choice=='/':
    if '/' in ops_list:
     print("DIVISION OF",a,"&",b,"is",a/b)
elif choice=='**':
    if '**' in ops_list:
     print("POWER OF",a,"&",b,"is",a**b)
elif choice=='%':
    if '**' in ops_list:
     print("MODULUS OF",a,"&",b,"is",a%b)
elif choice=='//':
    if '//' in ops_list:
     print("FLOOR OF",a,"&",b,"is",a//b)
else:
    print("INVALID INPUT")
    
    