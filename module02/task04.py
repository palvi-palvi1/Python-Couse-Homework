num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

sum_result = num1 + num2 + num3

product_result = num1 * num2 * num3

average_result = sum_result / 3

print("\nResults")
print(f"Sum: {sum_result}")
print(f"Product: {product_result}")
print(f"Average: {average_result:.2f}") # Format average to two decimals
