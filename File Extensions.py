def main():
    x=input("File name:").lower().strip()
    check_extensions(x) #calling a function named "check_extensions" what will check for our extensions

#defining 'check_extensions'
def check_extensions(s):
    dict={                #defining a dictionary here that contains all our required extensions
        ".gif":"image/gif",
        ".jpg":"image/jpeg",
        ".jpeg":"image/jpeg",
        ".png":"image/png",
        ".pdf":"application/pdf",
        ".txt":"text/plain",
        ".zip":"application/zip"
        }
    f1=s[-4:]        #storing the last 4 letters of input string in f1
    f2=s[-5:]        #storing the last 5 letters of input string in f2
    if f1 in dict:
        print(dict[f1])
    elif f2 in dict:
        print(dict[f2])
    else:
        print("application/octet-stream")

main()

