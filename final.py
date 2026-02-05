# Name: Xiaofeng Li
# File: final.py
#
#
import random
#  CARD DEFINITIONS


# Card names
EK = "Exploding Kitten"
D = "Defuse Card"
A = "Attack Card"
F = "Favor Card"
N = "Nope Card"
Sh = "Shuffle Card"
Sk = "Skip Card"
Se = "See the Future Card"
Ct = "Taco Cat"
Cw = "Watermelon Cat"
Cp = "Potato Cat"
Cb = "Beard Cat"
Cr = "Rainbow Cat"

# Card descriptions
CARD_DESCRIPTIONS = {
    EK: "You must show this card immediately. Unless you have a Defuse, you're dead. "
        "When you die, put the kitten that killed you face up in front of you so that "
        "everyone can see that you're dead, and the rest of your cards face down in front of you.",
    
    D: "If you drew an Exploding Kitten, you can play this card instead of dying. "
       "Place your Defuse in the Discard Pile. Then take the Exploding Kitten, and "
       "without reordering or viewing the other cards, secretly put it back in the "
       "Draw Pile anywhere you'd like. Your turn is over after playing this card.",
    
    A: "End your turn without drawing a card, and immediately force the next player "
       "to take 2 turns in a row. If the victim of an Attack plays this card on any "
       "of their turns, the attacks 'stack' and their turns are immediately transferred "
       "to the next player.",
    
    F: "Force any other player to give you 1 card from their hand. They choose which card to give you.",
    
    N: "Stop any action except for an Exploding Kitten or a Defuse. You can play a Nope "
       "at any time before an action has begun, even if it's not your turn.",
    
    Sh: "Shuffle the Draw Pile until the next player tells you to stop",
    
    Sk: "Immediately end your turn without drawing a card.",
    
    Se: "Privately view the top 3 cards from the Draw Pile and put them back in the same order.",
    
    "Cat": "These cards are powerless on their own, but if you collect any 2 matching Cat Cards, "
           "you can play them as a Pair to steal a random card from any player."
}

# All cat card types
CAT_CARDS = [Ct, Cw, Cp, Cb, Cr]

def create_deck() -> List[str]:
    """
    Create and return the initial game deck.
    
    Returns:
        List[str]: A list containing all game cards in their initial quantities
    """
    deck = (
        [EK] +           # 1 Exploding Kitten (more added based on player count)
        6 * [D] +        # 6 Defuse cards
        4 * [A] +        # 4 Attack cards
        4 * [F] +        # 4 Favor cards
        5 * [N] +        # 5 Nope cards
        4 * [Sh] +       # 4 Shuffle cards
        4 * [Sk] +       # 4 Skip cards
        5 * [Se] +       # 5 See the Future cards
        4 * [Ct] +       # 4 Taco Cat cards
        4 * [Cw] +       # 4 Watermelon Cat cards
        4 * [Cp] +       # 4 Potato Cat cards
        4 * [Cb] +       # 4 Beard Cat cards
        4 * [Cr]         # 4 Rainbow Cat cards
    )
    return deck

P1 = []
P2 = []
Discard = []
n = 0


def draw_card(deck: List[str], hand: List[str]) -> Optional[str]:
    """
    Draw a card from the deck and add it to the player's hand.
    
    Args:
        deck: The deck to draw from
        hand: The player's hand to add the card to
    
    Returns:
        Optional[str]: The card drawn, or None if deck is empty
    """
    if not deck:
        print("Warning: Deck is empty!")
        return None
    
    card = deck.pop(0)
    hand.append(card)
    return card




def shuffle_deck(deck: List[str]) -> List[str]:
    """
    Shuffle the deck randomly.
    
    Args:
        deck: The deck to shuffle
    
    Returns:
        List[str]: The shuffled deck
    """
    random.shuffle(deck)
    return deck

def display_hand(hand: List[str]) -> None:
    """
    Display a player's hand in a numbered, easy-to-read format.
    
    Args:
        hand: The player's hand to display
    """
    print("\n" + "="*50)
    print("YOUR HAND:")
    print("="*50)
    for i, card in enumerate(hand, 1):
        print(f"{i}. {card}")
    print("="*50 + "\n")


