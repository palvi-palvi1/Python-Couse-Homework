city_name = []
print("enter the name of five cities:")
for i in range(5):
    city = input(f"enter city {i+1}: ")
    city_name.append(city)
print("\n cities:")
for city in city_name:
    print(city)

