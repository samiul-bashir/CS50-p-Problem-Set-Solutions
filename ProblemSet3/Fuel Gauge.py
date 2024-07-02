def main():
    x=fraction("Fraction:")
    print(x)

def fraction(prompt):
    while True:
        try:
            neu,deno=input(prompt).split("/")
            value=((int(neu)/int(deno))*100)
            if value<=1:
                return "E"
            elif 90<= value<=100:
                return "F"
            elif value>100:                                              #use <pass> instead of <break> since break tends to return <"none">
                pass
            else:
                return str(int(round(value)))+"%"
        except ZeroDivisionError:
            pass
        except ValueError:
            pass
main()