def get_valid_input(prompt: str, valid_options: List[str]) -> str:
    """
    Get validated input from the user.
    
    Args:
        prompt: The prompt to display to the user
        valid_options: List of valid input options
    
    Returns:
        str: A valid user input
    """
    while True:
        user_input = input(prompt).strip().upper()
        if user_input in valid_options:
            return user_input
        print(f"Invalid input. Please enter one of: {', '.join(valid_options)}")


def get_valid_number(prompt: str, min_val: int, max_val: int) -> int:
    """
    Get a valid number input from the user within a specified range.
    
    Args:
        prompt: The prompt to display
        min_val: Minimum acceptable value (inclusive)
        max_val: Maximum acceptable value (inclusive)
    
    Returns:
        int: A valid number within the specified range
    """
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"Please enter a number between {min_val} and {max_val}")
        except ValueError:
            print("Please enter a valid number")


# ==================== CARD ACTIONS ====================

def play_skip(hand: List[str], card_index: int, discard: List[str]) -> bool:
    """
    Play a skip card to end the turn without drawing.
    
    Args:
        hand: Player's hand
        card_index: Index of the skip card
        discard: Discard pile
    
    Returns:
        bool: True if successful
    """
    print("\nYou skip your turn!")
    discard.append(hand.pop(card_index))
    return True


def play_shuffle(deck: List[str], hand: List[str], card_index: int, discard: List[str]) -> bool:
    """
    Play a shuffle card to shuffle the deck.
    
    Args:
        deck: The game deck
        hand: Player's hand
        card_index: Index of the shuffle card
        discard: Discard pile
    
    Returns:
        bool: True if successful
    """
    shuffle_deck(deck)
    print("\nThe deck has been shuffled!")
    discard.append(hand.pop(card_index))
    return True


def play_see_future(deck: List[str], hand: List[str], card_index: int, discard: List[str]) -> List[str]:
    """
    Play a See the Future card to view the top 3 cards of the deck.
    
    Args:
        deck: The game deck
        hand: Player's hand
        card_index: Index of the See the Future card
        discard: Discard pile
    
    Returns:
        List[str]: The top 3 cards (or fewer if deck has less than 3)
    """
    top_cards = deck[:min(3, len(deck))]
    print("\n" + "="*50)
    print("TOP 3 CARDS IN THE DECK:")
    for i, card in enumerate(top_cards, 1):
        print(f"{i}. {card}")
    print("="*50 + "\n")
    
    discard.append(hand.pop(card_index))
    return top_cards


def play_favor(asking_hand: List[str], giving_hand: List[str], is_player: bool = True) -> bool:
    """
    Play a Favor card to take a card from another player.
    
    Args:
        asking_hand: Hand of the player asking for a card
        giving_hand: Hand of the player giving a card
        is_player: Whether the asking player is the human player
    
    Returns:
        bool: True if successful
    """
    if not giving_hand:
        print("\nOpponent has no cards! Favor wasted.")
        return False
    
    if is_player:
        # AI gives a card to player
        card = ai_choose_card_to_give(giving_hand)
        asking_hand.append(card)
        giving_hand.remove(card)
        print(f"\nAI gave you: {card}")
    else:
        # Player gives a card to AI
        print("\nYour hand:")
        display_hand(giving_hand)
        card_index = get_valid_number(
            "Enter the number of the card you want to give: ",
            1, len(giving_hand)
        ) - 1
        
        card = giving_hand.pop(card_index)
        asking_hand.append(card)
        print(f"\nYou gave AI: {card}")
    
    return True

def ai_choose_card_to_give(hand: List[str]) -> str:
    """
    AI logic to choose which card to give away when a Favor is played against it.
    Prioritizes giving away less valuable cards.
    
    Args:
        hand: AI's hand
    
    Returns:
        str: The card chosen to give away
    """
    # Priority order (give away least valuable first)
    priority = CAT_CARDS + [F, Sk, Se, A, N, Sh, D]
    
    for card_type in priority:
        if card_type in hand:
            return card_type
    
    # Fallback: give any card
    return hand[0]

def play_two_of_a_kind(playing_hand: List[str], target_hand: List[str], 
                       cat_card: str, discard: List[str], is_player: bool = True) -> bool:
    """
    Play two matching cat cards to steal a random card from opponent.
    
    Args:
        playing_hand: Hand of player playing the combo
        target_hand: Hand of the target player
        cat_card: The type of cat card being played
        discard: Discard pile
        is_player: Whether the playing player is the human player
    
    Returns:
        bool: True if successful
    """
    if target_hand:
        stolen_card = random.choice(target_hand)
        target_hand.remove(stolen_card)
        playing_hand.append(stolen_card)
        
        player_name = "You" if is_player else "AI"
        print(f"\n{player_name} stole: {stolen_card}")
        
        discard.extend([cat_card, cat_card])
        return True
    else:
        print("\nOpponent has no cards to steal!")
        return False

