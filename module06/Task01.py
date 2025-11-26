season = ("spring", "summer", "autumn", "winter")
month_input = input("Enter the number of a month (1-12): ")
month_number = int(month_input)
index = (month_number % 12) // 3
corresponding_season = season[index]
print(f"Input: {month_number}")
print(f"Output: {corresponding_season}")
