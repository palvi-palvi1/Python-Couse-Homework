def sum_of_integers(values):
    total = 0
    for value in values:
        total += value
    return total

lists = [1,2,3,4,5]
sumOfIntegers = sum_of_integers(lists)
print(f"Sum of given listed is {sumOfIntegers}")
