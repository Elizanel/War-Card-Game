#War Card Game 
#Randomized Version Where both players are Computer Generated 
#Elizanel Martinez 
#Version 1.0 
# Help from: https://www.youtube.com/watch?v=r8HH1J-7KyA
            #https://www.youtube.com/watch?v=s8deyqe6kyI
            #https://www.youtube.com/watch?v=62TmpPDs0mM

import random 

def thedeck():
    #Will return any card from the whole deck 
    thecharacters = "♠♣◆♥"
    thenumbers = [str(number) for number in range (2, 11)]
    special_letters = "AKQJ"
    special_cards = [special + suit for special in special_letters for suit in thecharacters]
    regular_cards = [number + suit for number in thenumbers for suit in thecharacters]
    cards = special_cards + regular_cards
    return cards

def the_winner (firstpcard, secondpcard): 
    # This part will be able to determine who is the winner or tie. 
    schar_ranks = {'♣': 1, '◆': 2, '♥': 3, '♠': 4}
    sletter_ranks = {'J': 1, 'Q': 2, 'K': 3, 'A': 4}
    if firstpcard == secondpcard: 
        return 0 
    if firstpcard[0].isdecimal() and secondpcard[0].isalpha():
        return 2
    if firstpcard[0].isalpha() and secondpcard[0].isdecimal():
        return 1 
    if firstpcard[0].isdecimal() and secondpcard[0].isdecimal():
            if int(firstpcard[0]) > int (secondpcard[0]):
                return 1
            if int(firstpcard[0]) < int (secondpcard[0]):
                return 2
    if firstpcard[0].isalpha() and secondpcard[0].isalpha(): 
        if sletter_ranks[firstpcard[0]] > sletter_ranks[secondpcard[0]]:
            return 1
        if sletter_ranks[firstpcard[0]] < sletter_ranks[secondpcard[0]]:
            return 2 
    if  firstpcard[-1] != secondpcard[-1] and firstpcard[:-1] == secondpcard[:-1]:
        if schar_ranks[firstpcard[-1]] > schar_ranks[secondpcard[:-1]]:
            return 1 
        if schar_ranks[firstpcard[-1]] < schar_ranks[secondpcard[:-1]]:
            return 2 

def the_game():
#This part should be able to show the round/s
    cards = thedeck()
    print("Welcome to The Card Game Called War.")
    rounds = input ("How Many Rounds Would You Like To Play Today? ")
    #If someone writes in someothing that isnt a number- it will prompt them to write it again. 
    while not rounds.isdecimal(): 
        print ("Sorry This Number is Invalid. Please Try Again. ")
        rounds = input ("How Many Rounds Would You Like To Play? ")
    #Rounds Start at 0 in order to have the correct number of rounds in the game. 
    rounds_played = 0 
    firstplayer_score, secondplayer_score = 0, 0 
    while rounds_played < int(rounds): 
        round_played = input (f"To Show you round {rounds_played} Press Enter. If You Would Like To Exit, Press E To Exit: ")
        while round_played and round_played != "e":
            round_played = (f"To Show you round {rounds_played} Press Enter. If You Would Like To Exit, Press E To Exit: ")
        # You are able to quit if you do not want to play anymore. 
        if round_played == 'e': 
            print("Thank You For Playing The Card Game War")
            print (30 * '=')
            exit(0)

        firstplayer_card = random.choice(cards)
        secondplayer_card = random.choice(cards)
        #Shows each players card 
        print(f"This is the First Players Card: {firstplayer_card}")
        print(f"This is the Second Players Card: {secondplayer_card}")
        #Writes what a winner is and what to say if there is one or not. 
        winner= the_winner(firstplayer_card, secondplayer_card)
        if winner == 0:
            print ("There is a Tie! Congratulations! No one Lost!")
        if winner == 1: 
            print("Player 1 Won! Better Luck Next Time Player 2 :( ")
            firstplayer_score += 1
        if winner == 2:
            print("Player 2 Won! Better Luck Next Time Player 2 :(" )
            secondplayer_score += 1
        rounds_played += 1
        print(30 * '=', '\n')
    #Aesthetic purposes the = divides each round. 
    print(30 * '=')
    #Information for the end 
    print(f"Total Rounds Played: {rounds_played}")  
    print (f"Player 1 {firstplayer_score}-{secondplayer_score} Player 2") 
    if  firstplayer_score > secondplayer_score: 
        print(f"Congratulations Player 1! You Won ({firstplayer_score} out of {rounds_played} Rounds Played) ")
    if  secondplayer_score > firstplayer_score: 
        print(f"Congratulations Player 2! You Won ({secondplayer_score} out of {rounds_played} Rounds Played) ")
    if firstplayer_score == secondplayer_score: 
        print("ITS A TIE! No One Looses!")

if __name__ == "__main__" : 
    the_game()






        










 
