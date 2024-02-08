<h1 align="center" > Hangman: Guess the Cities in Germany </h1>

[Play game here](https://hangman-guess-german-city-a1d4f2c4de91.herokuapp.com/)

[Details on GitHub Repo](https://github.com/fh255/Hangman_guess)

Welcome to "**Hangman: Guess the Cities in Germany**" – a captivating and educational game that challenges your knowledge of German cities. Immerse yourself in a guessing adventure as you attempt to unravel the names of iconic German cities letter by letter. From the historic charm of Berlin to the picturesque landscapes of Munich, each correct guess brings you closer to victory. Sharpen your geographical wit and discover the diverse and culturally rich cities that make Germany a fascinating destination. Whether you're a geography enthusiast or just looking for a fun way to test your city-naming skills, Hangman: Guess the Cities in Germany promises an engaging and entertaining experience for players of all ages.  Prost und viel Spaß (Cheers and have fun)!

<img width="1005" alt="Screenshot 2024-01-30 at 16 29 57" src="https://github.com/fh255/Hangman_guess/assets/34744096/ece82f9b-3447-47bd-9b25-19f157f4678b">

## Index

- User Story
  - Objective
  - Extent
  - Structure
- Features
- Technologies
  - Programming Language
  - Tools
- Testing
  - Functional Testing
  - Manual Testing
  - Validator
- Deployment
  - Cloning the github repository
  - Forking the github repository
  - Validator
- Credit

## User Story

### Objective
- Purpose of the Website
  - Provide users with the opportunity to guess the concealed country within a maximum of 6 attempts.
  - Enable users to assess their knowledge of the cities in Germany by offering a platform to test and expand their awareness.
 
- Motivations for Visiting the Website
  - Engage in a solo guessing game, challenging oneself within a restricted number of attempts.
  - Assess one's global knowledge by participating in quizzes related to countries worldwide.

### Extent
- User Preferences
   - Precise and straightforward instructions for navigating the game.
   - Transparent notifications indicating the number of attempts, tracking used letters, issuing warnings for incorrect guesses, and providing hints for the mystery word.
   - The option to restart or exit the game at any point during gameplay.
   - Categorization of words within the game.
   - The ability to choose between starting a new round or exiting the game after completing each round.
- Developer's Expectations
   - Ensure the user discovers an enjoyable and user-friendly gaming experience.
   - Implement well-commented code to facilitate straightforward maintenance.
 
 ### Structure
The game incorporates a sequence of logical steps to facilitate seamless navigation. Users receive clear instructions throughout their journey, aiding them in understanding the required input and making informed decisions. Furthermore, each user action prompts a corresponding response, whether positive or negative.

The game's logic is visually depicted in a general flowchart, with modifications introduced during the programming and testing phases. The design prioritizes a more user-friendly visual structure, featuring distinct line patterns at pivotal moments in the game: the start, end, each attempt, and when presenting the rules. Additionally, new lines are strategically inserted at the conclusion of each message to prevent screen overload.

![Hangama_city](https://github.com/fh255/Hangman_guess/assets/34744096/4d7ae69d-bd04-4015-b9e3-d774e759a8ed)

At any stage of the game, the player has the option to exit by pressing '0' or initiate a new game by pressing '1'. This aspect is not represented in the flowchart.

## Feature

- At the commencement of the game, the player will be prompted to create a username. Upon entering a name, a welcoming message, along with the rules of the game, will appear on the screen.

  <img width="659" alt="rules" src="https://github.com/fh255/Hangman_guess/assets/34744096/94322919-0450-4d76-82e1-69c344e75f35">

- If the user does not provide a username, it will default to "Guest," and the system will generate a welcoming message along with the game rules on thescreen.

   <img width="643" alt="Screenshot 2024-02-05 at 16 36 18" src="https://github.com/fh255/Hangman_guess/assets/34744096/fc758606-22a9-4b27-b11c-53788ed0fb49">

- The initial two letters of the secret word will be selected and displayed on the screen as a hint.

   <img width="500" alt="first 2 letter" src="https://github.com/fh255/Hangman_guess/assets/34744096/e407fa2a-21c1-49d2-b2c3-0dab969df1d5">
- The user has the option to guess either a single letter, multiple letters, or the entire city name.
  
   <img width="728" alt="multiple letter" src="https://github.com/fh255/Hangman_guess/assets/34744096/d5be7f5c-6db8-4601-9648-726ef5025e8a">

   <img width="728" alt="correct word guess" src="https://github.com/fh255/Hangman_guess/assets/34744096/0990b425-cfeb-439f-98cd-58f557924f10">

   
- If the user repeatedly guesses the same letter, whether correct or incorrect, a message will appear on the screen stating, "You already guessed this letter . Try again." Additionally, with each incorrect letter, the number of attempts will decrement by one.
 
   <img width="728" alt="same letter guess" src="https://github.com/fh255/Hangman_guess/assets/34744096/a7394e91-07aa-4ffd-abb0-40dc37cbecd8">

- At any point in the game, the user can exit by pressing 0. Likewise, they have the option to initiate a new game by pressing 1.

<img width="728" alt="exiting game" src="https://github.com/fh255/Hangman_guess/assets/34744096/b6a38956-fccb-4b6c-a21a-66ad7692cbb8">

## Technology
### Programming Language
- [Python 3.12.1](https://www.python.org/)

### Tools
- [Git](https://git-scm.com/) : Gitpod terminal was employed for version control, facilitating Git commits and GitHub pushes.
- [Github](https://github.com/) : Following its transfer from Git, the code was utilized as the designated repository for the project.
- [draw.io ](https://app.diagrams.net/): Utilized for crafting the game's flowchart.
- [Heroku](https://dashboard.heroku.com/apps): Deployed the application and furnished an environment for code execution.
- [GitLab](https://tabletomarkdown.com/convert-spreadsheet-to-markdown/): Was employed to generate tables in the testing section.


## Testing

### Functional Testing
Verify that the various components of the application function as intended through functional testing.

| Test Label            | Test Action                                                                                                                                           | Expected Outcome                                                                                                                                           | Test Outcome |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| Load Cities           | Provide the path to a valid JSON file containing a list of cities in Germany.                                                                         | The function should return a list of city names.                                                                                                           | Pass         |
| Random City Selection | Provide a list of city names.                                                                                                                         | The function should return a randomly selected city in uppercase.                                                                                          | Pass         |
| Validate User Name    | Call the play_hangman function and provide various inputs for the player name, including valid names, empty names, and names with special characters. | The program should handle user names appropriately, defaulting to "Guest" when no name is provided, and ensuring that the name is used in the game output. | Pass         |
| Welcome Massage       | Run the Hangman game and observe the output.                                                                                                          | The welcome message should be displayed with the player's name, the game rules, and any additional information.                                            | Pass         |
| Display Word          | Provide a word and a list of guessed letters.                                                                                                         | The function should return a string with guessed letters revealed and others as underscores.                                                               | Pass         |
| Single Letter Guess   | Play the Hangman game, guess a single letter correctly or incorrectly.                                                                                | The game should correctly respond to the guess, update display, and track attempts.                                                                        | Pass         |
| Whole Word Guess      | Play the Hangman game, guess the entire word correctly or incorrectly.                                                                                | The game should correctly respond to the guess, update display, and track attempts.                                                                        | Pass         |
| Game Ending           | Play the Hangman game until the end, either by guessing the word or running out of attempts.                                                          | The game should display the correct outcome (win or lose) and the correct city.                                                                            | Pass         |
| Exit and New Game     | During the game, choose to exit (pressing 0) and start (1) a new game.                                                                                | The game should exit or start a new game based on user input.                                                                                              | Pass         |
| Play Again            | After finishing a game, choose to play again (Y) or exit(N).                                                                                          | The program should allow the player to continue or exit based on user input (Y/N).                                                                         | Pass         |
| Full Game Integration | Run the entire game, simulate user inputs for playing, and check the final output.                                                                    | The game should run smoothly, and the final output should reflect the game result.                                                                         | Pass         |
### Manual Testing
- Successfully underwent CI Python Linter checks, ensuring the absence of lingering issues.
- Tested via both the Gitpod and Heroku terminals, encompassing a diverse array of valid and invalid inputs, as well as repeating the same inputs for comprehensive verification.

### Validator
- [PEP8 Python Validator](https://pep8ci.herokuapp.com/): This program is now error-free, having undergone thorough testing and validation, ensuring the absence of any lingering issues.
   <img width="1259" alt="PP8" src="https://github.com/fh255/Hangman_guess/assets/34744096/07816521-2f5d-4c51-a042-8692e7cfcbfd">

  
## Deployment

### Cloning the github repository

- Open the GitHub repository you want to clone and click on the green "Code" button.
- Copy the repository URL provided (either HTTPS or SSH).
- Launch the Git Bash terminal.
- Navigate to the desired directory where you intend to store the cloned repository.
- Enter the command `git clone `, and then paste the previously copied URL. Press Enter to initiate the cloning process.
- To sync any modifications made in the local clone with the repository, utilize the subsequent steps.
```
a. Revise the code as necessary.
b. Access the terminal and execute git add . (or specify file_name).
c. Enter git commit -m "concise description of the modification".
d. Execute git push to upload the changes. 
```


### Forking the Github repository
By initiating a GitHub Repository fork, you can duplicate the original repository in your personal GitHub account. This allows you to review or implement changes without impacting the original repository.
- Navigate to the [GitHub repository](https://github.com/fh255/Hangman_guess) for the website.
- Located at the top of the Repository, you will find a "Fork" button.
- You should now possess a fresh copy of the initial repository within your own GitHub account.

### Deploy with Herokuapp
The deployments conducted manually through the Herokuapp.
#### Creating new account in Herokuapp
- To access the Heroku app, begin by registering for a free account and completing the sign-up form. Afterward, Heroku will send you an email containing a link. Upon clicking the link, you will be redirected to a page where you can set up your password. Following password setup, a page with a button labeled "Click here to proceed" will appear. Upon accepting the terms of service, the dashboard will become accessible.
 
#### Creating new app and Deploy
- To initiate the creation of a new app, click on the "Create new app" button. Provide the app's name and select the desired region. Prior to deployment, navigate to the Settings tab. Access the "Config Vars" section, where confidential data is stored. In the key field, enter the JSON file name in uppercase. Move to the workspace, copy the entire JSON file, paste it in the value field, and click the add button to include all the data.
- Proceed to the next step by adding two Buildpacks (Python and Node.js) to the application. In the deploy section, opt for GitHub as the deployment method and confirm the connection to GitHub. Specify the GitHub repository's name, search for it, and establish the link between the Heroku app and the GitHub repository.
- Select the Manual deploy option. Following the installation of Python, its dependencies, and various packages, a success message declaring "the app was successfully deployed" will appear on the screen, along with the deployed link.

## Credit
- I acquired knowledge of Python codes from diverse sources such as W3Schools, MDN Web Docs and TutorialsPoint.
- The idea for the Hangman Game's model originated from the Python for Beginners source.
- Gratitude to my mentor **Brian Macharia** for providing consistent support and valuable feedback.
-  Appreciation also extends to the readily available tutor assistance, accessible at any working hour.

## Acknowledgments
As part of my journey with [Code Institute](https://learn.codeinstitute.net/dashboard), I developed this game as my third project.














