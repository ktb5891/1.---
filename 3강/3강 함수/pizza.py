def make_pizza(size, *toppings):
    print("\n Making a "+str(size)+
        "-inch pizza with the topping")
    for topping in toppings:
        print("-" + topping)