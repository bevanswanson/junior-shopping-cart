PRICE_LIST = {
    'apple': 1,
    'banana': 2,
    'pak choi': 2,
    'snake oil': 5 
}


def greet(name):
    return f'Hello, {name}!'


def add_to_cart(item, cart):
    cart.append(item)
    return f'Adding {item} to cart.'


def view_stock():
    pass


def view_cart():
    pass


def calculate_total():
    pass


def main():
    print('Welcome to the Python Shop!')

    cart = []
    user = input('What is your name? ')

    print(greet(user))

    while True:
        command = input('What would you like to buy? \n  --If you want to view the options, type "help".\n')
        if command == 'help':
            print('Type "add <item>" to add an item to your cart.')
            print('Type "cart" to view your cart.')
            print('Type "checkout" to checkout.')
            print('Type "exit" to exit.')
        elif command.startswith('add'):
            item = command.split(' ')[1]
            print(add_to_cart(item, cart))
        elif command == 'cart':
            view_cart()
        elif command == 'checkout':
            calculate_total()
            break
        elif command == 'exit':
            break
        else:
            print('Sorry, that is not a valid command.')

    print('Thank you for shopping with us!')

if __name__ == '__main__':
    main()
