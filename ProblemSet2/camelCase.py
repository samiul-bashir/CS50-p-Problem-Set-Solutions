string=input("CamelCase:")
x=string               #Transfering user input into a different variable to operate on
j=""                   #creating a empty string
char_num=int(len(x))
for i in x:
    if x[0].isupper(): #condition so that we don't add "_" before the first letter if it was uppercase
        j=j+i
    elif i.isupper():
        j=j+"_"+i
    else:
        j=j+i
    e=j.lower().strip() #storing 'j' in 'e' and removing any empty spaces and making them all lower case
print("snake_case:",e)
