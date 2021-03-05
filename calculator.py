print("-------------------calculator---------------------")
print("Select operation.")
print("1.Add")
print("2.Multiply")
print("3.Subtract")
print("4.Divide")
ch=int(input("enter your choice"))
if ch==1:
         a=int(input("Enter first number"))
         b=int(input("Enter second number"))
         c=a+b
         print("sum",c)
elif ch==2:
      
      a=int(input("Enter first number"))
      b=int(input("Enter second number"))
      c=a*b
      print("mul",c)
elif ch==3:
	
     a=int(input("Enter first number"))
     b=int(input("Enter second number"))
     c=a-b
     print("sub",c)
elif ch==4:
     a=int(input("Enter first number"))
     b=int(input("Enter second number"))
     c=a/b
     print("div",c)