# Game Functions


def handle_exploding_kitten(hand: List[str], deck: List[str], 
                           discard: List[str], is_player: bool = True) -> bool:
    """
    Handle drawing an Exploding Kitten card.
    
    Args:
        hand: The player's hand
        deck: The game deck
        discard: Discard pile
        is_player: Whether this is the human player
    
    Returns:
        bool: True if player survived, False if eliminated
    """
    player_name = "You" if is_player else "AI"
    
    print(f"\n{'!'*50}")
    print(f"{player_name} drew an EXPLODING KITTEN!")
    print(f"{'!'*50}\n")
    
    if D in hand:
        print(f"{player_name} used a Defuse Card!")
        hand.remove(D)
        hand.remove(EK)
        discard.append(D)
        
        if is_player:
            position = get_valid_number(
                f"Where in the deck do you want to place the Exploding Kitten? (1-{len(deck) + 1}): ",
                1, len(deck) + 1
            )
            deck.insert(position - 1, EK)
        else:
            # AI places it deeper in the deck
            position = min(len(deck), random.randint(3, max(4, len(deck))))
            deck.insert(position, EK)
            print(f"AI placed the Exploding Kitten back in the deck.")
        
        print(f"{player_name} survived... for now.\n")
        return True
    else:
        print(f"\n{player_name} has no Defuse Card!")
        print(f"{player_name} EXPLODED! Game Over!")
        return False

    
def ai_should_play_card(deck: List[str], ai_hand: List[str]) -> Tuple[bool, Optional[str]]:
    """
    Determine if AI should play a card and which one.
    
    Args:
        deck: The game deck
        ai_hand: AI's hand
    
    Returns:
        Tuple[bool, Optional[str]]: (should_play, card_to_play)
    """
    deck_size = len(deck)
    
    # Always shuffle if saw an Exploding Kitten on top
    if Sh in ai_hand:
        # This would need to track if AI saw the future
        pass
    
    # Use Skip if deck is dangerous (less than 9 cards)
    if deck_size < 9 and Sk in ai_hand:
        return True, Sk
    
    # Use Attack if deck is dangerous
    if deck_size < 9 and A in ai_hand:
        return True, A
    
    # Play Favor if deck is medium risk
    if deck_size < 19 and F in ai_hand:
        return True, F
    
    # Play two of a kind if available
    for cat in CAT_CARDS:
        if ai_hand.count(cat) >= 2:
            return True, cat
    
    # Play See the Future to scout
    if Se in ai_hand:
        return True, Se
    
    return False, None


def ai_play_turn(ai_hand: List[str], player_hand: List[str], 
                deck: List[str], discard: List[str]) -> bool:
    """
    Execute the AI's turn.
    
    Args:
        ai_hand: AI's hand
        player_hand: Player's hand
        deck: Game deck
        discard: Discard pile
    
    Returns:
        bool: True if AI survived the turn
    """
    print("\n" + "="*50)
    print("AI's Turn")
    print("="*50)
    
    # AI decision making
    should_play, card = ai_should_play_card(deck, ai_hand)
    
    if should_play and card:
        if card == Sk:
            print("AI plays Skip!")
            ai_hand.remove(Sk)
            discard.append(Sk)
            return True
        
        elif card == Sh:
            print("AI plays Shuffle!")
            play_shuffle(deck, ai_hand, ai_hand.index(Sh), discard)
        
        elif card == Se:
            print("AI plays See the Future!")
            top_cards = play_see_future(deck, ai_hand, ai_hand.index(Se), discard)
            # AI could make decisions based on what it sees
            if top_cards and top_cards[0] == EK:
                print("AI sees danger ahead!")
                # Try to play Skip or Shuffle if available
                if Sk in ai_hand:
                    print("AI plays Skip to avoid danger!")
                    ai_hand.remove(Sk)
                    discard.append(Sk)
                    return True
                elif Sh in ai_hand:
                    print("AI plays Shuffle to avoid danger!")
                    play_shuffle(deck, ai_hand, ai_hand.index(Sh), discard)
        
        elif card == F:
            print("AI plays Favor!")
            play_favor(ai_hand, player_hand, is_player=False)
            ai_hand.remove(F)
            discard.append(F)
        
        elif card == A:
            print("AI plays Attack!")
            ai_hand.remove(A)
            discard.append(A)
            return True  # Attack handled separately
        
        elif card in CAT_CARDS and ai_hand.count(card) >= 2:
            print(f"AI plays Two of a Kind: {card}!")
            ai_hand.remove(card)
            ai_hand.remove(card)
            play_two_of_a_kind(ai_hand, player_hand, card, discard, is_player=False)
    
    # Draw a card
    print("\nAI draws a card...")
    drawn_card = draw_card(deck, ai_hand)
    
    if drawn_card == EK:
        return handle_exploding_kitten(ai_hand, deck, discard, is_player=False)
    
    print(f"AI now has {len(ai_hand)} cards.")
    return True
        


