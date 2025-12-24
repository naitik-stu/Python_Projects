import random

cards_for_a = [1,2,3,4,5,6,7,8,9,10,10,10,10]
cards_for_b = [1,2,3,4,5,6,7,8,9,10,10,10,10]

print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      '------'                           |__/          
""")


start_bj = input("Enter 'y' to start the game : ")
if start_bj == "y":
    run_bj = True

def deal_cards(player_a, player_b):
    a_1 = 0
    a_2 = 0
    b_1 = 0
    b_2 = 0
    a_1 = random.choice(cards_for_a)
    cards_for_a.remove(a_1)
    a_2 = random.choice(cards_for_a)
    cards_for_a.remove(a_2)
    b_1 = random.choice(cards_for_b)
    cards_for_b.remove(b_1)
    b_2 = random.choice(cards_for_b)
    cards_for_b.remove(b_2)
    player_a.append(a_1)
    player_a.append(a_2)
    player_b.append(b_1)
    player_b.append(b_2)

while run_bj == True:

    cards_a = []
    cards_b = []

    deal_cards(cards_a, cards_b)

    show_b = random.choice(cards_b)

    print(f"Your Cards = {cards_a}, Score {sum(cards_a)}")
    print(f"Computer's One Card = {show_b}")

    player_bj = True

    while player_bj == True:

        hit_or_stand = input("Enter 'y' to hit, 'n' to stand : ")
        if hit_or_stand == "y":
            cards_a.append(random.choice(cards_for_a))
            print(f"Your Cards = {cards_a}, Score {sum(cards_a)}")
        elif hit_or_stand == "n":
            print(f"Your Cards = {cards_a}")
            player_bj = False
            dealer_bj = True

    while dealer_bj == True:
        if sum(cards_b)< 17:
            cards_b.append(random.choice(cards_for_b))
        elif sum(cards_b)<= 17:
            dealer_bj = False

        

    if player_bj == False and dealer_bj == False:
        if sum(cards_a)> 21 and sum(cards_b)> 21:
            print(f"Your Cards = {cards_a}, Score {sum(cards_a)} \n Dealer's Cards = {cards_b}, Score {sum(cards_b)}")
            print("Both Busted!!")
            print("No One Won")
            run_bj = False
        elif sum(cards_a)> 21 and sum(cards_b)<= 21:
            print(f"Your Cards = {cards_a}, Score {sum(cards_a)} \n Dealer's Cards = {cards_b}, Score {sum(cards_b)}")
            print("You Busted!!")
            print("Coputer Won")
            run_bj = False
        elif sum(cards_b)> 21 and sum(cards_a)<= 21:
            print(f"Your Cards = {cards_a}, Score {sum(cards_a)} \n Dealer's Cards = {cards_b}, Score {sum(cards_b)}")
            print("Computer Busted")
            print("You Won!!")
            run_bj = False
        elif sum(cards_a)> sum(cards_b):
            print(f"Your Cards = {cards_a}, Score {sum(cards_a)} \n Dealer's Cards = {cards_b}, Score {sum(cards_b)}")
            print("You Won!!")
            run_bj = False
        elif sum(cards_a) < sum(cards_b):
            print(f"Your Cards = {cards_a}, Score {sum(cards_a)} \n Dealer's Cards = {cards_b}, Score {sum(cards_b)}")
            print("You loose!!")
            print("Computer Won")
            run_bj = False
