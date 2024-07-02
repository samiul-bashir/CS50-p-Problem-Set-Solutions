def main():


    due=50                                 #Intialisation 
    while due>0:
        print("Amount Due:",due)           #Printing the Due amount
        insert=int(input("Insert Coin"))   #Taking user input
        inside=inserted_coin(insert)       #calling a function called "inserted_coin"
        due = due - inside
    if due<0:
         print("Change Owed:",abs(due))  #for when inserted amount is more than 50 (abs() is used to convert the negative value into positive )
    else:
         print("Change Owed:",due)       #when inserted amount is exact



def inserted_coin(n):                    # defining function inserted_coin
    list=[5,10,25]                       # Allowed Coins only
    init=0
    if n in list:
        init = init+ n                  #updating init
        return init
    else:
        return 0                        #adds zero if invalid coin is inserted


main()                                 #function call