# def hostGame(P1, P2, Deck, Discard):
#     """Hosts a game of exploding kittens 
#     """
#     shuffle(Deck)
#     for x in range(6):
#         Deck.remove(D)
#     Deck.remove(EK)
#     P1 += [D]
#     P2 += [D]
#     for x in range(5):
#         drawC(Deck, P1)
#     for x in range(5):
#         drawC(Deck, P2)
#     Deck += 4*[D] + [EK]
#     #shuffle(Deck)
#     Turn = 0
#     x = 1
#     y = x
    
#     while checkLost(P1) == False and checkLost(P2) == False:
#         Turn += 1
#         n = 0
#         if Turn%2 == 1:
#             while n == 0:
#                 print(P1)
#                 print()
#                 PC = input("Do you want to play a card? (Y or N): ")
#                 if PC == "N":
#                     drawC(Deck, P1)
#                     if P1[(len(P1))-1] == EK:
#                         if explode(P1, Deck, Discard) == False:
#                             return 0
#                         else:
#                             x += 1
#                             pass
#                     break
#                 elif PC == "Y":
#                     while n == 0:
#                         print(P1)
#                         print()
#                         CardL = int(input("What is the the numerical position of the card you want to play: "))
#                         Card = P1[CardL-1]
#                         print(Card)
#                         if Card == D:
#                             print("Error. Cannot be played")
#                             print()
#                         if Card == Sk:
#                             skip(CardL, P1, Discard)                      
#                             break
#                         if Card == Sh:
#                             shuffle(Deck)
#                             Discard += [Card]
#                             P1.pop(CardL-1)
#                         if Card == Ct or Card == Cw or Card == Cp or Card == Cb or Card == Cr:
#                             P1.remove(Card)
#                             if Card in P1:
#                                 print("You played two of a kind!")
#                                 print()
#                                 Discard += 2*[Card]
#                                 P1.remove(Card)
#                                 twoOAK(P1, P2)
#                             else:
#                                 print("You do not have two of a kind!")
#                                 print()
#                                 P1 += [Card]
#                         if Card == F:
#                             aifavor(P1,P2)
#                             P1.pop(CardL-1)
#                             Discard += Card
#                         if Card == Se:
#                             S = sTF(Deck, P1, Discard)
#                             print("Next Three Cards Are: ")
#                             print()
#                             print(S)
#                             print()
#                         print()
#                         print()
#                         print("The bot has " + str(len(P2)) + " cards")
#                         print()
#                         print(P1)
#                         print()

#                         if Card == A:
#                             P1.remove(A)
#                             Discard += [A]
#                             print()
#                             print("You play an attatck card!")
#                             print("AI will now have two turns")
#                             print()
#                             for x in range(1):   
#                                 while n == 0:
#                                     if P2 == []:
#                                         print("AI does not play a card!")
#                                         print()
#                                         drawC(Deck, P2)
#                                         if P2[(len(P2))-1] == EK:
#                                             if aiexplode(P2, Deck, Discard) == False:
#                                                 return 0
#                                             else:
#                                                 pass
#                                         break
#                                     if P2 != []:
#                                         if x > y:
#                                             if Sh in P2:
#                                                 shuffle(Deck)
#                                                 P2.remove(Sh)
#                                                 Discard += [Sh]
#                                                 y += 1
#                                                 print()
#                                                 print("AI played " + Sh + "!")
#                                                 print()

