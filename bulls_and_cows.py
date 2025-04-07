import random
import os

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_number(length, allow_repeats=False):
    """Generate a random number of specified length.
    
    If allow_repeats is False, all digits will be unique.
    If allow_repeats is True, digits may be repeated.
    """
    if allow_repeats:
        # Generate a number with possibly repeated digits
        if length > 1:
            # First digit can't be 0 for multi-digit numbers
            first_digit = random.randint(1, 9)
            # Generate each remaining digit independently
            rest_digits = [random.randint(0, 9) for _ in range(length - 1)]
            return str(first_digit) + ''.join(map(str, rest_digits))
        else:
            # Single digit can be 0-9
            return str(random.randint(0, 9))
    else:
        # Generate a number with unique digits
        digits = list(range(10))  # 0-9
        random.shuffle(digits)
        
        # Ensure first digit is not 0 for numbers with length > 1
        if length > 1 and digits[0] == 0:
            # Swap with a non-zero digit
            for i in range(1, 10):
                if digits[i] != 0:
                    digits[0], digits[i] = digits[i], digits[0]
                    break
        
        return ''.join(map(str, digits[:length]))

def calculate_bulls_and_cows(secret, guess):
    """Calculate the number of bulls and cows."""
    bulls = 0
    cows = 0
    
    # Check for bulls (correct digit in correct position)
    for i in range(len(secret)):
        if guess[i] == secret[i]:
            bulls += 1
    
    # Check for cows (correct digit in wrong position)
    # Count common digits in both numbers
    for digit in set(guess):
        cows += min(secret.count(digit), guess.count(digit))
    
    # Subtract bulls from common digits to get cows
    cows -= bulls
    
    return bulls, cows

def display_title():
    """Display the game title."""
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
    """Display the game rules."""
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
    """Get the difficulty level from the player."""
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
    """Validate the player's guess."""
    # Check if input is a number
    if not guess.isdigit():
        return False, "Your guess must contain only digits."
    
    # Check if input has the correct length
    if len(guess) != length:
        return False, f"Your guess must be {length} digits long."
    
    # Check if all digits are unique (only if repeats are not allowed)
    if not allow_repeats and len(set(guess)) != length:
        return False, "Your guess must contain unique digits."
    
    # For numbers with length > 1, first digit shouldn't be 0
    if length > 1 and guess[0] == '0':
        return False, "The first digit cannot be 0."
    
    return True, ""

