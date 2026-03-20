import random
#Import the random libary to allow the computer to randomly select their characters, attack, and both the user to land critcal hits

from animal_fighters import choose_character
#Imports the function from function.py
play_again = "y"
# play_again makes it so if you want to play the game again

while play_again.lower() == "y":
#This is the loop tha allows the whole to game to run unless the character type n = no
    
    Character = {
        "Cat": {
            "Scratch": 13,
            "slap": 8,
            "Pounce": 18
        },
        "Dog": {
            "Thunder Bark": 20,
            "Bite": 15,
            "Dig": 10
    },
        "Bird": {
            "Peck": 13,
            "Seed blast": 7,
            "Ariel slash": 23
        }   
    }
#I used a dictionary to stores the characters, attacks, and the different amount of damage each attack has
   
    print("welcome to Animal Fighters")
#Displays the welcome with the game's name
    enter_CS = int(input("click 1 if you would like to enter character selection "))
# Ask the user if they want to go into Character selection

#2
    if enter_CS == 1:
       selected = choose_character(Character)
     # brings the function from functions.py, then the selected character is returned and saved in "selected"


#3
    opponents = []
# creates a list for the possible opponents

    for name in Character:
        if name != selected:
            opponents.append(name)
#This loop makes it so that the opponent list of characters does not include yours

    Computer = random.choice(opponents)
    print('the computer chose:', Computer)
#The computers random selection
    Player_health = 100
    Computer_health = 100

    Battle_running = True
# controls if the battle continue

    while Battle_running and Player_health > 0 and Computer_health > 0:
#This loop allows the battle to continue while both the player and the robot are alive

        print("Your health:", Player_health)
        print("computer health:", Computer_health)
    #Displays both of the current health of the player and computer for each turn

        print("select your attack:")
        player_ablities = list(Character[selected].keys())
#Gets all the attack names from the choosen character
      
        for i in range(len(player_ablities)):
            print(i + 1, "-", player_ablities[i], "- Damage:", Character[selected][player_ablities [i]])
#Displays the list of attack with the different amount of a damage

        attack_choice = int(input("Enter the number of your attack:"))
        player_attack = player_ablities[attack_choice - 1]
        player_damage = Character[selected][player_attack]
# When the player selects an attack the program find damage amount

       
        crit = random.randint(1,4)
# randomly selects a number from 1-4
        if crit == 1:
            player_damage = player_damage * 2
            print("Crital hit")
#if the random number is 1 the damaged caused by the player is 2 times of its original amount

        Computer_health -= player_damage
        print("you used", player_attack, "and caused", player_damage, "damage!")
# Displays the result of the player's attack and health of the computer

        if Computer_health <= 0:
            print("Computer is defeated!!!")
            print("you win!")
            Battle_running = False
#If the computer's health gets to 0 or negative, the player wins

        if Battle_running:
            computer_abliliies = list(Character[Computer].keys())
            computer_attack = random.choice(computer_abliliies)
            computer_damage = Character[Computer][computer_attack]
#If the battle is still going the computer is able to randomly select an attack
        #Crital hit for computer

        computer_crit = random.randint(1,4)
# This allows the computer to get a crital hit randomly

        if computer_crit == 1:
            computer_damage = computer_damage * 2
            print("Crital hit against you!")
# allows  the computer to have a random critcal hit

        Player_health -= computer_damage
        print("the computer used",computer_attack, " and caused", computer_damage, "damage")
#Reduces the health of the player and displays damage caused by the computer

        if Player_health <= 0:
            print("You lose!")
            print("computer wins!")
            Battle_running = False
# If the player's health gets to 0 or negative, the computer wins

    play_again = input("would you like to play again? y/n ")

print("Good Game")
# Displays the final message