#                                         if len(Deck) < 9:
#                                             if Sk in P2:
#                                                 print()
#                                                 print("The AI skip its turn!")
#                                                 print()
#                                                 P2.remove(Sk)
#                                                 break
#                                             else:
#                                                 print("AI does not play a card!")
#                                                 print()
#                                                 drawC(Deck, P2)
#                                                 if P2[(len(P2))-1] == EK:
#                                                     if aiexplode(P2, Deck, Discard) == False:
#                                                         return 0
#                                                     else:
#                                                         pass
#                                                 break

#                                         if len(Deck) < 19:
#                                             if F in P2:
#                                                 print()
#                                                 print("AI played " + F + "!")
#                                                 print()
#                                                 favor(P1, P2)
#                                                 P2.remove(F)
#                                                 Discard += [F]
#                                             elif P2.count(Ct) >= 2 or P2.count(Cw) >= 2 or P2.count(Cp) >= 2 or P2.count(Cb) >= 2 or P2.count(Cr) >= 2:
#                                                 choice = []
#                                                 if P2.count(Ct) >= 2:
#                                                     choice += [Ct]
#                                                 if P2.count(Cw) >= 2:
#                                                     choice += [Cw]
#                                                 if P2.count(Cp) >= 2:
#                                                     choice += [Cp]
#                                                 if P2.count(Cb) >= 2:
#                                                     choice += [Cb]
#                                                 if P2.count(Cr) >= 2:
#                                                     choice += [Cr]
#                                                 cardUse = random.choice(range(len(choice)))
#                                                 CardTOK = choice[cardUse]
#                                                 P2.remove(CardTOK)
#                                                 P2.remove(CardTOK)
#                                                 print("AI played Two of A Kind of " + CardTOK + "!")
#                                                 AiOAK(P2, P1)
#                                                 Discard += 2*[CardTOK] 
#                                             elif Se in P2:
#                                                 S = sTF(Deck, P2, Discard)
#                                                 print()
#                                                 print("AI played " + Se + "!")
#                                                 print()
#                                                 if S[0] == EK:
#                                                     if Sk in P2:
#                                                         print()
#                                                         print("The AI skip its turn!")
#                                                         print()
#                                                         P2.remove(Sk)
#                                                         break
#                                                     elif Sh in P2:
#                                                         print()
#                                                         print("The AI shuffles the deck!")
#                                                         print()
#                                                         P2.remove(Sh)
#                                                         shuffle(Deck)        
#                                                     else: 
#                                                         print()
#                                                         print("AI says oh oh")
#                                                         print()
#                                             else:
#                                                 print("AI does not play a card!")
#                                                 print()
#                                                 drawC(Deck, P2)
#                                                 if P2[(len(P2))-1] == EK:
#                                                     if aiexplode(P2, Deck, Discard) == False:
#                                                         return 0
#                                                     else:
#                                                         pass
#                                                 break
#                                         else:
#                                             print("AI does not play a card!")
#                                             print()
#                                             drawC(Deck, P2)
#                                             if P2[(len(P2))-1] == EK:
#                                                 if aiexplode(P2, Deck, Discard) == False:
#                                                     return 0
#                                                 else:
#                                                     pass
#                                             break
#                             break        
                            
                            
#                         PCA = input("Do you want to play another card? (Y or N): ")
#                         if PCA == "Y":
#                             pass
#                         if PCA == "N":
#                             drawC(Deck, P1)
#                             if P1[(len(P1))-1] == EK:
#                                 if explode(P1, Deck, Discard) == False:
#                                     return 0
#                                 else:
#                                     x += 1
#                                     pass
#                             break
#                 else:
#                     return "ERROR"
#                 break

# #### Bots Turn

#         elif Turn%2 == 0:
#             while n == 0:
#                 if P2 == []:
#                     print("AI does not play a card!")
#                     print()
#                     drawC(Deck, P2)
#                     if P2[(len(P2))-1] == EK:
#                         if aiexplode(P2, Deck, Discard) == False:
#                             return 0
#                         else:
#                             pass
#                     break
#                 if P2 != []:
#                     if x > y:
#                         if Sh in P2:
#                             shuffle(Deck)
#                             P2.remove(Sh)
#                             Discard += [Sh]
#                             y += 1
#                             print()
#                             print("AI played " + Sh + "!")
#                             print()

