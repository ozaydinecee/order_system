menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee', 
        "price": 2.50},
    3: {"name": 'cake', 
        "price": 2.79},
    4: {"name": 'soup', 
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99}
}

def calculate_subtotal(order):
    
    print('Calculating bill subtotal...')
    
    items = []
    items = [item["price"] for item in order]
    
    
    subtotal=0.0
    for i in items:
        subtotal+=i

    subtotal=round(subtotal,2)
    return subtotal


def calculate_tax(subtotal):
    
    print('Calculating tax from subtotal...')
    tax=(subtotal*0.15)
    tax = round(tax, 2)
    return tax
    

def summarize_order(order,subtotal,tax):
    
    #print_order(order)
    names=[]
    names = [name["name"] for name in order]

    total=subtotal+tax
    total=round(total,2)

    return names,total

# This function is provided for you, and will print out the items in an order
def print_order(order):
    print('You have ordered ' + str(len(order)) + ' items')
    items = []
    items = [item["name"] for item in order]
    print(items)
    print(order)
    return order

# This function is provided for you, and will display the menu
def display_menu():
    print("------- Menu -------")
    for selection in menu:
        print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")
    print()

# This function is provided for you, and will create an order by prompting the user to select menu items
def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input('Select menu item number ' + str(count) + ' (from 1 to 5): ')
        count += 1
        order.append(menu[int(item)])
    return order


def main():
    order = take_order()
    print_order(order)

    subtotal = calculate_subtotal(order)
    print("Subtotal for the order is: " + str(subtotal))

    tax = calculate_tax(subtotal)
    print("Tax for the order is: " + str(tax))

    names,total = summarize_order(order,subtotal,tax)
    print("Total for the order is: " + str(total))
    print("Ordered items names are: " + str(names))

    

if __name__ == "__main__":
    main()
