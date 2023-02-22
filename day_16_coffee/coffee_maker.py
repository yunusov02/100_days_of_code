from menu import MenuItem


class CoffeeMaker:
    def __init__(self):
        self.ingredients = {
            'water': 300,
            'milk': 200,
            'coffee': 100
        }
        

    def report(self):
        print()
        print(f"Water: {self.ingredients['water']}ml")
        print(f"Milk: {self.ingredients['milk']}ml")
        print(f"Coffee: {self.ingredients['coffee']}g")
        print()

    def is_resource_sufficient(self, drink: MenuItem):
        for key in self.ingredients.keys():
            if drink.ingredients[key] > self.ingredients[key]:
                print("Sorry that's not enough ingredients")
                return False
        return True


    def make_coffee(self, order: MenuItem):
        for key in self.ingredients.keys():
            self.ingredients[key] -= order.ingredients[key]         
        print(f"Here is your {order.name}. Enjoy")