#                     if len(Deck) < 9:
#                         if A in P2:
#                             P2.remove(A)
#                             Discard += [A]
#                             print()
#                             print("The Ai plays an attatck card!")
#                             print("You will now have two turns")
#                             print()
#                             for x in range(1):
#                                 while n == 0:
#                                     print(P1)
#                                     print()
#                                     PC = input("Do you want to play a card? (Y or N): ")
#                                     if PC == "N":
#                                         drawC(Deck, P1)
#                                         if P1[(len(P1))-1] == EK:
#                                             if explode(P1, Deck, Discard) == False:
#                                                 return 0
#                                             else:
#                                                 x += 1
#                                                 pass
#                                         break
#                                     elif PC == "Y":
#                                         while n == 0:
#                                             print(P1)
#                                             print()
#                                             CardL = int(input("What is the the numerical position of the card you want to play (Not Attack Card): "))
#                                             Card = P1[CardL-1]
#                                             print(Card)
#                                             if Card == D:
#                                                 print("Error. Cannot be played")
#                                                 print()
#                                             if Card == Sk:
#                                                 skip(CardL, P1, Discard)                      
#                                                 break
#                                             if Card == Sh:
#                                                 shuffle(Deck)
#                                                 Discard += [Card]
#                                                 P1.pop(CardL-1)
#                                             if Card == Ct or Card == Cw or Card == Cp or Card == Cb or Card == Cr:
#                                                 P1.remove(Card)
#                                                 if Card in P1:
#                                                     print("You played two of a kind!")
#                                                     print()
#                                                     Discard += 2*[Card]
#                                                     P1.remove(Card)
#                                                     twoOAK(P1, P2)
#                                                 else:
#                                                     print("You do not have tow of a kind!")
#                                                     print()
#                                                     P1 += [Card]
#                                             if Card == F:
#                                                 aifavor(P1,P2)
#                                                 P1.pop(CardL-1)
#                                                 Discard += Card
#                                             if Card == Se:
#                                                 S = sTF(Deck, P1, Discard)
#                                                 print("Next Three Cards Are: ")
#                                                 print()
#                                                 print(S)
#                                                 print()
#                                             print()
#                                             print()
#                                             print("The bot has " + str(len(P2)) + " cards")
#                                             print()
#                                             print(P1)
#                                             print()

#                                             if Card == A:
#                                                 return "ERROR"
#                                             PCA = input("Do you want to play another card? (Y or N): ")
#                                             if PCA == "Y":
#                                                 pass
#                                             if PCA == "N":
#                                                 drawC(Deck, P1)
#                                                 if P1[(len(P1))-1] == EK:
#                                                     if explode(P1, Deck, Discard) == False:
#                                                         return 0
#                                                     else:
#                                                         x += 1
#                                                         pass
#                                                 break
#                                     else:
#                                         return "ERROR"
#                                     break
#                             break 
                          
                        
#                         elif Sk in P2:   
#                             print()
#                             print("The AI skip its turn!")
#                             print()
#                             P2.remove(Sk)
#                             break
#                         else:
#                             print("AI does not play a card!")
#                             print()
#                             drawC(Deck, P2)
#                             if P2[(len(P2))-1] == EK:
#                                 if aiexplode(P2, Deck, Discard) == False:
#                                     return 0
#                                 else:
#                                     pass
#                             break

