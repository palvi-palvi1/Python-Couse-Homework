user_input = input("enter a digit to check it is a prime number: ")
number = int(user_input)
if number <= 1:
    print(f"{number} is NOT a prime number.")
else:
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    if is_prime:
        print(f"{number} IS a prime number.")
    else:
        print(f"{number} is NOT a prime number.")