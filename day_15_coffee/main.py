from config import *


def report():
    print()
    print(f"Water: {products['water']}ml")
    print(f"Milk: {products['milk']}ml")
    print(f"Coffee: {products['coffee']}g")
    print(f"Money ${money}")
    print()


def orders():
    print("Espresso")
    print("Latte")
    print("Cappucino")
    order = input("What would you like: ").lower()
    if order in ("espresso", "latte", "cappucino"):
        return order
    elif order == "report":
        report()
    elif order == "exit":
        return False


def calc_coins():
    print('Please insert coins')
    try:
        quarter = int(input('how many  quarters?: '))
        dimes = int(input('how many  dimes?: '))
        nickless = int(input('how many  nickless?: '))
        pennies = int(input('how many  pennies?: '))
    except ValueError:
        print('Please try again')
        calc_coins()
    coin = quarter * 0.25 + dimes * 0.1 + nickless * 0.05 + pennies * 0.01
    return coin


def calc_product(order):
    global money

    for key in MENU[order].keys():
        products[key] -= MENU[order][key]
    print(f"Here is your {order}")
    money += PRICES[order]


def main():
    while True:
        order = orders()
        if order is None:
            continue
        if order == False:
            break
        
        coin = calc_coins()
        if coin < PRICES[order]:
            print("Sorry that's not enough money")
            continue

        if all(products[key] >= MENU[order][key] for key in MENU[order].keys()):
            calc_product(order)
            change = round(coin - PRICES[order], 2)
            print(f"Here is your change {change}")
        else:
            for key in MENU[order].keys():
                if not products[key] >= MENU[order][key]:
                    print(f"Sorry that's not enough {key}")
                    continue


if __name__ == "__main__":
    main()

