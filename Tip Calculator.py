def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    e =d.strip("$") #removing the $ sign
    f=float(e)      #Converting to float
    return f        # returning the value to <dollars>
    


def percent_to_float(p):
    n=p.strip("%")  #removing the % sign
    m=float(n)      #Converting to float
    return m*0.01   #returning the value of m to <percent>


main()
