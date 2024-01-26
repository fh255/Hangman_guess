import random

def choose_random_city():
    cities = ["Berlin", "Hamburg", "Munich", "Cologne", "Frankfurt", "Stuttgart", "Dusseldorf", "Dortmund", "Essen",
              "Leipzig", "Bremen", "Dresden", "Hanover", "Nuremberg", "Duisburg", "Bochum", "Wuppertal", "Bielefeld",
              "Bonn", "Mannheim", "Karlsruhe", "Wiesbaden", "Munster", "Gelsenkirchen", "Augsburg", "Moenchengladbach",
              "Braunschweig", "Chemnitz", "Kiel", "Aachen", "Magdeburg", "Halle", "Freiburg", "Krefeld", "Lubeck",
              "Oberhausen", "Erfurt", "Mainz", "Rostock", "Kassel", "Hagen", "Saarbrucken", "Hamm", "Potsdam"]
    return random.choice(cities).upper()

# Corrected the spelling of print()
print(choose_random_city())