db = open("output.txt", "a")

class Beverage:
    def __init__(self, price):
        self.price = price

coke = Beverage(2.50)
monster = Beverage(3.00)
gatorade = Beverage(2.50)
sprite = Beverage(2.00)
rootBeer = Beverage(1.25)
water = Beverage(1.75)

class VendingMachine:
    selection = "1) Coca Cola, 2) Monster, 3) Gatorade, 4) Sprite, 5) Root Beer, 6) Water"

print(VendingMachine.selection)
item = float(input("Please select an item by number "))
if item == 1:
    print("Please insert $", coke.price)
    money = float(input("$"))
    if money == coke.price:
        print("Coke vended")
    elif money < coke.price:
        print("Not enough money, payment was $", coke.price - money, "short")
    elif money > coke.price:
        print("Coke vended")
        print("Your change is $", money - coke.price)

elif item == 2:
    print("Please insert $", monster.price)
    money = float(input("$"))
    if money == monster.price:
        print("Monster vended")
    elif money < monster.price:
        print("Not enough money, payment was $", monster.price - money, "short")
    elif money > monster.price:
        print("Monster vended")
        print("Your change is $", money - monster.price)

elif item == 3:
    print("Please insert $", gatorade.price)
    money = float(input("$"))
    if money == gatorade.price:
        print("Gatorade vended")
    elif money < gatorade.price:
        print("Not enough money, payment was $", gatorade.price - money, "short")
    elif money > gatorade.price:
        print("Gatorade vended")
        print("Your change is $", money - gatorade.price)

elif item == 4:
    print("Please insert $", sprite.price)
    money = float(input("$"))
    if money == sprite.price:
        print("Sprite vended")
    elif money < sprite.price:
        print("Not enough money, payment was $", sprite.price - money, "short")
    elif money > sprite.price:
        print("Sprite vended")
        print("Your change is $", money - sprite.price)

elif item == 5:
    print("Please insert $", rootBeer.price)
    money = float(input("$"))
    if money == rootBeer.price:
        print("Root Beer vended")
    elif money < rootBeer.price:
        print("Not enough money, payment was $", rootBeer.price - money, "short")
    elif money > rootBeer.price:
        print("Root Beer vended")
        print("Your change is $", money - rootBeer.price)

elif item == 6:
    print("Please insert $", water.price)
    money = float(input("$"))
    if money == water.price:
        print("Water vended")
    elif money < water.price:
        print("Not enough money, payment was $", water.price - money, "short")
    elif money > water.price:
        print("Water vended")
        print("Your change is $", money - water.price)

while item > -1:
    print(VendingMachine.selection)
    item = float(input("Please select an item by number "))
    if item == 1:
        print("Please insert $", coke.price)
        money = float(input("$"))
        if money == coke.price:
            print("Coke vended")
        elif money < coke.price:
            print("Not enough money, payment was $", coke.price - money, "short")
        elif money > coke.price:
            print("Coke vended")
            print("Your change is $", money - coke.price)

    elif item == 2:
        print("Please insert $", monster.price)
        money = float(input("$"))
        if money == monster.price:
            print("Monster vended")
        elif money < monster.price:
            print("Not enough money, payment was $", monster.price - money, "short")
        elif money > monster.price:
            print("Monster vended")
            print("Your change is $", money - monster.price)

    elif item == 3:
        print("Please insert $", gatorade.price)
        money = float(input("$"))
        if money == gatorade.price:
            print("Gatorade vended")
        elif money < gatorade.price:
            print("Not enough money, payment was $", gatorade.price - money, "short")
        elif money > gatorade.price:
            print("Gatorade vended")
            print("Your change is $", money - gatorade.price)

    elif item == 4:
        print("Please insert $", sprite.price)
        money = float(input("$"))
        if money == sprite.price:
            print("Sprite vended")
        elif money < sprite.price:
            print("Not enough money, payment was $", sprite.price - money, "short")
        elif money > sprite.price:
            print("Sprite vended")
            print("Your change is $", money - sprite.price)

    elif item == 5:
        print("Please insert $", rootBeer.price)
        money = float(input("$"))
        if money == rootBeer.price:
            print("Root Beer vended")
        elif money < rootBeer.price:
            print("Not enough money, payment was $", rootBeer.price - money, "short")
        elif money > rootBeer.price:
            print("Root Beer vended")
            print("Your change is $", money - rootBeer.price)

    elif item == 6:
        print("Please insert $", water.price)
        money = float(input("$"))
        if money == water.price:
            print("Water vended")
        elif money < water.price:
            print("Not enough money, payment was $", water.price - money, "short")
        elif money > water.price:
            print("Water vended")
            print("Your change is $", money - water.price)
