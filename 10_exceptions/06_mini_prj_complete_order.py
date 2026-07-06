class InvalidChaiError(Exception): pass

def bill(flavour, cups):
    menu = {"masala":28, "ginger":40}
    try:
        if flavour not in menu:
            raise InvalidChaiError(f"Sorry!, {flavour} Chai is not Available.")
        if not isinstance(cups, int):
            raise TypeError("Sorry! Number of cups must be integer.")
        total = menu[flavour] * cups
        print(f"Your bill for {cups} {flavour} chai is ₹{total}")
    except Exception as e:
        print(e)
    finally:
        print("Thank you for visiting! Have a nice day!\n")

bill("masala",4)
# Your bill for 4 masala chai is ₹112
# Thank you for visiting! Have a nice day!


bill("masal",4)
# Sorry!, masal Chai is not Available.
# Thank you for visiting! Have a nice day!

bill("masala","sds")
# Sorry! Number of cups must be integer.
# Thank you for visiting! Have a nice day!