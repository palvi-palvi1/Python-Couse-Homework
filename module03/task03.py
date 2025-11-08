gender = input("enter your biological gender (male/female): ")
hemoglobin = float(input("enter your hemoglobin level (g/L): "))




if gender.lower() == "female":
    if hemoglobin < 117:
        print("your hemoglobin level is low.")


    elif hemoglobin <= 155:
        print("your hemoglobin level is normal.")
    else:
            print("your hemoglobin level is high.")
elif gender.lower() == "male":
    if hemoglobin < 134:
        print("your hemoglobin level is low.")

    elif hemoglobin <= 167:
            print("your hemoglobin level is normal.")
    else:
            print("your hemoglobin level is normal.")
else:
        print("Invalid gender entered.")

