string=input("Input:")
j=""
for i in string:
    if i in ["A","U","O","I","E","a","e","i","o","u"]:
        j=j+i
        j=j.replace(i,"")

    else:
        j=j+i
print("Output:",j)


