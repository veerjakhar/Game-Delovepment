dict = {"Peanut": "Supporter", "Pebble": "Distracter", "Vee": "Extracter"}

while True:
    print("1. Insert")
    print("2. Display all toons")
    print("3. Display all roles")
    print("4. Get role")
    print("5. Delete")
    choice = int(input("Please anter a number from 1-5: "))
    if choice == 1:
        toon = input("Enter toon: ")
        role = input("Enter toon's role: ")
        dict[toon] = role
    elif choice == 2:
        print(list(dict.keys()))
    elif choice == 3:
        print(list(dict.values()))
    elif choice == 4:
        ft = input("Input the toon you want to find: ")
        print(dict.get(ft))
    elif choice == 5:
        dt = input("Input the toon you want to delete: ")
        del dict[dt]
    else:
        print("Please enter a valid option: ")
        continue
