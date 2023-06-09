from datetime import date


def initial_display():
    display = '''      Sunway International Billing system
                 Maitidevi, Kathmandu
*----------*----------*----------*----------*----------*
                '''
    print(display)


def input_information():
    name = (input("Enter the name of the customer : "))
    address = (input("Enter the address of the customer : "))
    unit = int(input("Enter the units consumed by the customer : "))
    return name, address, unit


def calculation_units(unit):
    global amount, total, discount
    if unit <= 100:
        print("no charge for first 100 units")
    elif 101 <= unit <= 200:
        amount = (unit - 100) * 5
        total = amount
        discount = 0
    elif 201 <= unit <= 500:
        amount = 500 + ((unit - 300) * 10)
        total = amount
        discount = 0
    elif unit > 500:
        amount = 500 + 3000 + ((unit - 500) * 15)
        discount = 0.1 * unit
        total = amount - discount
    else:
        print("Thank you")
    return amount, total, discount


def output():
    print("Name          : ", name)
    print("Address       : ", address)
    print("Amount        : ", amount)
    print("Discount      : ", discount)
    print("Total amount  : ", total)


initial_display()
name, address, unit = input_information()
amount, total, discount = calculation_units(unit)
output()