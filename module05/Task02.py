numbers_list = []
user_input = input("Enter a number (just press Enter key to quit): ")
while user_input != "":
    number = int(user_input)
    numbers_list.append(number)
    user_input = input("Enter a number (or just press Enter to quit): ")
numbers_list.sort(reverse=True)
print("\nTop 5 numbers in descending order:")
top_five = numbers_list[:5]
print(top_five)