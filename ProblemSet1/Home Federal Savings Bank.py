x=input("Greeting:").strip().lower()
if x[:5]=="hello":
    print("$0")
elif x[0]=='h' and x[:5]!="hello":
    print("$20")
else:
    print("$100")

