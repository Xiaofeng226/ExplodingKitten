# Name: Max Schernikau and Xiaofeng Li
# File: final.py
#
#
import random
EK = "Exploding Kitten"
EKD = "You must show this card immediately. Unless you have a Defuse, you're dead. When you die, put the kitten that killed you face up in front of you so that everyone can see that you're dead, and the rest of your cards face down in front of you."

D = "Defuse Card"
DD = "If you drew an Exploding Kitten, you can play this card instead of dying. Place your Defuse in the Discard Pile. Then take the Exploding Kitten, and without reordering or viewing the other cards, secretly put it back in the Draw Pile anywhere you'd like. Your turn is over after playing this card."

A = "Attack Card"
AD = "End your turn without drawing a card, and immediately force the next player to take 2 turns in a row. If the victim of an Attack plays this card on any of their turns, the attacks 'stack' and their turns are immediately transferred to the next player, who must take the Attacker's current and remaining untaken turn(s) PLUS 2 additional turns."

F = "Favor Card"
FD = "Force any other player to give you 1 card from their hand. They choose which card to give you."

N = "Nope Card"
ND = "Stop any action except for an Exploding Kitten or a Defuse. It's as if the card beneath a Nope never existed. You can also play a Nope on another Nope to negate it and create a Yup, and so on. You can play a Nope at any time before an action has begun, even if it's not your turn. Any cards that have been Noped are lost. Leave them in the Discard Pile. You can even play a Nope on a Special Combo."

Sh = "Shuffle Card"
ShD = "Shuffle the Draw Pile until the next player tells you to stop"

Sk = "Skip Card"
SkD = "Immediately end your turn without drawing a card."

Se = "See the Future Card"
SeD = "Privately view the top 3 cards from the Draw Pile and put them back in the same order. Don't show the cards to the other players."

CD = "These cards are powerless on their own, but if you collect any 2 matching Cat Cards, you can play them as a Pair to steal a random card from any player."
Ct = "Taco Cat"
Cw = "Watermelon Cat"
Cp = "Potato Cat"
Cb = "Beard Cat"
Cr = "Rainbow Cat"

Deck = [EK] + 6*[D] + 4*[A] + 4*[F] + 4*[Sh] + 4*[Sk] + 5*[Se] + 4*[Ct] + 4*[Cw] + 4*[Cp] + 4*[Cb] + 4*[Cr]

P1 = []
P2 = []
Discard = []
n = 0


def drawC(Deck, B):
    """Takes element 0 from list A and puts it in list B
    """
    x = Deck[0]
    Deck.pop(0)
    B += [x]




# Cards


def shuffle(A):
    """ Rearranges the list of A
    """
    random.shuffle(A)
    return A
        

def checkLost(A):
    """ Checks if hand A wins 
    """
    if D not in A and EK in A:
        return True
    else:
        return False


def skip(CL, P, Discard):
    """Skips one turn ahead
    """
    print("You skip to your opponents turn!")
    print()
    Discard += [P[CL]]
    P.pop(CL-1)


def favor(P1, P2):
    """P1 gives P2 a card of thier choice
    """
    print()
    print(P1)
    print()
    CardL = int(input("What is the location of the card you want to give to AI?")) - 1
    if CardL > len(P1):
        return "ERROR"
    if CardL < 0:
        return "ERROR"
    Card = P1[CardL]
    print("AI was given " + Card + " !")
    P1.pop(CardL)
    P2 += [Card]
    print()

def aifavor(P1, P2):
    Card = ""
    if P2 == []:
        print("Bot has no cards, you wasted your Favor Card LOL")
    elif Ct in P2 or Cw in P2 or Cb in P2 or Cr in P2 or Cp in P2:
        if Ct in P2:
            Card = Ct
        elif Cw in P2:
            Card = Cw
        elif Cb in P2:
            Card = Cb
        elif Cr in P2:
            Card = Cr
        elif Cp in P2:
            Card = Cp
    elif Sh in P2:
        Card = Sh
    elif Se in P2:
        Card = Se
    elif Sk in P2:
        Card = Sk
    elif A in P2:
        Card = A
    elif N in P2:
        Card = N
    elif D in P2:
        Card = D
    else:
        Card = F
    P1 += [Card]
    P2.remove(Card)
    print("AI gave you " + Card + "!")
        


