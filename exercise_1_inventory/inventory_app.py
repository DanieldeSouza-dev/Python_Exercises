# functions and menu

dict_products = {
    'iphone': 5000,
    'ipad': 7000,
    'airpods': 1500
}


def bar():
    print('-=' * 12)


# menu

bar()
print('Welcome to Inventory 1.0!')
bar()

while True:
    keys = dict_products.keys()
    validation = str(input('Customer [C]\nStaff [S]\nExit [E]\n: ')).lower()
    if validation == 'e':
        print('Thanks for using Inventory 1.0. See you next time!')
        break  # end the program
    elif validation == 'c':
        while True:
            print(keys)
            customer = str(input('Enter the product name to check its price: '))
            if customer in dict_products:
                print(f'O valor do {customer} ', end='')
                print(dict_products[customer])
                view_again = str(input('Would you like to check another product? [y/n]: ')).lower()
                if view_again != 'y':
                    break  # exits the costumer loop and go back to menu
            else:
                print('Product not found! Please try again.')
    elif validation == 's':
        while True:
            new_product = str(input('Enter the product name: '))
            new_price = int(input('Enter its price: '))
            dict_products[new_product] = new_price
            print('Product successfully added!\n')
            view_again = str(input('Would you like to add another product? [y/n]: ')).lower()
            if view_again != 'y':
                print(dict_products)
                break  # exits the staff loop and go back to menu