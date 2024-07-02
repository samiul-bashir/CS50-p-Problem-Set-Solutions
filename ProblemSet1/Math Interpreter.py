expression=input("Expression")
x,y,z=expression.split(" ") #using .split() to split our string input into 3 chunks and storing them in <x,y,z>
x=float(x) #converting data type to perform arithmetic
z=float(z) #converting data type to perform arithmetic

#The Arithmetic part
if y == '+':
    print(x+z)
elif y == "-":
    print(x-z)
elif y == "*":
    print(x*z)
elif y == "/":
    print(x/z)
else:
    print("invalid input")

