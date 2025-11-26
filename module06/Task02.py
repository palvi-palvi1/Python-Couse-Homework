def manage_names():

    user_names = set()
    while True:
        name = input("Enter a name: ")
        if not name:
            break
        if name in user_names:
            print("Existing name")
        else:
            print("New name")
            user_names.add(name)

    print("\nThe unique names are:")
    for name in user_names:
        print(name)
manage_names()
