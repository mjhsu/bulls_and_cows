import random
import os

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_number(length, allow_repeats=False):
    """Generate a random number of specified length."""
    if allow_repeats:
        if length > 1:
            first_digit = random.randint(1, 9)
            rest_digits = [random.randint(0, 9) for _ in range(length - 1)]
            return str(first_digit) + ''.join(map(str, rest_digits))
        else:
            return str(random.randint(0, 9))
    else:
        digits = list(range(10))
        random.shuffle(digits)
        if length > 1 and digits[0] == 0:
            for i in range(1, 10):
                if digits[i] != 0:
                    digits[0], digits[i] = digits[i], digits[0]
                    break
        return ''.join(map(str, digits[:length]))

def calculate_bulls_and_cows(secret, guess):
    """Calculate the number of bulls and cows."""
    bulls = sum(guess[i] == secret[i] for i in range(len(secret)))
    cows = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - bulls
    return bulls, cows

def display_title():
    title = """
    ╔═══════════════════════════════════════════════╗
    ║                                               ║
    ║   ██████╗ ██╗   ██╗██╗     ██╗     ███████╗   ║
    ║   ██╔══██╗██║   ██║██║     ██║     ██╔════╝   ║
    ║   ██████╔╝██║   ██║██║     ██║     ███████╗   ║
    ║   ██╔══██╗██║   ██║██║     ██║     ╚════██║   ║
    ║   ██████╔╝╚██████╔╝███████╗███████╗███████║   ║
    ║   ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝   ║
    ║                                               ║
    ║      ██╗      ██████╗ ██████╗ ██╗    ██╗███████╗      ║
    ║     ██╔╝     ██╔════╝██╔═══██╗██║    ██║██╔════╝      ║
    ║    ██╔╝█████╗██║     ██║   ██║██║ █╗ ██║███████╗      ║
    ║   ██╔╝ ╚════╝██║     ██║   ██║██║███╗██║╚════██║      ║
    ║  ██╔╝        ╚██████╗╚██████╔╝╚███╔███╔╝███████║      ║
    ║  ╚═╝          ╚═════╝ ╚═════╝  ╚══╝╚══╝ ╚══════╝      ║
    ║                                               ║
    ╚═══════════════════════════════════════════════╝
    """
    print(title)
    print("\nWelcome to Bulls & Cows - The Number Guessing Game!")
    print("=================================================")

def display_rules():
    print("\n📋 GAME RULES:")
    print("1. The computer will generate a random number.")
    print("2. You need to guess this number.")
    print("3. After each guess, you'll receive feedback:")
    print("   - 🐂 Bulls: Digits that are correct and in the correct position.")
    print("   - 🐄 Cows: Digits that are correct but in the wrong position.")
    print("4. The game continues until you guess the correct number (all bulls).")
    print("\nExample with unique digits: If the secret number is 1234 and you guess 1325:")
    print("- You get 1 Bull (for the digit 1 in the correct position)")
    print("- You get 2 Cows (for the digits 2 and 3 in wrong positions)")
    print("\nExample with repeated digits: If the secret number is 1122 and you guess 1221:")
    print("- You get 2 Bulls (for the digits 1 and 2 in correct positions)")
    print("- You get 2 Cows (for the other 1 and 2 in wrong positions)")

