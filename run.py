import json
import random

def load_cities_from_json(file_path):
    """
    Load cities from a JSON file.

    Parameters:
    file_path (str): The path to the JSON file.

    Returns:
    list: List of cities.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data["cities"]

def choose_random_city(cities):
    """
    Choose a random city from the predefined list.

    Parameters:
    cities (list): List of cities.

    Returns:
    str: A random city name in uppercase.
    """
    return random.choice(cities).upper()

def display_word(word, guessed_letters):
    """
    Display the current state of the word with revealed letters.

    Parameters:
    word (str): The word to be guessed.
    guessed_letters (list): List of guessed letters.

    Returns:
    str: Current state of the word with revealed letters.
    """
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def print_rules():
    """
    Print the rules of the Hangman game.
    """
    print("\nRules for Hangman - Guess the City in Germany:")
    print("1. You need to guess the name of a city in Germany.")
    print("2. You can guess a single letter or the entire word.")
    print("3. You have 6 attempts to guess the word.")
    print("4. If you guess a letter correctly, it will be revealed in the word.")
    print("5. If you guess the entire word correctly, you win!")
    print("6. If you run out of attempts, the correct city will be revealed.")
    print("7. At any point, you can type '0' to exit or '1' to start a new game.")
    print("8. Have fun and enjoy the game!\n")

def play_hangman(cities):
    """
    Main function to play the Hangman game.

    Parameters:
    cities (list): List of cities.
    """
    city_to_guess = choose_random_city(cities)
    guessed_letters = []
    attempts = 6

    print("Here's a hint: First two letters are", city_to_guess[:2])

    while attempts > 0:
        print("\nAttempts left:", attempts)
        print("Current Word:", display_word(city_to_guess, guessed_letters))

        guess = input("Enter a letter or the whole word (type '0' to exit, '1' for a new game): ").upper()

        if guess == '0':
            print("Exiting the game.")
            return
        elif guess == '1':
            print("Starting a new game.")
            play_hangman(cities)

        if len(guess) == 1:  # Single letter guess
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in city_to_guess:
                print("Good guess!")
                guessed_letters.append(guess)
            else:
                print("Incorrect guess. Try again.")
                attempts -= 1
        elif len(guess) == len(city_to_guess) and guess.isalpha():  # Whole word guess
            if guess == city_to_guess:
                print(f"Congratulations! You guessed the city correctly:", city_to_guess)
                return
            else:
                print("Incorrect guess. Try again.")
                attempts -= 1
        else:
            print("Invalid input. Please enter a valid letter or the whole word.")

        if set(city_to_guess) <= set(guessed_letters):
            print(f"Congratulations! You guessed the city correctly:", city_to_guess)
            return

    if attempts == 0:
        print(f"Sorry, you ran out of attempts. The correct city was:", city_to_guess)

if __name__ == "__main__":
    # Load cities from the JSON file
    cities_file_path = 'cities.json'  # Replace with the actual path to your JSON file
    cities = load_cities_from_json(cities_file_path)

    player_name = input("Set your name: ")

    if not player_name:
        player_name = "Guest"
        print("No name provided. Defaulting to Guest.")

    print(f"Welcome, {player_name}, to Hangman - Guess the City in Germany!")
    while True:
        print_rules()
        # Pass the loaded cities to the function
        play_hangman(cities)
        play_again = input("Do you want to play again? (Y/N): ").lower()
        if play_again != 'y':
            break
