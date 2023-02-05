name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
    "\nIt is 7AM, you have a job interview at 9AM, do you go back to bed or wake up.\nType 'sleep' if you want to back to sleep or 'wake up' if you want to get ready: ").lower()

if answer == "sleep":
    answer = input(
        "\nIt is now 8AM, do you continue to sleep or wake up?\nType sleep or wake up: ")

    if answer == "sleep":
        print("\nYou over slept and late for your interview")
    elif answer == "wake up":
        print("\nYou got up in time for the interview but no time to have breakfast and failed your interview.")
    else:
        print('\nNot a valid option. You lose.')

elif answer == "wake up":
    answer = input(
        "\nAs you approach the coffee machine, you had a sudden urge to go bathroom.\nType 'coffee' for make your coffee or 'bathroom' to go to the bathroom:  ")

    if answer == "coffee":
        print("\nYou couldnt hold it in and pee'd yourself.")
    elif answer == "bathroom":
        print("\nYou felt good after going to the bathroom.")
    else:
        print('\nNot a valid option. You lose.')

else:
    print('\nNot a valid option. You lose.')

print("\nThank you for playing", name)