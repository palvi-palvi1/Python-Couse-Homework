length_str = input("Enter the length of the rectangle: ")
width_str = input("Enter the width of the rectangle: ")

length = float(length_str)
width = float(width_str)

area = length * width
perimeter = 2 * (length + width)

print("--- Results ---")
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