def sTF(D, P, Discard):
    """See the top three element of the Deck list
    """
    Discard += [Se]
    P.remove(Se)
    return D[:3]
    


def twoOAK(P1, P2):
    """Playing two of the same cat card and randomly taking one of P2's card
    """
    selection = random.choice(range(len(P2)))
    P1 += [P2[selection]]
    print("You Took " + P2[selection])
    P2.pop(selection)

def AiOAK(P1, P2):
    """Playing two of the same cat card and randomly taking one of P2's card
    """
    selection = random.choice(range(len(P2)))
    P1 += [P2[selection]]
    print("Ai Took " + P2[selection])
    P2.pop(selection)

# Game Functions


def explode(P, Deck, Discard):
    """Checks if there is an exploding kitten in your hand and uses your diffuse if there if not lose
    """
    Survive = True
    if D in P:
        print()
        print("You drew and exploding kitten!")
        print()
        print("You used a defuse card!")
        print("You survive... for now...")
        print()
        P.remove(D)
        Discard += [D]
        P.remove(EK)
        ekL = int(input("Where in the deck do you want to put the exploding kitten? (+ interger)"))
        if ekL >= len(Deck):
            Deck += [EK]
        elif ekL <= 0:
            return "ERROR"
        else:
            Deck.insert(ekL-1, EK)
        print()
        return Survive
    else:
        print()
        print("YOU LOSE!!!! THE AI WINS")
        print()
        Survive = False
        return Survive

def aiexplode(P, Deck, Discard):
    """Checks if there is an exploding kitten in your hand and uses your diffuse if there if not lose
    """
    Survive = True
    if D in P:
        print()
        print("Ai drew and exploding kitten!")
        print()
        print("Ai used a defuse card!")
        print("Ai survives... for now...")
        print()
        P.remove(D)
        Discard += [D]
        P.remove(EK)
        if len(Deck) > 3:
            ekL = random.choice(range(3,len(Deck)))
        else:
            ekL = len(Deck)
        if ekL >= len(Deck):
            Deck += [EK]
        else:
            Deck.insert(ekL-1, EK)
        print()
        return Survive
    else:
        print()
        print("AI exploded! You WIN")
        print()
        Survive = False
        return Survive

        


