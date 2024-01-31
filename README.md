<img width="1005" alt="Screenshot 2024-01-30 at 16 29 57" src="https://github.com/fh255/Hangman_guess/assets/34744096/0b2676d1-ba58-4f2a-bc0e-84cf5e7a6384">


# Hangman - Guess the City in Germany

Welcome to Hangman - Guess the City in Germany! This is a simple text-based Hangman game where you try to guess the name of a city in Germany. Have fun and enjoy the game!

## Getting Started

1. Make sure you have Python installed on your system.
2. Clone this repository:

    ```bash
    git clone https://hangman-guess-german-city-a1d4f2c4de91.herokuapp.com/
    cd hangman-german-cities
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Set up the game:

    - Create a JSON file named `cities.json` with a list of cities in Germany.
    - Update the file path in the code to point to your `cities.json`:

        ```python
        cities_file_path = 'path/to/cities.json'
        ```

## How to Play

1. Run the game:

    ```bash
    python3 run.py
    ```

2. Enter your name when prompted.

3. Follow the on-screen instructions to guess the city. You can guess a single letter or the entire word.

4. Have fun playing and try to guess the city correctly within 6 attempts!

## Rules

- You need to guess the name of a city in Germany.
- You can guess a single letter or the entire word.
- You have 6 attempts to guess the word.
- If you guess a letter correctly, it will be revealed in the word.
- If you guess the entire word correctly, you win!
- If you run out of attempts, the correct city will be revealed.
- At any point, you can type '0' to exit or '1' to start a new game.


