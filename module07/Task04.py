def get_even_numbers(numbers):
    new_list = []
    for n in numbers:
        if n % 2 == 0:
            new_list.append(n)
    return new_list

original_list = [1,2,3,4,5,6,7,8,9]
new_filter_list = get_even_numbers(original_list)
print("original_list:",  original_list)
print("even_number:" ,  new_filter_list)
