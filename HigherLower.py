import random
from people_data import data

from art_HigherLower import logo,vs

run_game = False
print(logo)
ask_play = input("Enter 's' to start the Higher Lower Gaame : ").lower()
if ask_play == 's':
    run_game = True
else:
    print("Thank you! Visit Again.")

used_set = set()
a_person = random.choice(data)
used_set.add(a_person['name'])

score = 0

while run_game == True:
    b_person = random.choice(data)
    if b_person['name'] in used_set:
        b_person = random.choice(data)
    elif b_person['name'] not in used_set:
        used_set.add(b_person['name'])

    print(f"\nCompare A: {a_person['name']}, a {a_person['description']}, from {a_person['country']}.\n")
    print(vs)
    print(f"\nCompare B: {b_person['name']}, a {b_person['description']}, from {b_person['country']}.\n")
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower = a_person['follower_count']
    b_follower = b_person['follower_count']
    if a_follower > b_follower:
        correct_answer = 'a'
    else:
        correct_answer = 'b'
    if user_choice == correct_answer:
        print("You are right! Continue...")
        score += 1
        print(f"Your current score is: {score}.")
        if correct_answer == 'b':
            a_person = a_person
        elif correct_answer == 'a':
            a_person = b_person
    elif user_choice != correct_answer:
        print(f"You are wrong! {a_person['name']} has {a_follower} million followers and {b_person['name']} has {b_follower} million followers.")
        run_game = False
        print("Game Over. Thank you for playing!")

    
    



