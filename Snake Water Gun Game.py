import random
import emoji

print("============:Welcome to the Snake Game:=========")
x = int(input("Are you ready for the game ?\n1. Yes\n2. No\n\n"))
user_name = input("Set your name before starting the game: ")
print(f"\n-------:Thank you {user_name} for choosing to play the game with us:-------")
if x == 1:
    user_count = 0
    comp_count = 0
    tied_count = 0
    i = 0
    while i < 10:
        choice = random.choice(['S','W','G'])
        user_input = input("\nIt's your turn now. Enter Snake(S)/Gun(G)/Water(W)\n")
        if (user_input.upper() == 'G' and choice == 'S') or (user_input.upper() == 'S' and choice == 'W') or (user_input.upper() == 'W' and choice == 'G'):
            print("You Won this time")
            print(f"Computer's choice was: {choice}")
            user_count+=1

        elif user_input.upper() == choice:
            print("No Result. Game tied this time")
            print(f"Computer's choice was: {choice}")
            tied_count+=1
        else:
            print("Sorry !! You lost this time")
            print(f"Computer's choice was: {choice}")
            comp_count+=1
        i+=1
else:
    print("\nThanx for coming. Please visit next time.")

try:
    print("\n------------------FINAL RESULT------------------")
    print(f"\nYou won {user_count} times out of 10.\nComputer won {comp_count} times out of 10.\nGame tied {tied_count} times")
    if user_count > comp_count:
        smiley = emoji.emojize(":grinning_face_with_big_eyes:")
        print(f"\nYipeeee !!! You are the winner in this game {smiley}")
    elif user_count == comp_count:
        print("\nGame tied. Well Played both of you")
    else:
        print("Computer is the winner in this game")
    print("\nThank you for having played this game with us. ")
except:
    pass