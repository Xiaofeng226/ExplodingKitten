# Exploding Kitten 💣🐱

A Python implementation of the popular card game "Exploding Kittens" - a strategic, kitty-powered version of Russian Roulette where players take turns drawing cards until someone draws an exploding kitten and loses the game.

## 🎮 About The Game

Exploding Kittens is a highly strategic, card-based game where players draw cards from a deck until someone draws an Exploding Kitten card. The objective is to be the last player standing by using various action cards to avoid drawing the deadly Exploding Kitten or to force other players to draw one.

## 🃏 Game Rules

### Setup
- You and an AI goes for a face-off!
- The deck contains various action cards and Exploding Kitten cards
- Remove Exploding Kittens from the deck, then insert 1 fewer Exploding Kitten than the number of players

### Gameplay
1. Players take turns clockwise
2. On your turn, you can play as many action cards as you want (or none)
3. At the end of your turn, draw a card from the deck
4. If you draw an Exploding Kitten and don't have a Defuse card, you're eliminated
5. If you have a Defuse card, you can use it to neutralize the Exploding Kitten and secretly place it back in the deck
6. The last player remaining wins!

### Card Types
- **Exploding Kitten**: Eliminates you from the game unless defused
- **Defuse**: Neutralizes an Exploding Kitten
- **Attack**: Forces the next player to take 2 turns
- **Skip**: Ends your turn without drawing
- **Favor**: Ask another player for a card
- **Shuffle**: Shuffles the deck
- **See the Future**: View the top cards of the deck
- **Cat Cards**: Collect pairs to steal cards from opponents

## 🚀 Getting Started

### Prerequisites
- Python 3.x

### Installation
```bash
# Clone the repository
git clone https://github.com/Xiaofeng226/ExplodingKitten.git

# Navigate to the project directory
cd ExplodingKitten
```

### Running the Game
```bash
python final.py
```

## 💻 Technical Details

This is a command-line implementation of Exploding Kittens built with Python. The game includes:
- Turn-based gameplay mechanics
- Card management system
- Player elimination logic
- Interactive command-line interface

## 🎯 Features

- Against AI    
- All core card types and actions in the original set except for the card nope
- Strategic gameplay with card effects
- Randomized deck shuffling
- Turn-based mechanics

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Add more cards types to your liking!!!!

## 📝 License

This project is an educational implementation of the Exploding Kittens game concept. Please note that "Exploding Kittens" is a trademark of Exploding Kittens LLC.

## 🎲 Acknowledgments

- Original game created by Elan Lee and Matthew Inman (The Oatmeal)
- Inspired by the award-winning card game that became the most-backed project in Kickstarter history

## 📧 Contact

Project Link: [https://github.com/Xiaofeng226/ExplodingKitten](https://github.com/Xiaofeng226/ExplodingKitten)

---

**Have fun and may the odds be ever in your favor! 🎉**