#                     if len(Deck) < 19:
#                         if F in P2:
#                             print()
#                             print("AI played " + F + "!")
#                             print()
#                             favor(P1, P2)
#                             P2.remove(F)
#                             Discard += [F]
#                         elif P2.count(Ct) >= 2 or P2.count(Cw) >= 2 or P2.count(Cp) >= 2 or P2.count(Cb) >= 2 or P2.count(Cr) >= 2:
#                             choice = []
#                             if P2.count(Ct) >= 2:
#                                 choice += [Ct]
#                             if P2.count(Cw) >= 2:
#                                 choice += [Cw]
#                             if P2.count(Cp) >= 2:
#                                 choice += [Cp]
#                             if P2.count(Cb) >= 2:
#                                 choice += [Cb]
#                             if P2.count(Cr) >= 2:
#                                 choice += [Cr]
#                             cardUse = random.choice(range(len(choice)))
#                             CardTOK = choice[cardUse]
#                             P2.remove(CardTOK)
#                             P2.remove(CardTOK)
#                             print("AI played Two of A Kind of " + CardTOK + "!")
#                             AiOAK(P2, P1)
#                             Discard += 2*[CardTOK] 
#                         elif Se in P2:
#                             S = sTF(Deck, P2, Discard)
#                             print()
#                             print("AI played " + Se + "!")
#                             print()
#                             if S[0] == EK:
#                                 if Sk in P2:
#                                     print()
#                                     print("The AI skip its turn!")
#                                     print()
#                                     P2.remove(Sk)
#                                     break
#                                 elif Sh in P2:
#                                     print()
#                                     print("The AI shuffles the deck!")
#                                     print()
#                                     P2.remove(Sh)
#                                     shuffle(Deck)
#                                 elif A in P2:
#                                     P2.remove(A)
#                                     Discard += [A]
#                                     print()
#                                     print("The Ai plays an attatck card!")
#                                     print("You will now have two turns")
#                                     print()
#                                     for x in range(1):
#                                         while n == 0:
#                                             print(P1)
#                                             print()
#                                             PC = input("Do you want to play a card? (Y or N): ")
#                                             if PC == "N":
#                                                 drawC(Deck, P1)
#                                                 if P1[(len(P1))-1] == EK:
#                                                     if explode(P1, Deck, Discard) == False:
#                                                         return 0
#                                                     else:
#                                                         x += 1
#                                                         pass
#                                                 break
#                                             elif PC == "Y":
#                                                 while n == 0:
#                                                     print(P1)
#                                                     print()
#                                                     CardL = int(input("What is the the numerical position of the card you want to play (Not Attack Card): "))
#                                                     Card = P1[CardL-1]
#                                                     print(Card)
#                                                     if Card == D:
#                                                         print("Error. Cannot be played")
#                                                         print()
#                                                     if Card == Sk:
#                                                         skip(CardL, P1, Discard)                      
#                                                         break
#                                                     if Card == Sh:
#                                                         shuffle(Deck)
#                                                         Discard += [Card]
#                                                         P1.pop(CardL-1)
#                                                     if Card == Ct or Card == Cw or Card == Cp or Card == Cb or Card == Cr:
#                                                         P1.remove(Card)
#                                                         if Card in P1:
#                                                             print("You played two of a kind!")
#                                                             print()
#                                                             Discard += 2*[Card]
#                                                             P1.remove(Card)
#                                                             twoOAK(P1, P2)
#                                                         else:
#                                                             print("You do not have tow of a kind!")
#                                                             print()
#                                                             P1 += [Card]
#                                                     if Card == F:
#                                                         aifavor(P1,P2)
#                                                         P1.pop(CardL-1)
#                                                         Discard += Card
#                                                     if Card == Se:
#                                                         S = sTF(Deck, P1, Discard)
#                                                         print("Next Three Cards Are: ")
#                                                         print()
#                                                         print(S)
#                                                         print()
#                                                     print()
#                                                     print()
#                                                     print("The bot has " + str(len(P2)) + " cards")
#                                                     print()
#                                                     print(P1)
#                                                     print()

#                                                     if Card == A:
#                                                         return "ERROR"
#                                                     PCA = input("Do you want to play another card? (Y or N): ")
#                                                     if PCA == "Y":
#                                                         pass
#                                                     if PCA == "N":
#                                                         drawC(Deck, P1)
#                                                         if P1[(len(P1))-1] == EK:
#                                                             if explode(P1, Deck, Discard) == False:
#                                                                 return 0
#                                                             else:
#                                                                 x += 1
#                                                                 pass
#                                                         break
#                                             else:
#                                                 return "ERROR"
#                                             break
#                                     break        
#                                 else: 
#                                     print()
#                                     print("AI says oh oh")
#                                     print()
#                         else:
#                             print("AI does not play a card!")
#                             print()
#                             drawC(Deck, P2)
#                             if P2[(len(P2))-1] == EK:
#                                 if aiexplode(P2, Deck, Discard) == False:
#                                     return 0
#                                 else:
#                                     pass
#                             break
#                     else:
#                         print("AI does not play a card!")
#                         print()
#                         drawC(Deck, P2)
#                         if P2[(len(P2))-1] == EK:
#                             if aiexplode(P2, Deck, Discard) == False:
#                                 return 0
#                             else:
#                                 pass
#                         break
