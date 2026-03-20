def choose_character(Character):
#This function allows the player to select a character and return the selected character back to the main.py file
    choosing_character = True
#controls the selection loop

    while choosing_character:
            print("Pick your character:")
#Shows the different characters

            character_lists = list(Character.keys())
#Turns the dictonary keys into a list so the choices are displayed as numbers 
           
            for i in range(len(character_lists)):
                print(i + 1, "_", character_lists[i])
#Allows the character to be printed with a number
           
            choice = int(input("Enter the number of the character you would like to pick:  "))
#gets the users input from the character selection
           
            selected = character_lists [choice - 1]
#Select the character based off the number that was input by the player
    
            print("you selected", selected)
#Displays selected character

            print("Abilities:")
#
            for ability in Character[selected]:
                print(ability, "- Damage:", Character[selected][ability])
#Displays the ablilities and the amounts of damage from each ability

            Confirm = input("Press 'y' to confirm or 'n' to go back: ")
#Ask player to confirm their selection
            if Confirm.lower() == 'y':
                print("character selected :", selected)
#Confirms again
                return selected
            else:
                print("select again")
#Allows the player to select again if they have not confirmed