def get_difficulty():
    print("\n🎮 CHOOSE DIFFICULTY:")
    print("1. Easy (3 digits)")
    print("2. Medium (4 digits)")
    print("3. Hard (5 digits)")
    print("4. Expert (6 digits)")
    while True:
        try:
            choice = input("\nEnter your choice (1-4): ")
            if choice == '1':
                return 3, "Easy"
            elif choice == '2':
                return 4, "Medium"
            elif choice == '3':
                return 5, "Hard"
            elif choice == '4':
                return 6, "Expert"
            else:
                print("❌ Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

def validate_guess(guess, length, allow_repeats=False):
    if not guess.isdigit():
        return False, "Your guess must contain only digits."
    if len(guess) != length:
        return False, f"Your guess must be {length} digits long."
    if not allow_repeats and len(set(guess)) != length:
        return False, "Your guess must contain unique digits."
    if length > 1 and guess[0] == '0':
        return False, "The first digit cannot be 0."
    return True, ""

def display_history(history):
    if not history:
        return
    print("\n📜 GUESS HISTORY:")
    print("╔════════╦═══════╦═══════╗")
    print("║ Guess  ║ Bulls ║ Cows  ║")
    print("╠════════╬═══════╬═══════╣")
    for guess, bulls, cows in history:
        print(f"║ {guess.ljust(6)} ║ {str(bulls).center(5)} ║ {str(cows).center(5)} ║")
    print("╚════════╩═══════╩═══════╝")

def get_game_mode():
    print("\n🎮 CHOOSE GAME MODE:")
    print("1. Player Guesses (You guess the computer's number)")
    print("2. Computer Solver (Computer guesses your number)")
    while True:
        try:
            choice = input("\nEnter your choice (1-2): ")
            if choice == '1':
                return 1, "Player Guesses"
            elif choice == '2':
                return 2, "Computer Solver"
            else:
                print("❌ Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

def generate_all_possible_numbers(length, allow_repeats=False):
    if allow_repeats:
        return generate_all_possible_numbers_with_repeats(length)
    else:
        return generate_all_possible_numbers_unique(length)

def generate_all_possible_numbers_unique(length):
    if length > 10:
        return []
    from itertools import permutations
    digits = list(range(10))
    possible_numbers = []
    if length > 1:
        for perm in permutations(digits, length):
            if perm[0] != 0:
                possible_numbers.append(''.join(map(str, perm)))
    else:
        for digit in digits:
            possible_numbers.append(str(digit))
    return possible_numbers

def generate_all_possible_numbers_with_repeats(length):
    possible_numbers = []
    if length == 1:
        for i in range(10):
            possible_numbers.append(str(i))
    else:
        def generate_recursive(current, remaining):
            if remaining == 0:
                possible_numbers.append(current)
                return
            start = 1 if len(current) == 0 else 0
            for digit in range(start, 10):
                generate_recursive(current + str(digit), remaining - 1)
        generate_recursive("", length)
    return possible_numbers

def filter_possible_numbers(possible_numbers, guess, bulls, cows):
    filtered = []
    for number in possible_numbers:
        calc_bulls, calc_cows = calculate_bulls_and_cows(number, guess)
        if calc_bulls == bulls and calc_cows == cows:
            filtered.append(number)
    return filtered

def get_user_feedback(guess):
    print(f"\n🤖 Computer's guess: {guess}")
    while True:
        try:
            bulls_input = input("How many bulls? ")
            bulls = int(bulls_input)
            if bulls == len(guess):
                print(f"\n🎉 COMPUTER WINS!")
                print(f"The computer guessed your number {guess}!")
                return bulls, 0
            cows_input = input("How many cows? ")
            cows = int(cows_input)
            if bulls < 0 or cows < 0:
                print("❌ Bulls and cows must be non-negative numbers.")
                continue
            if bulls + cows > len(guess):
                print(f"❌ Bulls + cows cannot exceed {len(guess)} (the length of the guess).")
                continue
            return bulls, cows
        except ValueError:
            print("❌ Please enter valid numbers.")

def get_max_lives(length):
    if length == 3:
        return 7
    elif length == 4:
        return 8
    elif length == 5:
        return 9
    elif length == 6:
        return 10
    else:
        return 7

def display_lives_hearts(lives_left, max_lives):
    heart = "♥"
    empty = "♡"
    bar_length = 20
    filled = int(bar_length * lives_left / max_lives)
    bar = "█" * filled + "░" * (bar_length - filled)
    print(f"Lives: {heart * lives_left}{empty * (max_lives - lives_left)}  [{bar}] {lives_left}/{max_lives}")

def display_hangman_dead():
    print(r"""
     +---+
     |   |
    [X]_ |
    /|\  |
    / \  |
         |
   =========
   The hangman is dead! 💀
""")

def computer_solver_mode(length, allow_repeats=False):
    print(f"\n🧠 COMPUTER SOLVER MODE")
    print(f"Think of a {length}-digit number" + (" (digits can repeat)" if allow_repeats else " (unique digits only)") + ".")
    if not allow_repeats:
        print("Make sure all digits are unique and the first digit is not 0 (for multi-digit numbers).")
    else:
        print("The first digit cannot be 0 (for multi-digit numbers).")
    print("\n🔄 Generating all possible numbers...")
    possible_numbers = generate_all_possible_numbers(length, allow_repeats)
    print(f"Generated {len(possible_numbers)} possible numbers.")

    max_lives = get_max_lives(length)
    lives_left = max_lives
    attempts = 0
    guess_history = []

    while possible_numbers and lives_left > 0:
        attempts += 1
        guess = random.choice(possible_numbers)
        bulls, cows = get_user_feedback(guess)
        guess_history.append((guess, bulls, cows))
        if bulls == length:
            print(f"The computer guessed your number in {attempts} attempts!")
            break
        possible_numbers = filter_possible_numbers(possible_numbers, guess, bulls, cows)
        print(f"\n📊 Remaining possibilities: {len(possible_numbers)}")
        display_history(guess_history)
        lives_left -= 1
        display_lives_hearts(lives_left, max_lives)
        if not possible_numbers:
            print("\n❌ No possible numbers remain!")
            print("This means the feedback was inconsistent. Please check your responses.")
            break
        if lives_left == 0:
            display_hangman_dead()
            print("Game over! The hangman died!")
            break
        if len(possible_numbers) <= 10:
            print(f"🔍 Remaining possibilities: {', '.join(possible_numbers)}")
    return attempts

def player_guess_mode(length, allow_repeats=False):
    print(f"\n🎮 PLAYER GUESS MODE")
    secret_number = generate_number(length, allow_repeats)
    print(f"I've generated a {length}-digit number" + (" (digits may repeat)" if allow_repeats else " (unique digits)") + ". Try to guess it!")
    max_lives = get_max_lives(length)
    lives_left = max_lives
    attempts = 0
    guess_history = []
    while lives_left > 0:
        attempts += 1
        guess = input(f"\nAttempt {attempts}: Enter your {length}-digit guess: ")
        is_valid, error_message = validate_guess(guess, length, allow_repeats)
        if not is_valid:
            print(f"❌ {error_message}")
            attempts -= 1
            continue
        bulls, cows = calculate_bulls_and_cows(secret_number, guess)
        guess_history.append((guess, bulls, cows))
        print(f"🐂 Bulls: {bulls}, 🐄 Cows: {cows}")
        if bulls == length:
            print(f"\n🎉 CONGRATULATIONS! You guessed the number {secret_number} in {attempts} attempts!")
            break
        print()
        display_history(guess_history)
        lives_left -= 1
        display_lives_hearts(lives_left, max_lives)
        if lives_left == 0:
            display_hangman_dead()
            print(f"\nGame over! The hangman died! The number was {secret_number}.")
            break
    return attempts

def main():
    while True:
        clear_screen()
        display_title()
        display_rules()
        mode, mode_name = get_game_mode()
        length, difficulty = get_difficulty()
        print(f"\n🔢 DIGIT REPETITION:")
        print("1. Unique digits only (traditional)")
        print("2. Allow repeated digits")
        while True:
            repeat_choice = input("\nEnter your choice (1-2): ")
            if repeat_choice == '1':
                allow_repeats = False
                break
            elif repeat_choice == '2':
                allow_repeats = True
                break
            else:
                print("❌ Invalid choice. Please enter 1 or 2.")
        clear_screen()
        print(f"🎯 Starting {mode_name} mode - {difficulty} difficulty")
        print(f"🔢 Number length: {length} digits")
        print(f"🔄 Repeated digits: {'Allowed' if allow_repeats else 'Not allowed'}")
        if mode == 1:
            attempts = player_guess_mode(length, allow_repeats)
        else:
            attempts = computer_solver_mode(length, allow_repeats)
        print(f"\n📊 Game completed in {attempts} attempts!")
        while True:
            play_again = input("\nWould you like to play again? (y/n): ").lower()
            if play_again in ['y', 'yes']:
                break
            elif play_again in ['n', 'no']:
                print("\nThanks for playing Bulls & Cows! 🐂🐄")
                return
            else:
                print("❌ Please enter 'y' for yes or 'n' for no.")

if __name__ == "__main__":
    main()
