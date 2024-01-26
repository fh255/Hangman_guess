import random

def choose_random_city():
    # List of cities in Germany
    cities = ["Berlin", "Hamburg", "Munich", "Cologne", "Frankfurt", "Stuttgart", "Dusseldorf", "Dortmund", "Essen",
              "Leipzig", "Bremen", "Dresden", "Hanover", "Nuremberg", "Duisburg", "Bochum", "Wuppertal", "Bielefeld",
              "Bonn", "Mannheim", "Karlsruhe", "Wiesbaden", "Munster", "Gelsenkirchen", "Augsburg", "Moenchengladbach",
              "Braunschweig", "Chemnitz", "Kiel", "Aachen", "Magdeburg", "Halle", "Freiburg", "Krefeld", "Lubeck",
              "Oberhausen", "Erfurt", "Mainz", "Rostock", "Kassel", "Hagen", "Saarbrucken", "Hamm", "Potsdam"]
    
    # Return a randomly chosen city in uppercase
    return random.choice(cities).upper()

# Get a random city
random_city = choose_random_city()
print(random_city)



# Call the hangman function
def hangman():
    # Get player name from input
    player_name = input("Set your name: ")

    # Check if no name is provided, default to "Guest"
    if not player_name:
        player_name = "Guest"
        print("No name provided. Defaulting to Guest.")

    # Welcome message
    print(f"Welcome, {player_name}, to Hangman - Guess the City in Germany!")

# Get a random city to guess
city_to_guess = choose_random_city()

# Initialize variables for guessed letters and attempts
guessed_letters = []
attempts = 5

# Display a hint for the first two letters of the city
print("Here's a hint: First two letters are", city_to_guess[:2])

while attempts > 0:
        print("\nAttempts left:", attempts)
        print("Current Word:", display_word(city_to_guess, guessed_letters))

        guess = input("Enter a letter or the whole word: ").upper()

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
                print(f"Congratulations, {player_name}! You guessed the city correctly:", city_to_guess)
                break
            else:
                print("Incorrect guess. Try again.")
                attempts -= 1
        else:
            print("Invalid input. Please enter a valid letter or the whole word.")

        if set(city_to_guess) <= set(guessed_letters):
            print(f"Congratulations, {player_name}! You guessed the city correctly:", city_to_guess)
            break

    if attempts == 0:
        print(f"Sorry, {player_name}, you ran out of attempts. The correct city was:", city_to_guess)

if __name__ == "__main__":
hangman()
