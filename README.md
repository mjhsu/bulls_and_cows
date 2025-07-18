# 🐂🐄 Bulls & Cows - The Number Guessing Game

![Bulls & Cows Banner](https://img.shields.io/badge/Bulls%20%26%20Cows-Python-blueviolet?style=for-the-badge)

A modern, fun, and challenging command-line implementation of the classic Bulls & Cows game, featuring:
- Player and Computer Solver modes
- Unique or repeated digits
- Multiple difficulty levels
- Hangman-style lives with visual feedback
- ASCII art, hearts, and a friendly UI

---

## 🎮 Features
- **Two Game Modes:**
  - Player guesses the computer's number
  - Computer guesses your number (you provide feedback!)
- **Difficulty Levels:** Easy (3 digits), Medium (4), Hard (5), Expert (6)
- **Unique or Repeated Digits:** Choose your challenge
- **Hangman Life System:** Lose a life for each wrong guess, with hearts and a hangman/"death" display
- **ASCII Art & History:** Beautiful title, guess history, and fun win/lose screens
- **Open Source & Easy to Run**

---

## 🚀 Quick Start

1. **Clone the repo:**
   ```bash
   git clone https://github.com/mjhsu/bulls_and_cows.git
   cd bulls_and_cows
   ```
2. **Run the game:**
   ```bash
   python bulls_and_cows.py
   # or
   py bulls_and_cows.py
   ```

---

## 🖥️ Screenshots

```
╔═══════════════════════════════════════════════╗
║                                               ║
║   ██████╗ ██╗   ██╗██╗     ██╗     ███████╗   ║
║   ... (ASCII art title) ...                   ║
║                                               ║
╚═══════════════════════════════════════════════╝

Welcome to Bulls & Cows - The Number Guessing Game!
=================================================

📋 GAME RULES:
1. The computer will generate a random number.
2. You need to guess this number.
3. After each guess, you'll receive feedback:
   - 🐂 Bulls: Digits that are correct and in the correct position.
   - 🐄 Cows: Digits that are correct but in the wrong position.
4. The game continues until you guess the correct number (all bulls).

Lives: ♥♥♥♥♥♥♥  [███████░░░░░░░░░░░░░░░░] 7/7

📜 GUESS HISTORY:
╔════════╦═══════╦═══════╗
║ Guess  ║ Bulls ║ Cows  ║
╠════════╬═══════╬═══════╣
║ 123    ║   1   ║   2   ║
╚════════╩═══════╩═══════╝
```

---

## 🧑‍💻 How to Play
- **Choose your mode:** Player or Computer Solver
- **Pick difficulty and digit rules**
- **Guess the number or provide feedback**
- **Try to win before the hangman dies!**

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License
MIT License

---

## ⭐️ Star This Repo
If you like this project, please give it a star on GitHub!

---

## 🙏 Acknowledgements
- Inspired by the classic pen-and-paper game
- ASCII art and UI by [mjhsu](https://github.com/mjhsu)

---

Enjoy the game and happy guessing! 🐂🐄