def display_history(history):
    """Display the history of guesses."""
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
    """Get the game mode from the player."""
    print("\n🎮 CHOOSE GAME MODE:")
    print("1. Player Guesses (You guess the computer's number)")
    print("2. Computer Solver (Computer guesses your number)")
    
    while True:
        try:
            choice = input("\nEnter your choice (1-2): ")
            if choice == '1':
                return "player"
            elif choice == '2':
                return "computer"
            else:
                print("❌ Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("❌ Invalid input. Please try again.")

def generate_all_possible_numbers(length, allow_repeats=False):
    """Generate all possible numbers of specified length.
    
    If allow_repeats is False, all digits will be unique.
    If allow_repeats is True, digits may be repeated.
    """
    if allow_repeats:
        return generate_all_possible_numbers_with_repeats(length)
    else:
        return generate_all_possible_numbers_unique(length)

def generate_all_possible_numbers_unique(length):
    """Generate all possible numbers with unique digits of specified length."""
    if length > 10:
        raise ValueError("Cannot generate numbers with unique digits longer than 10 digits")
    
    possible_numbers = []
    
    # Generate all permutations of digits
    digits = list(range(10))  # 0-9
    
    # For numbers with length > 1, first digit can't be 0
    if length > 1:
        first_digits = list(range(1, 10))  # 1-9
        for first_digit in first_digits:
            remaining_digits = digits.copy()
            remaining_digits.remove(first_digit)
            
            # Generate all permutations of remaining digits
            for perm in generate_permutations(remaining_digits, length - 1):
                possible_numbers.append(str(first_digit) + ''.join(map(str, perm)))
    else:
        # For single-digit numbers, 0-9 are all valid
        possible_numbers = [str(d) for d in digits]
    
    return possible_numbers

def generate_all_possible_numbers_with_repeats(length):
    """Generate all possible numbers with possibly repeated digits of specified length.
    
    Note: For longer lengths, this can generate a very large number of possibilities.
    For example, for length=6, there are 10^6 = 1,000,000 possibilities.
    """
    # For very long lengths, this could be memory-intensive
    # Consider implementing a generator version for production use
    if length > 6:
        print("⚠️ Warning: Generating all possible numbers with repeated digits for length > 6")
        print("This may take a long time and use a lot of memory.")
    
    possible_numbers = []
    
    # For numbers with length > 1, first digit can't be 0
    if length > 1:
        # Generate all possible combinations
        for first_digit in range(1, 10):  # 1-9
            # For the remaining positions, any digit 0-9 can be used
            # We'll use a recursive helper function to generate all combinations
            for rest_digits in generate_combinations_with_repeats(length - 1):
                possible_numbers.append(str(first_digit) + ''.join(map(str, rest_digits)))
    else:
        # For single-digit numbers, 0-9 are all valid
        possible_numbers = [str(d) for d in range(10)]
    
    return possible_numbers

def generate_combinations_with_repeats(length):
    """Generate all combinations of digits (0-9) of specified length, allowing repeats."""
    if length == 0:
        yield []
    else:
        for digit in range(10):  # 0-9
            for rest in generate_combinations_with_repeats(length - 1):
                yield [digit] + rest

def generate_permutations(digits, length):
    """Generate all permutations of specified length from the given digits."""
    if length == 0:
        return [[]]
    
    result = []
    for i, digit in enumerate(digits):
        remaining_digits = digits[:i] + digits[i+1:]
        for perm in generate_permutations(remaining_digits, length - 1):
            result.append([digit] + perm)
    
    return result

def filter_possibilities(possibilities, guess, bulls, cows):
    """Filter the list of possibilities based on the feedback."""
    filtered = []
    
    for possible in possibilities:
        b, c = calculate_bulls_and_cows(possible, guess)
        if b == bulls and c == cows:
            filtered.append(possible)
    
    return filtered

def computer_solver(length, allow_repeats=False):
    """Computer solver for Bulls and Cows game."""
    print(f"\n🤖 COMPUTER SOLVER MODE (Length: {length})")
    print("The computer will generate a secret number and then try to solve it.")
    print("You'll see the computer's solving strategy in action.")
    
    if allow_repeats:
        print("\n⚠️ NOTE: The computer solver will now consider numbers with repeated digits.")
        print("This significantly increases the number of possibilities, so it may take longer to solve.")
    
    # Generate a secret number for the computer to guess
    secret_number = generate_number(length, allow_repeats)
    print(f"\n🎲 Generated a secret {length}-digit number.")
    
    # Check if the number has repeated digits
    if allow_repeats:
        has_repeats = len(set(secret_number)) < len(secret_number)
        if has_repeats:
            print("(Debug: The number contains repeated digits)")
        else:
            print("(Debug: The number does NOT contain repeated digits - this is still possible by chance)")
    
    # For debugging or demonstration, you can uncomment this
    print(f"Secret number: {secret_number} (shown for demonstration)")
    
    # Generate all possible numbers
    print("\nGenerating all possible numbers... (this may take a moment for longer lengths)")
    possibilities = generate_all_possible_numbers(length, allow_repeats)
    print(f"Generated {len(possibilities)} possible numbers.")
    
    attempts = 0
    history = []
    
    # Add a small delay between guesses to make it easier to follow
    import time
    
    # Main solving loop
    while possibilities:
        # Make a guess (choose the first possibility for simplicity)
        # In a more advanced implementation, we could use information theory
        # to choose the guess that would eliminate the most possibilities
        guess = possibilities[0]
        attempts += 1
        
        print(f"\n🤖 Computer's guess #{attempts}: {guess}")
        
        # Calculate Bulls and Cows automatically
        bulls, cows = calculate_bulls_and_cows(secret_number, guess)
        print(f"🐂 Bulls: {bulls} | 🐄 Cows: {cows}")
        
        # Add to history
        history.append((guess, bulls, cows))
        
        # Check if the computer has won
        if bulls == length:
            print(f"\n🎉 The computer guessed the number {secret_number} in {attempts} attempts!")
            display_history(history)
            return
        
        # Filter possibilities based on feedback
        old_count = len(possibilities)
        possibilities = filter_possibilities(possibilities, guess, bulls, cows)
        new_count = len(possibilities)
        
        print(f"Narrowed down from {old_count} to {new_count} possibilities.")
        
        # Add a small delay to make it easier to follow
        time.sleep(1)
        
        if not possibilities:
            print("\n❌ Something went wrong. There are no possible numbers that match the feedback.")
            print("This should never happen in automatic mode.")
            return

def get_repeat_option():
    """Ask if the player wants to allow repeated digits."""
    print("\n🔄 ALLOW REPEATED DIGITS?")
    print("1. No (Traditional mode - all digits must be unique)")
    print("2. Yes (Challenge mode - digits may be repeated)")
    
    while True:
        try:
            choice = input("\nEnter your choice (1-2): ")
            if choice == '1':
                return False
            elif choice == '2':
                return True
            else:
                print("❌ Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("❌ Invalid input. Please try again.")

def play_game():
    """Main function to play the Bulls and Cows game."""
    clear_screen()
    display_title()
    display_rules()
    
    # Get difficulty level
    length, difficulty_name = get_difficulty()
    
    # Ask if the player wants to allow repeated digits
    allow_repeats = get_repeat_option()
    
    # Get game mode
    mode = get_game_mode()
    
    if mode == "computer":
        # Pass the allow_repeats parameter to the computer solver
        computer_solver(length, allow_repeats)
        
        # Ask to play again
        play_again = input("\nWould you like to play again? (y/n): ").lower()
        if play_again == 'y':
            play_game()
        else:
            print("\n👋 Thanks for playing Bulls & Cows!")
        return
    
    # Generate the secret number for player mode
    secret_number = generate_number(length, allow_repeats)
    
    # Game variables
    attempts = 0
    history = []
    
    # Display game info
    if allow_repeats:
        print(f"\n🎲 {difficulty_name} mode with REPEATED DIGITS: I've generated a {length}-digit number.")
        # Check if the number actually has repeated digits
        has_repeats = len(set(secret_number)) < len(secret_number)
        if has_repeats:
            print("(Debug: The number contains repeated digits)")
        else:
            print("(Debug: The number does NOT contain repeated digits - this is still possible by chance)")
    else:
        print(f"\n🎲 {difficulty_name} mode with UNIQUE DIGITS: I've generated a {length}-digit number.")
    
    print(f"Try to guess it! (Type 'quit' to exit, 'hint' for a hint, 'history' to see past guesses)")
    
    # For debugging - always show the secret number during testing
    print(f"Secret number: {secret_number} (shown for testing)")
    
    # Main game loop
    while True:
        guess = input("\nEnter your guess: ").lower()
        
        # Handle special commands
        if guess == 'quit':
            print(f"\n👋 Thanks for playing! The secret number was {secret_number}.")
            break
        elif guess == 'hint':
            # Provide a hint about one random position
            position = random.randint(0, length - 1)
            print(f"🔍 Hint: The digit at position {position + 1} is {secret_number[position]}.")
            continue
        elif guess == 'history':
            display_history(history)
            continue
        
        # Validate the guess
        valid, error_message = validate_guess(guess, length, allow_repeats)
        if not valid:
            print(f"❌ {error_message}")
            continue
        
        # Increment attempts
        attempts += 1
        
        # Calculate bulls and cows
        bulls, cows = calculate_bulls_and_cows(secret_number, guess)
        
        # Add to history
        history.append((guess, bulls, cows))
        
        # Display result
        print(f"🐂 Bulls: {bulls} | 🐄 Cows: {cows}")
        
        # Check if the player has won
        if bulls == length:
            print(f"\n🎉 Congratulations! You've guessed the number {secret_number} in {attempts} attempts!")
            
            # Display final history
            display_history(history)
            
            # Ask to play again
            play_again = input("\nWould you like to play again? (y/n): ").lower()
            if play_again == 'y':
                play_game()
            else:
                print("\n👋 Thanks for playing Bulls & Cows!")
            break

# Only run the game when this script is executed directly, not when imported
if __name__ == "__main__":
    play_game()
