print("Welcome to Daily Life Simulator")

name = input("Please Enter your name: ")

wake_choice = input("Wake up or stay asleep? (W/S): ").lower()

if wake_choice == "w" or wake_choice == "wake up":
    print("Good morning!" + " " + name)
elif wake_choice == "s" or wake_choice == "stay asleep":
    print(f"You chose to stay asleep" + " " +  name)
else:
    print("You seem confused... Daydreaming.")

print("\nChoose What to do?")
print("A. Eat Breakfast")
print("B. Wash Your Face")
print("C. Moisturizer")
print("D. Take a Bath")
print("E. Study")

choice = input("Enter a Choice (A-E): ")

#Breakfast Time
if choice == "A" or choice == "a":
    print("\nAvailable Breakfast:")
    print("1. Rice with Fried Chicken")
    print("2. Rice with Adobo")
    print("3. Oatmeal")
    print("4. Rice with Vegetable")
    print("5. Rice with Fried Fish")

    breakfast = input("Enter (1-5): ")

    if breakfast == "1":
        print("You ate Rice with Fried Chicken")
    elif breakfast == "2":
        print("You ate Rice with Adobo")
    elif breakfast == "3":
        print("You ate Oatmeal")
    elif breakfast == "4":
        print("You ate Rice with Vegetable")
    elif breakfast == "5":
        print("You ate Rice with Fried Fish")
    else:
        print("You are daydreaming in the Simulator")

#Wash Face Time
elif choice == "B" or choice == "b":
    print("\nAvailable Products:")
    print("A. Cleanser")
    print("B. Soap")

    face = input("Select (A/B): ")

    if face == "A" or face == "a":
        print("You used Cleanser")
    elif face == "B" or face == "b":
        print("You used Soap")
    else:
        print("You are daydreaming in the Simulator")

#Moisturizer Time
elif choice == "C" or choice == "c":
    print("\nAvailable Products:")
    print("A. Moisturizer")
    print("B. Aloe Vera")

    moisturizer = input("Select (A/B): ")

    if moisturizer == "A" or moisturizer == "a":
        print("You used Moisturizer")
    elif moisturizer == "B" or moisturizer == "b":
        print("You used Aloe Vera")
    else:
        print("You are daydreaming in the Simulator")

#Take a Bath Time
elif choice == "D" or choice == "d":
    print("\nBath Products:")
    print("1. Soap")
    print("2. Bodywash")
    print("3. Shampoo")
    print("4. Conditioner")

    bath = input("Choose (1-4): ")

    if bath == "1":
        print("You used Soap")
    elif bath == "2":
        print("You used Bodywash")
    elif bath == "3":
        print("You used Shampoo")
    elif bath == "4":
        print("You used Conditioner")
    else:
        print("You are daydreaming in the Simulator")

#Study Time
elif choice == "E" or choice == "e":
    print("\nSubjects:")
    print("1. Programming")
    print("2. History")
    print("3. Data Structures & Algorithms")
    print("4. Mathematics")
    print("5. Entrepreneur")

    subject = input("Choose (1-5): ")

    if subject == "1":
        print("You studied Programming")
    elif subject == "2":
        print("You studied History")
    elif subject == "3":
        print("You studied Data Structures & Algorithms")
    elif subject == "4":
        print("You studied Mathematics")
    elif subject == "5":
        print("You studied Entrepreneur")
    else:
        print("You are daydreaming in the Simulator")

else:
    print("You are daydreaming in the Simulator")

#Next Step
print("\nWhat will you do next?")
print("A. Grocery")
print("B. Work")
print("C. Stay Home")

next_step = input("Enter (A-C): ")

#Grocery
if next_step == "A" or next_step == "a":
    print("\nWelcome to Grocery")

    product = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    total = price * quantity
    money = float(input("Enter your money: "))
    change = money - total

    print("Product:", product)
    print("Total:", total)
    print("Change:", change)

    go_home = input("Do you want to go home? (y/n): ")

    if go_home == "y" or go_home == "Y":
        print("Drive safe going home!")

        sleep = input("Do you want to sleep? (y/n): ")

        if sleep == "y" or sleep == "Y":
            print("Good night! End of the simulator.")
        elif sleep == "n" or sleep == "N":
            print("You stayed awake. End of the Simulator.")
        else:
            print("You are daydreaming in the Simulator")

    elif go_home == "n" or go_home == "N":
        print("You stayed outside. End of the Simulator.")
    else:
        print("You are daydreaming in the Simulator")

#Work Time
elif next_step == "B" or next_step == "b":
    print("\nChoose outfit:")
    print("1. Casual")
    print("2. Formal")

    outfit = input("Choose (1-2): ")

    if outfit == "1":
        print("You wore Casual outfit")
    elif outfit == "2":
        print("You wore Formal attire")
    else:
        print("You are daydreaming in the Simulator")

    print("\nChoose car:")
    print("1. Porsche")
    print("2. Mercedes")
    print("3. Ferrari")

    car = input("Choose (1-3): ")

    if car == "1":
        print("You drove Porsche to work")
    elif car == "2":
        print("You drove Mercedes to work")
    elif car == "3":
        print("You drove Ferrari to work")
    else:
        print("You are daydreaming in the Simulator")

    work_time = input("What time is your work? ")

    print("You are scheduled to work at", work_time)

    go_home = input("Do you want to go home? (y/n): ")

    if go_home == "y" or go_home == "Y":
        print("After work, drive safe going home!")

        sleep = input("Do you want to sleep? (y/n): ")

        if sleep == "y" or sleep == "Y":
            print("Good night! End of the Simulator.")
        elif sleep == "n" or sleep == "N":
            print("You stayed awake. End of the Simulator.")
        else:
            print("You are daydreaming in the Simulator")

    elif go_home == "n" or go_home == "N":
        print("You stayed at work. End of the Simulator.")
    else:
        print("You are daydreaming in the Simulator")

#Home Time
elif next_step == "C" or next_step == "c":
    print("\nChoose a chore:")
    print("1. Clean")
    print("2. Cook")
    print("3. Rest")

    chore = input("Choose (1-3): ")

    if chore == "1":
        print("You cleaned the house")
    elif chore == "2":
        print("You cooked food")
    elif chore == "3":
        print("You rested")
    else:
        print("You are daydreaming in the Simulator")

    go_home = input("Do you want to go home? (y/n): ")

    if go_home == "y" or go_home == "Y":
        print("You are already at home!")

        sleep = input("Do you want to sleep? (y/n): ")

        if sleep == "y" or sleep == "Y":
            print("Good night! End of the Simulator.")
        elif sleep == "n" or sleep == "N":
            print("You stayed awake. End of the Simulator.")
        else:
            print("You are daydreaming in the Simulator")

    elif go_home == "n" or go_home == "N":
        print("You stayed awake at home. End of the Simulator.")
    else:
        print("You are daydreaming in the Simulator")

else:
    print("You are daydreaming in the Simulator")

print("\n End of the Simulator")