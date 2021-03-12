class CoffeeMachine:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.disposable_cups = 9
        self.money = 550

    def remaining(self, action):
        # global water, milk, coffee_beans, disposable_cups, money
        if action == "remaining":
            if self.money == 0:
                print("The coffee machine has:")
                print(str(self.water) + " of water")
                print(str(self.milk) + " of milk")
                print(str(self.coffee_beans) + " of coffee beans")
                print(str(self.disposable_cups) + " of disposable cups")
                print(str(self.money) + " of money")
            else:
                print("The coffee machine has:")
                print(str(self.water) + " of water")
                print(str(self.milk) + " of milk")
                print(str(self.coffee_beans) + " of coffee beans")
                print(str(self.disposable_cups) + " of disposable cups")
                print("$" + str(self.money) + " of money")

    def buy(self, action):
        # global water, milk, coffee_beans, disposable_cups, money
        if action == "buy":
            client = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            if client == "1":
                if self.water - 250 >= 0 and self.coffee_beans - 16 >= 0 and self.disposable_cups - 1 >= 0:
                    print("I have enough resources, making you a coffee!")
                    self.water -= 250
                    self.coffee_beans -= 16
                    self.disposable_cups -= 1
                    self.money += 4
                elif self.water - 250 < 0:
                    print("Sorry, not enough water!")
                elif self.coffee_beans - 16 < 0:
                    print("Sorry, not enough coffee beans!")
                elif self.disposable_cups - 1 < 0:
                    print("Sorry, not enough disposable cups!")
            elif client == "2":
                if self.water - 350 >= 0 and self.milk - 75 >= 0 and self.coffee_beans - 20 >= 0\
                        and self.disposable_cups - 1 >= 0:
                    print("I have enough resources, making you a coffee!")
                    self.water -= 350
                    self.milk -= 75
                    self.coffee_beans -= 20
                    self.disposable_cups -= 1
                    self.money += 7
                elif self.water - 350 < 0:
                    print("Sorry, not enough water!")
                elif self.milk - 75 < 0:
                    print("Sorry, not enough milk!")
                elif self.coffee_beans - 20 < 0:
                    print("Sorry, not enough coffee beans!")
                elif self.disposable_cups - 1 < 0:
                    print("Sorry, not enough disposable cups!")
            elif client == "3":
                if self.water - 200 >= 0 and self.milk - 100 >= 0 and self.coffee_beans - 12 >= 0\
                        and self.disposable_cups - 1 >= 0:
                    print("I have enough resources, making you a coffee!")
                    self.water -= 200
                    self.milk -= 100
                    self.coffee_beans -= 12
                    self.disposable_cups -= 1
                    self.money += 6
                elif self.water - 200 < 0:
                    print("Sorry, not enough water!")
                elif self.milk - 100 < 0:
                    print("Sorry, not enough milk!")
                elif self.coffee_beans - 12 < 0:
                    print("Sorry, not enough coffee beans!")
                elif self.disposable_cups - 1 < 0:
                    print("Sorry, not enough disposable cups!")

    def fill(self, action):
        # global water, milk, coffee_beans, disposable_cups, money
        if action == "fill":
            # print("The coffee machine has:")
            # print(str(water) + " of water")
            # print(str(milk) + " of milk")
            # print(str(coffee_beans) + " of coffee beans")
            # print(str(disposable_cups) + " of disposable cups")
            # print(str(money) + " of money")
            self.water += int(input("Write how many ml of water do you want to add:"))
            self.milk += int(input("Write how many ml of milk do you want to add:"))
            self.coffee_beans += int(input("Write how many grams of coffee beans do you want to add:"))
            self.disposable_cups += int(input("Write how many disposable cups of coffee do you want to add:"))
            # print("The coffee machine has:")
            #         # print(str(water) + " of water")
            #         # print(str(milk) + " of milk")
            #         # print(str(coffee_beans) + " of coffee beans")
            #         # print(str(disposable_cups) + " of disposable cups")
            #         # print(str(money) + " of money")

    def take(self, action):
        # global water, milk, coffee_beans, disposable_cups, money
        if action == "take":
            # print("The coffee machine has:")
            # print(str(water) + " of water")
            # print(str(milk) + " of milk")
            # print(str(coffee_beans) + " of coffee beans")
            # print(str(disposable_cups) + " of disposable cups")
            # print(str(money) + " of money")
            print("I gave you $" + str(self.money))
            self.money -= self.money

    def make_transaction(self):
        action = input()
        self.buy(action)
        self.fill(action)
        self.take(action)
        self.remaining(action)


# while True:
#     client_transaction = input()
#     if client_transaction == "exit":
#         break
#     make_transaction(client_transaction)
my_coffee_machine = CoffeeMachine()
my_coffee_machine.make_transaction()

