import random
number_dice = int(input("how many dice do you want to roll?"))
total_sum = 0
for i in range(number_dice):
    rolldice = random.randint(1,6)
    total_sum += rolldice
print(f"The total sum is: {total_sum}")
