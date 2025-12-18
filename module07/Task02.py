def convert_to_liters(gallons):
    liters = gallons * 3.78541
    return liters
def main():
    print("gallons to liters converter or enter negative number to quit")

    while True:
        user_input = float(input("\nEnter volume in gallons: "))

        if user_input < 0:
            print("Exiting program. Goodbye!")
            break
        result = convert_to_liters(user_input)
        print(f"{user_input} gallons is {result:.2f} liters.")
main()