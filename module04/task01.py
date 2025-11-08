number = 1
count = 0
while number <= 1000:
    if number % 3 == 0:
        print(number)
        number += 1
    number += 1

    print(f"total numbers divisible by 3: {count}")

