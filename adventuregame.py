import time
def display_message(message):
    print(message)
    time.sleep(1)

# Function to handle the player's choice
def get_choice(options):
    choice = input("Enter your choice: ").lower()
    while choice not in options:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice: ").lower()
    return choice

# Introduction
display_message("Welcome to the Adventure Game!")
display_message("In this Game you will found a treasure by taking good actions")
display_message("You find yourself in a dark cave with three paths ahead.")

# Main game loop
while True:
    display_message("Enter which cave you want go:")
    display_message("1. First cave")
    display_message("2. Second cave")
    display_message("3. Third cave")
    choice = get_choice(['1', '2','3'])

    if choice == '1':
        display_message("You encounter a dragon!")
        display_message("What will you do?")
        display_message("1. Fight the dragon")
        display_message("2. Run away")
        fight_choice = get_choice(['1', '2'])

        if fight_choice == '1':
            display_message("You should fight the dragon...")
            display_message("Bravo! you defeated the dragon")
            display_message("You Enteres into another cave and you encounter a monster ")
            display_message('What will you do?')
            display_message("1. fight with the monster")
            display_message("2. Run away")
            another_choice=get_choice(['1','2'])
            if another_choice == '1':
                display_message("Bravo! you Defeated the Monster.")
                display_message("You found the treasure and You win the Game!")
                break
            else:
                display_message("you are killed by monster")
                break
        else:
            display_message("You try to run away but the dragon catches you. You lose!")
            break
    elif choice == '2':
        display_message("you find some obsatcles in this cave")
        display_message("what will you do?")
        display_message("1. Face them")
        display_message("2. Run away ")
        fight_choice1 = get_choice(['1','2'])
        if fight_choice1 == '1':
            display_message("You came across the obstacles")
            display_message("you entered into another cave")
            display_message("you found some  people in  this cave")
            display_message("what will you do?")
            display_message("1. Save them and get the treasure")
            display_message("2. Run away")
            another_choice1 =get_choice(['1','2'])
            if another_choice1 == '1':
                display_message('you saved them and found the Treasure')
                display_message("You Win the Game!!")
                break
            else:
                display_message("you lose!")
                break
    elif choice == '3':
        display_message("you found the treasure and you Win!")
        break
            
        



        







