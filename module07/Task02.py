def convertor(value):
    liter = 3.78541
    return value * liter

while True:
    quantity_Gasoline = int(input("enter the quantity of gasoline:"))
    if quantity_Gasoline < 0:
        print("You entered negative number.")
        break
    else:
        result = convertor(quantity_Gasoline)
        print(f"{quantity_Gasoline} gallons is equal to {result} liters.")