def hostGame(P1, P2, Deck, Discard):
    """Hosts a game of exploding kittens 
    """
    shuffle(Deck)
    for x in range(6):
        Deck.remove(D)
    Deck.remove(EK)
    P1 += [D]
    P2 += [D]
    for x in range(5):
        drawC(Deck, P1)
    for x in range(5):
        drawC(Deck, P2)
    Deck += 4*[D] + [EK]
    #shuffle(Deck)
    Turn = 0
    x = 1
    y = x
    
    while checkLost(P1) == False and checkLost(P2) == False:
        Turn += 1
        n = 0
        if Turn%2 == 1:
            while n == 0:
                print(P1)
                print()
                PC = input("Do you want to play a card? (Y or N): ")
                if PC == "N":
                    drawC(Deck, P1)
                    if P1[(len(P1))-1] == EK:
                        if explode(P1, Deck, Discard) == False:
                            return 0
                        else:
                            x += 1
                            pass
                    break
                elif PC == "Y":
                    while n == 0:
                        print(P1)
                        print()
                        CardL = int(input("What is the the numerical position of the card you want to play: "))
                        Card = P1[CardL-1]
                        print(Card)
                        if Card == D:
                            print("Error. Cannot be played")
                            print()
                        if Card == Sk:
                            skip(CardL, P1, Discard)                      
                            break
                        if Card == Sh:
                            shuffle(Deck)
                            Discard += [Card]
                            P1.pop(CardL-1)
                        if Card == Ct or Card == Cw or Card == Cp or Card == Cb or Card == Cr:
                            P1.remove(Card)
                            if Card in P1:
                                print("You played two of a kind!")
                                print()
                                Discard += 2*[Card]
                                P1.remove(Card)
                                twoOAK(P1, P2)
                            else:
                                print("You do not have two of a kind!")
                                print()
                                P1 += [Card]
                        if Card == F:
                            aifavor(P1,P2)
                            P1.pop(CardL-1)
                            Discard += Card
                        if Card == Se:
                            S = sTF(Deck, P1, Discard)
                            print("Next Three Cards Are: ")
                            print()
                            print(S)
                            print()
                        print()
                        print()
                        print("The bot has " + str(len(P2)) + " cards")
                        print()
                        print(P1)
                        print()

                        if Card == A:
                            P1.remove(A)
                            Discard += [A]
                            print()
                            print("You play an attatck card!")
                            print("AI will now have two turns")
                            print()
                            for x in range(1):   
                                while n == 0:
                                    if P2 == []:
                                        print("AI does not play a card!")
                                        print()
                                        drawC(Deck, P2)
                                        if P2[(len(P2))-1] == EK:
                                            if aiexplode(P2, Deck, Discard) == False:
                                                return 0
                                            else:
                                                pass
                                        break
                                    if P2 != []:
                                        if x > y:
                                            if Sh in P2:
                                                shuffle(Deck)
                                                P2.remove(Sh)
                                                Discard += [Sh]
                                                y += 1
                                                print()
                                                print("AI played " + Sh + "!")
                                                print()

                                        if len(Deck) < 9:
                                            if Sk in P2:
                                                print()
                                                print("The AI skip its turn!")
                                                print()
                                                P2.remove(Sk)
                                                break
                                            else:
                                                print("AI does not play a card!")
                                                print()
                                                drawC(Deck, P2)
                                                if P2[(len(P2))-1] == EK:
                                                    if aiexplode(P2, Deck, Discard) == False:
                                                        return 0
                                                    else:
                                                        pass
                                                break

                                        if len(Deck) < 19:
                                            if F in P2:
                                                print()
                                                print("AI played " + F + "!")
                                                print()
                                                favor(P1, P2)
                                                P2.remove(F)
                                                Discard += [F]
                                            elif P2.count(Ct) >= 2 or P2.count(Cw) >= 2 or P2.count(Cp) >= 2 or P2.count(Cb) >= 2 or P2.count(Cr) >= 2:
                                                choice = []
                                                if P2.count(Ct) >= 2:
                                                    choice += [Ct]
                                                if P2.count(Cw) >= 2:
                                                    choice += [Cw]
                                                if P2.count(Cp) >= 2:
                                                    choice += [Cp]
                                                if P2.count(Cb) >= 2:
                                                    choice += [Cb]
                                                if P2.count(Cr) >= 2:
                                                    choice += [Cr]
                                                cardUse = random.choice(range(len(choice)))
                                                CardTOK = choice[cardUse]
                                                P2.remove(CardTOK)
                                                P2.remove(CardTOK)
                                                print("AI played Two of A Kind of " + CardTOK + "!")
                                                AiOAK(P2, P1)
                                                Discard += 2*[CardTOK] 
                                            elif Se in P2:
                                                S = sTF(Deck, P2, Discard)
                                                print()
                                                print("AI played " + Se + "!")
                                                print()
                                                if S[0] == EK:
                                                    if Sk in P2:
                                                        print()
                                                        print("The AI skip its turn!")
                                                        print()
                                                        P2.remove(Sk)
                                                        break
                                                    elif Sh in P2:
                                                        print()
                                                        print("The AI shuffles the deck!")
                                                        print()
                                                        P2.remove(Sh)
                                                        shuffle(Deck)        
                                                    else: 
                                                        print()
                                                        print("AI says oh oh")
                                                        print()
                                            else:
                                                print("AI does not play a card!")
                                                print()
                                                drawC(Deck, P2)
                                                if P2[(len(P2))-1] == EK:
                                                    if aiexplode(P2, Deck, Discard) == False:
                                                        return 0
                                                    else:
                                                        pass
                                                break
                                        else:
                                            print("AI does not play a card!")
                                            print()
                                            drawC(Deck, P2)
                                            if P2[(len(P2))-1] == EK:
                                                if aiexplode(P2, Deck, Discard) == False:
                                                    return 0
                                                else:
                                                    pass
                                            break
                            break        
                            
                            
                        PCA = input("Do you want to play another card? (Y or N): ")
                        if PCA == "Y":
                            pass
                        if PCA == "N":
                            drawC(Deck, P1)
                            if P1[(len(P1))-1] == EK:
                                if explode(P1, Deck, Discard) == False:
                                    return 0
                                else:
                                    x += 1
                                    pass
                            break
                else:
                    return "ERROR"
                break

