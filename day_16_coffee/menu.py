class MenuItem:
    def __init__(self, name, cost, water, coffee, milk):
        self.name = name
        self.cost = cost
        self.ingredients = {
            'water': water,
            'coffee': coffee,
            'milk': milk
        }


class Menu:
    def __init__(self) -> None:
        self.menu: list[MenuItem] = [
            MenuItem('espresso', 1.5, 100, 18, 0),
            MenuItem('latte', 2.5, 200, 24, 150),
            MenuItem('cappucino', 3.0, 250, 24, 100)
        ]
        
    def get_item(self):
        options = ""
        for item in self.menu:
            options += str(item.name) + "\n"
        return options

    def find_order(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that order is not avialable")
