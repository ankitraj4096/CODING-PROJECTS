MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


total_quantity = {"Water":300,"Milk":200,"Coffee":100,"Money":0}
def report():
    print(f"Water: {total_quantity["Water"]}ml")
    print(f"Milk: {total_quantity["Milk"]}ml")
    print(f"Coffee: {total_quantity["Coffee"]}g")
    print(f"Money: ${total_quantity["Money"]}")



def coin_taker():
    blank = []
    a = int(input("how many quarters?: "))
    b = int(input("how many dimes?: "))
    c = int(input("how many nickles?: "))
    d = int(input("how many pennies?: "))
    blank.append(a)
    blank.append(b)
    blank.append(c)
    blank.append(d)



    return blank  
def amount_calculator(x):
    money = x[0]*(0.25) + x[1]*(0.1) + x[2]*(0.05) + x[3]*(0.01)
    return money   



def checker(a):
    if a == "espresso":
        if MENU[a]['ingredients']["water"] > total_quantity["Water"] or  MENU[a]['ingredients']["coffee"] > total_quantity["Coffee"]:
            return 0
        else:
            return 1
    elif MENU[a]['ingredients']["water"] > total_quantity["Water"] or MENU[a]['ingredients']["milk"] > total_quantity["Milk"] or MENU[a]['ingredients']["coffee"] > total_quantity["Coffee"]:
        return 0
    else:
        return 1
    


def money_transc():
    humm = coin_taker()
    bill = amount_calculator(humm)
    return bill


def money_sufficient(bill,string):
    if bill > MENU[string]["cost"]:
        remaining = bill - MENU[string]["cost"]
        remaining = round(remaining,2)
        return remaining
    else:
        print("Sorry that's not enough money. Money refunded.")
        return 0
    

def update(a):
    if a != "espresso":
        total_quantity["Water"] -= MENU[a]['ingredients']["water"]
        total_quantity["Milk"] -= MENU[a]['ingredients']["milk"]
        total_quantity["Coffee"] -= MENU[a]['ingredients']["coffee"]
        total_quantity["Money"] += MENU[a]['cost']
    else:
        total_quantity["Water"] -= MENU[a]['ingredients']["water"]
        total_quantity["Coffee"] -= MENU[a]['ingredients']["coffee"]
        total_quantity["Money"] += MENU[a]['cost']


should_continue = True

options = ["cappuccino","espresso","latte"]


while should_continue:
    question = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if question == "report":
        report()
    elif question in options:
        value = checker(question)
        if value == 0:
            print("Sorry there is not enough ")
            should_continue = False
        else:
            bill = money_transc()
            xmas = money_sufficient(bill,question)
            if xmas != 0:
                update(question)
                print(f"Here is your ${xmas} in change.")
                print(f"Here is your {question}☕.Enjoy!")
    else:
        print("Input sahi de bhai")
