GRAMS_PER_LOT = 13.3
LOTS_PER_POUND = 32
POUNDS_PER_TALENT = 20
GRAMS_PER_KILOGRAM = 1000

talents = float(input("Enter talents: \n"))
pounds = float(input("Enter pounds: \n"))
lots = float(input("Enter lots: \n"))


total_lots = (talents * POUNDS_PER_TALENT * LOTS_PER_POUND) + \
             (pounds * LOTS_PER_POUND) + lots

total_grams = total_lots * GRAMS_PER_LOT

kilograms = int(total_grams // GRAMS_PER_KILOGRAM)
remaining_grams = total_grams % GRAMS_PER_KILOGRAM


print("\nThe weight in modern units:")
print(f"{kilograms} kilograms and {remaining_grams:.2f} grams.")
