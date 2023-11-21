logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
import os

def clear_console():
  os.system('cls')

def play():
    print(logo)
    import random
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    player = [cards[random.randint(0,len(cards)-1)],cards[random.randint(0,len(cards)-1)]]
    print(f"Your cards: {player}")



    dealer =  [cards[random.randint(0,len(cards)-1)],cards[random.randint(0,len(cards)-1)]]
    print(f"Dealer's card : {dealer[1]}")

    ai_decision = ["hit","stand"]

    def sum(card1,card2):
        return card1+card2

    def add_card():
        new_card = cards[random.randint(0,len(cards)-1)]
        return new_card



    def userTurn(card1,card2):
        proceed = True
        sum_player = sum(card1,card2)

        while proceed:


            print(f"Your Total: {sum_player}")
            if sum_player == 21:
                print("BlackJack")
                return "blackjack",sum_player

            if sum_player > 21:
                # print("Bust! You lose")

                
                return "bust",sum_player

            decision = input("Do you want to 'hit' or 'stand': ").lower()

            if decision == "hit":
                sum_player = sum(sum_player,add_card())
                print("You have hit")
            elif decision == "stand":
                # print("You have stand")
                return "stand",sum_player
            
                
    def dealerTurn(card1,card2):
        proceed = True
        sum_dealer = sum(card1,card2)

        while proceed:


            print(f"Dealer's Total: {sum_dealer}")
            if sum_dealer == 21:
                print("BlackJack")
                return "blackjack",sum_dealer

            if sum_dealer > 21:
                print("Dealer's Bust")
                return "bust",sum_dealer
            if sum_dealer >= 19:
                ai_number = 1
            else:
                ai_number = 0
            decision = ai_decision[ai_number]
            if decision == "hit":
                sum_dealer = sum(sum_dealer,add_card())
                print("Dealer has hit")

            elif decision == "stand":
                print("Dealer has stand")
                
                return "stand",sum_dealer    


    checkUser, userTotal = userTurn(player[0],player[1])

    print(f"Dealer's 2nd card : {dealer[0]}")

    if checkUser == "bust":
        print("Bust! You lose")
        

        
    else:
        checkDealer, dealerTotal = dealerTurn(dealer[0],dealer[1])   
        if checkDealer == "bust":
            print("You win")
        else: 
            if userTotal == dealerTotal:
                print("DRAW")
            elif userTotal> dealerTotal:
                print("You win")
            else:
                print("You Lose")            


    print(f"Dealer's final hand: {dealer}")
    # print(f"Dealer's Total card : {sum(dealer[1],dealer[0])}")


proceeding = True
while proceeding:        
    playhuh = input("Do you want to play blackjack? y/n   ").lower()

    if playhuh == "y":
        clear_console()
        play()
    else:
        print("Thank you")    
        break