#### Bots Turn

        elif Turn%2 == 0:
            while n == 0:
                if P2 == []:
                    print("AI does not play a card!")
                    print()
                    drawC(Deck, P2)
                    if P2[(len(P2))-1] == EK:
                        if aiexplode(P2, Deck, Discard) == False:
                            return 0
                        else:
                            pass
                    break
                if P2 != []:
                    if x > y:
                        if Sh in P2:
                            shuffle(Deck)
                            P2.remove(Sh)
                            Discard += [Sh]
                            y += 1
                            print()
                            print("AI played " + Sh + "!")
                            print()

                    if len(Deck) < 9:
                        if A in P2:
                            P2.remove(A)
                            Discard += [A]
                            print()
                            print("The Ai plays an attatck card!")
                            print("You will now have two turns")
                            print()
                            for x in range(1):
                                while n == 0:
                                    print(P1)
                                    print()
                                    PC = input("Do you want to play a card? (Y or N): ")
                                    if PC == "N":
                                        drawC(Deck, P1)
                                        if P1[(len(P1))-1] == EK:
                                            if explode(P1, Deck, Discard) == False:
                                                return 0
                                            else:
                                                x += 1
                                                pass
                                        break
                                    elif PC == "Y":
                                        while n == 0:
                                            print(P1)
                                            print()
                                            CardL = int(input("What is the the numerical position of the card you want to play (Not Attack Card): "))
                                            Card = P1[CardL-1]
                                            print(Card)
                                            if Card == D:
                                                print("Error. Cannot be played")
                                                print()
                                            if Card == Sk:
                                                skip(CardL, P1, Discard)                      
                                                break
                                            if Card == Sh:
                                                shuffle(Deck)
                                                Discard += [Card]
                                                P1.pop(CardL-1)
                                            if Card == Ct or Card == Cw or Card == Cp or Card == Cb or Card == Cr:
                                                P1.remove(Card)
                                                if Card in P1:
                                                    print("You played two of a kind!")
                                                    print()
                                                    Discard += 2*[Card]
                                                    P1.remove(Card)
                                                    twoOAK(P1, P2)
                                                else:
                                                    print("You do not have tow of a kind!")
                                                    print()
                                                    P1 += [Card]
                                            if Card == F:
                                                aifavor(P1,P2)
                                                P1.pop(CardL-1)
                                                Discard += Card
                                            if Card == Se:
                                                S = sTF(Deck, P1, Discard)
                                                print("Next Three Cards Are: ")
                                                print()
                                                print(S)
                                                print()
                                            print()
                                            print()
                                            print("The bot has " + str(len(P2)) + " cards")
                                            print()
                                            print(P1)
                                            print()

                                            if Card == A:
                                                return "ERROR"
                                            PCA = input("Do you want to play another card? (Y or N): ")
                                            if PCA == "Y":
                                                pass
                                            if PCA == "N":
                                                drawC(Deck, P1)
                                                if P1[(len(P1))-1] == EK:
                                                    if explode(P1, Deck, Discard) == False:
                                                        return 0
                                                    else:
                                                        x += 1
                                                        pass
                                                break
                                    else:
                                        return "ERROR"
                                    break
                            break 
                          
                        
                        elif Sk in P2:   
                            print()
                            print("The AI skip its turn!")
                            print()
                            P2.remove(Sk)
                            break
                        else:
                            print("AI does not play a card!")
                            print()
                            drawC(Deck, P2)
                            if P2[(len(P2))-1] == EK:
                                if aiexplode(P2, Deck, Discard) == False:
                                    return 0
                                else:
                                    pass
                            break

                    if len(Deck) < 19:
                        if F in P2:
                            print()
                            print("AI played " + F + "!")
                            print()
                            favor(P1, P2)
                            P2.remove(F)
                            Discard += [F]
                        elif P2.count(Ct) >= 2 or P2.count(Cw) >= 2 or P2.count(Cp) >= 2 or P2.count(Cb) >= 2 or P2.count(Cr) >= 2:
                            choice = []
                            if P2.count(Ct) >= 2:
                                choice += [Ct]
                            if P2.count(Cw) >= 2:
                                choice += [Cw]
                            if P2.count(Cp) >= 2:
                                choice += [Cp]
                            if P2.count(Cb) >= 2:
                                choice += [Cb]
                            if P2.count(Cr) >= 2:
                                choice += [Cr]
                            cardUse = random.choice(range(len(choice)))
                            CardTOK = choice[cardUse]
                            P2.remove(CardTOK)
                            P2.remove(CardTOK)
                            print("AI played Two of A Kind of " + CardTOK + "!")
                            AiOAK(P2, P1)
                            Discard += 2*[CardTOK] 
                        elif Se in P2:
                            S = sTF(Deck, P2, Discard)
                            print()
                            print("AI played " + Se + "!")
                            print()
                            if S[0] == EK:
                                if Sk in P2:
                                    print()
                                    print("The AI skip its turn!")
                                    print()
                                    P2.remove(Sk)
                                    break
                                elif Sh in P2:
                                    print()
                                    print("The AI shuffles the deck!")
                                    print()
                                    P2.remove(Sh)
                                    shuffle(Deck)
                                elif A in P2:
                                    P2.remove(A)
                                    Discard += [A]
                                    print()
                                    print("The Ai plays an attatck card!")
                                    print("You will now have two turns")
                                    print()
                                    for x in range(1):
                                        while n == 0:
                                            print(P1)
                                            print()
                                            PC = input("Do you want to play a card? (Y or N): ")
                                            if PC == "N":
                                                drawC(Deck, P1)
                                                if P1[(len(P1))-1] == EK:
                                                    if explode(P1, Deck, Discard) == False:
                                                        return 0
                                                    else:
                                                        x += 1
                                                        pass
                                                break
                                            elif PC == "Y":
                                                while n == 0:
                                                    print(P1)
                                                    print()
                                                    CardL = int(input("What is the the numerical position of the card you want to play (Not Attack Card): "))
                                                    Card = P1[CardL-1]
                                                    print(Card)
                                                    if Card == D:
                                                        print("Error. Cannot be played")
                                                        print()
                                                    if Card == Sk:
                                                        skip(CardL, P1, Discard)                      
                                                        break
                                                    if Card == Sh:
                                                        shuffle(Deck)
                                                        Discard += [Card]
                                                        P1.pop(CardL-1)
                                                    if Card == Ct or Card == Cw or Card == Cp or Card == Cb or Card == Cr:
                                                        P1.remove(Card)
                                                        if Card in P1:
                                                            print("You played two of a kind!")
                                                            print()
                                                            Discard += 2*[Card]
                                                            P1.remove(Card)
                                                            twoOAK(P1, P2)
                                                        else:
                                                            print("You do not have tow of a kind!")
                                                            print()
                                                            P1 += [Card]
                                                    if Card == F:
                                                        aifavor(P1,P2)
                                                        P1.pop(CardL-1)
                                                        Discard += Card
                                                    if Card == Se:
                                                        S = sTF(Deck, P1, Discard)
                                                        print("Next Three Cards Are: ")
                                                        print()
                                                        print(S)
                                                        print()
                                                    print()
                                                    print()
                                                    print("The bot has " + str(len(P2)) + " cards")
                                                    print()
                                                    print(P1)
                                                    print()

                                                    if Card == A:
                                                        return "ERROR"
                                                    PCA = input("Do you want to play another card? (Y or N): ")
                                                    if PCA == "Y":
                                                        pass
                                                    if PCA == "N":
                                                        drawC(Deck, P1)
                                                        if P1[(len(P1))-1] == EK:
                                                            if explode(P1, Deck, Discard) == False:
                                                                return 0
                                                            else:
                                                                x += 1
                                                                pass
                                                        break
                                            else:
                                                return "ERROR"
                                            break
                                    break        
                                else: 
                                    print()
                                    print("AI says oh oh")
                                    print()
                        else:
                            print("AI does not play a card!")
                            print()
                            drawC(Deck, P2)
                            if P2[(len(P2))-1] == EK:
                                if aiexplode(P2, Deck, Discard) == False:
                                    return 0
                                else:
                                    pass
                            break
                    else:
                        print("AI does not play a card!")
                        print()
                        drawC(Deck, P2)
                        if P2[(len(P2))-1] == EK:
                            if aiexplode(P2, Deck, Discard) == False:
                                return 0
                            else:
                                pass
                        break
