length = float(input("enter the length of the zander (cm): "))
legal_limit = 42

if length >= legal_limit:
    shortfall = legal_limit - length
    print(f"The zander is {shortfall:.1f} cm below the legal size limit. Please release it back it back into the lack.")

else:
    print("the zander meets the size limit and can be kept.")
    