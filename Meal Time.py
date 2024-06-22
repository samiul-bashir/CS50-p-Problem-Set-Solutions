def main():
    x=input("What time is it?")
    t= convert(x)
    if t>=7 and t<=8:
        print("breakfast time")
    elif t>=12 and t<=13:
        print("lunch time")
    elif t>18 and t<19:
        print("dinner time")



def convert(time):
    hr,min=time.split(":") #separating the time into hours and minutes and storing them in 'hr' and 'min' respectively
    hr=float(hr)
    min=float(min)
    min=(min/60)      #coverting the minute format into decimal hour
    return hr + min

    ###


if __name__ == "__main__":
    main()
