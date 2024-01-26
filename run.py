import random

def choose_random_city():
    cities = ["Berlin", "Hamburg", "Munich", "Cologne", "Frankfurt", "Stuttgart", "Dusseldorf", "Dortmund", "Essen",
              "Leipzig", "Bremen", "Dresden", "Hanover", "Nuremberg", "Duisburg", "Bochum", "Wuppertal", "Bielefeld",
              "Bonn", "Mannheim", "Karlsruhe", "Wiesbaden", "Munster", "Gelsenkirchen", "Augsburg", "Moenchengladbach",
              "Braunschweig", "Chemnitz", "Kiel", "Aachen", "Magdeburg", "Halle", "Freiburg", "Krefeld", "Lubeck",
              "Oberhausen", "Erfurt", "Mainz", "Rostock", "Kassel", "Hagen", "Saarbrucken", "Hamm", "Potsdam"]
    return random.choice(cities).upper()

# Get a random city
random_city = choose_random_city()
print(random_city)

def hangman():
    player_name = input("Set your name: ")

    if not player_name:
        player_name = "Guest"
        print("No name provided. Defaulting to Guest.")

    print(f"Welcome, {player_name}, to Hangman - Guess the City in Germany!")

hangman()