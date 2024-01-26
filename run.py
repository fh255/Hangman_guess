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

# Call the hangman function
hangman()
