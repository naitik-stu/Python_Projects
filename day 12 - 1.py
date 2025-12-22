import random

numbers = list(range(1,101))

print("""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|      
""")

run_game_ask = input("Enter 'y' to start the game : ")

if run_game_ask == "y":
    run_game = True

while run_game == True:
    print("Welcome To The Number Guessing Game!!")
    print("Im Guessing A Number Beteween 1 - 100 ")
    ask_level = input("which level 'easy' or 'hard' : ")

    chances = 0

    if ask_level == "easy":
        chances = 10
        run = True

    elif ask_level == "hard":
        chances = 5
        run = True

    win_number = random.choice(numbers)

    while run == True:
        print(f"\n{chances} Chances remaining ")
        guess = int(input("\nTake a Guess : "))
        
        if guess == win_number:
            print(f"You won the number is {win_number}")
            run = False
            run_game = False

        elif guess != win_number:
            if win_number > guess:
                print("Too Low")
            elif win_number < guess:
                print("Too High")
            chances -= 1
            print(f"Wrong Guess")
            if chances == 0:
                run = False
                run_game = False
                print(f"You lost the number was {win_number}")

