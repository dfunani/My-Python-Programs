import pyinputplus
import sys
from card import Card
import random


def Main():
    '''Blackjack, inspired by Al Sweigart al@inventwithpython.com'''
    try:
        with open('money.txt', 'r') as f:
            MONEY = int(f.read())
    except:
        MONEY = 5000
    if MONEY == 0:
        MONEY = 5000
    Display(MONEY, "Money")
    bet = "0"
    while bet.isdigit() and (int(bet) == 0 or int(bet) > MONEY):
        bet = GetBet(MONEY)
    if not bet.isdigit():
        return sys.exit()
    bet = int(bet)
    Display(bet, "Bet")
    PLAYER = 0
    DEALER = 0
    PlayerDeck = [Card().RenderBack()]
    DealerDeck = [Card().RenderBack()]

    while True:
        Display(MONEY, "Money")
        Display(bet, "Bet")

        if PLAYER > 21:
            MONEY -= bet
            with open('money.txt', 'w') as f:
                f.write(str(MONEY))
            return sys.exit(f"You lose {bet}")
        DeckDisplay(PlayerDeck, f"Player: {str(PLAYER)}")
        DeckDisplay(DealerDeck, f"Dealer: {str(DEALER)}")
        choice = pyinputplus.inputChoice(
            prompt="(H)it, (S)tand, (D)ouble down\n>", choices=["H", "S", "D"])

        if choice == 'D' and len(PlayerDeck) == 1:
            bet *= 2
            Display(bet, "Bet")
            choice = "H"
        elif choice == 'D':
            print("Can only double down on first turn")
            choice = "H"

        if choice == "S":
            deal = DealerDeck.pop(0)
            if deal[1][1] == '#':
                temp = Card()
                check = False

                if temp.value.isdigit() and DEALER + int(temp.value) > 21:
                    DealerDeck.insert(0, deal)
                    check = True
                elif (temp.value == "A" and DEALER + 11 > 21) or (temp.value == "A" and DEALER + 1 > 21):
                    DealerDeck.insert(0, deal)
                    check = True
                elif ((temp.value == "J" or temp.value == "K" or temp.value == "Q") and DEALER + 10 > 21):
                    DealerDeck.insert(0, deal)
                    check = True
                else:
                    DealerDeck.insert(0, temp.RenderFront())

                if temp.value.isdigit() and not check:
                    DEALER += int(temp.value)
                elif temp.value == "A" and not check:
                    if DEALER + 11 > 21:
                        DEALER += 1
                    else:
                        DEALER += 11
                elif not check:
                    DEALER += 10

                DeckDisplay(PlayerDeck, f"Player: {str(PLAYER)}")
                DeckDisplay(DealerDeck, f"Dealer: {str(DEALER)}")

                if not check:
                    print(f"Dealer drew a {temp.value} of {temp.shape}.\n")
                    MONEY -= bet
                    with open('money.txt', 'w') as f:
                        f.write(str(MONEY))
                    sys.exit(f"You lose {bet}") if PLAYER >= DEALER else sys.exit(
                        f"You lose {bet}")
                else:
                    print(f"Dealer chose to stand.\n")
                    MONEY += bet
                    with open('money.txt', 'w') as f:
                        f.write(str(MONEY))
                    sys.exit(f"You win {bet}") if PLAYER >= DEALER else sys.exit(
                        f"You lose {bet}")

        if choice == "H":
            temp = PlayerDeck.pop(0)

            if temp[1][1] == '#':
                temp = Card()
                PlayerDeck.insert(0, temp.RenderFront())

                if temp.value.isdigit():
                    PLAYER += int(temp.value)
                elif temp.value == "A":
                    PLAYER += int(pyinputplus.inputChoice(
                        prompt="Play Ace as 1 or 11?\n", choices=["1", '11']))
                else:
                    PLAYER += 10
            else:
                return sys.exit("Something went wrong")

            print(f"You drew a {temp.value} of {temp.shape}.\n")

        deal = DealerDeck.pop(0)

        if deal[1][1] == '#':
            temp = Card()
            check = False

            if temp.value.isdigit() and DEALER + int(temp.value) > 21:
                DealerDeck.insert(0, deal)
                check = True
            elif (temp.value == "A" and DEALER + 11 > 21) or (temp.value == "A" and DEALER + 1 > 21):
                DealerDeck.insert(0, deal)
                check = True
            elif ((temp.value == "J" or temp.value == "K" or temp.value == "Q") and DEALER + 10 > 21):
                DealerDeck.insert(0, deal)
                check = True
            else:
                DealerDeck.insert(0, temp.RenderFront())

            if temp.value.isdigit() and not check:
                DEALER += int(temp.value)
            elif temp.value == "A" and not check:
                if DEALER + 11 > 21:
                    DEALER += 1
                else:
                    DEALER += 11
            elif not check:
                DEALER += 10

            DeckDisplay(PlayerDeck, f"Player: {str(PLAYER)}")
            DeckDisplay(DealerDeck, f"Dealer: {str(DEALER)}")

            if not check:
                DealerDeck.insert(0, Card().RenderBack())
                print(f"Dealer drew a {temp.value} of {temp.shape}.\n")
            else:
                print(f"Dealer chose to stand.\n")

            PlayerDeck.insert(0, Card().RenderBack())
        else:
            return sys.exit("Something went wrong")
        print("----------------------------------------------------")

        if PLAYER == 21:
            MONEY += bet
            with open('money.txt', 'w') as f:
                f.write(str(MONEY))
            return sys.exit(f"You won {bet}")
        elif DEALER == 21:
            MONEY -= bet
            with open('money.txt', 'w') as f:
                f.write(str(MONEY))
            return sys.exit(f"You lose {bet}")


def Display(bal, text="Money"):
    print(f"{text}: ${bal}")


def GetBet(bal):
    return pyinputplus.inputRegex(regex=r"^(?:[1-9]|\d{2,3}|[1-4]\d{3}|5000)$|[q]+|[Q]", prompt=f"How much do you bet? (1-{bal}, or QUIT)\n")


def DeckDisplay(cards, score):
    row0 = ''
    row1 = ''
    row2 = ''
    row3 = ''
    for card in cards:
        row0 += card[0]
        row1 += card[1]
        row2 += card[2]
        row3 += card[3]

    print(f'''{score}
{row0}
{row1}
{row2}
{row3}
''')


if __name__ == '__main__':
    Main()
