from textwrap import dedent

orders = {
    "Wings":0,
    "Cookies":0,
    "Spring Rolls":0,
    "Salmon":0,
    "Steak":0,
    "Meat Tornado":0,
    "A Literal Garden":0,
    "Ice Cream":0,
    "Cake":0,
    "Pie":0,
    "Coffee": 0,
    "Tea":0,
    "Unicorn Tear":0,
}

def welcome_customer():
    welcome = """
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************
    """
    welcome_formatted = dedent(welcome)
    return welcome_formatted    

def menu():
    menu = """
    Appetizers
    ----------
    {}
    {}
    {}
    Entrees
    -------
    {}
    {}
    {}
    {}
    Desserts
    --------
    {}
    {}
    {}
    Drinks
    ------
    {}
    {}
    {}
    """.format(*orders)
    return dedent(menu)

def get_order():
    item = """
    ***********************************
    ** What would you like to order? **
    ***********************************
    """

    while True:
        order = input(dedent(item)).title()
        if order == "Quit":
            break

        if order not in orders:
            print(f"Sorry we dont serve {order}")
        else:
            orders[order] = orders[order]+1
            print(f"**{orders[order]} order(s) of {order} have been added to your meal**")
    
    print("Thanks for visting   !")
    return orders

def main():
    print(welcome_customer())
    print(menu())
    orders = get_order()

if __name__ == "__main__":
    main()