def sum_list_numbers(numbers):
    total = 0
    for x in numbers:
        total = total + x
    return total
def main():
    my_numbers = [1, 2, 3, 4, 5]
    total_sum = sum_list_numbers(my_numbers)
    print(f"The list is: {my_numbers}")
    print(f"The sum of the numbers is: {total_sum}")

main()