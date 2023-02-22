class MoneyMachine:
    CURRENCY = "$"
    
    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }
    
    def __init__(self) -> None:
        self.money = 0
        self.recieved = 0
    
    def report(self):
        print(f"Money: {self.CURRENCY}{self.money}")

    def coin_proces(self):
        print("Please insert coins")
        for key in self.COIN_VALUES.keys():
            self.recieved += int(input(f"How many {key}: ")) * self.COIN_VALUES[key]
        return self.recieved

    def make_payment(self, cost: float):
        self.coin_proces()
        if self.recieved >= cost:
            change = round(self.recieved - cost, 2)
            print(f"Here is your change {self.CURRENCY}{change}")
            self.money += cost
            self.recieved = 0
            return True
        else:
            print("Please That's not enough money")
            return False

