def main():
    menu={
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    price=0
    while True:
        try:
            key=input("Item:").strip().title()
            if key in menu:
                #price=0             #> we can't set the price to 0 inside the loop as this will set value of price=0 after every run and won't update
                price=price + menu[key]

                print(f"${price:.2f}")
                continue
            else:
                continue

        except EOFError:
            break
        except KeyError:
            continue

main()
