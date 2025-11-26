number_input = input("enter a number (blank to stop): ")
smallest_number = None
largest_number = None
while number_input != "":
    number = float(number_input)
    if smallest_number is None or number < smallest_number:
        smallest_number = number
    if largest_number is None or number > largest_number:
        largest_number = number
    number_input = input("enter a number (blank to stop): ")
print("smallest number entered:", smallest_number)
print("largest number entered:", largest_number)
