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
- Testing
- Deployment
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

![Hangman](https://github.com/fh255/Hangman_guess/assets/34744096/9309b0df-3d22-4065-9fd4-ee004ecc49e7)

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


## Testing

### Manual Testing
- Successfully underwent CI Python Linter checks, ensuring the absence of lingering issues.
- Tested via both the Gitpod and Heroku terminals, encompassing a diverse array of valid and invalid inputs, as well as repeating the same inputs for comprehensive verification.

### Validator
- [PEP8 Python Validator](https://pep8ci.herokuapp.com/): This program is now error-free, having undergone thorough testing and validation, ensuring the absence of any lingering issues.
   <img width="1259" alt="PP8" src="https://github.com/fh255/Hangman_guess/assets/34744096/07816521-2f5d-4c51-a042-8692e7cfcbfd">

  
## Deployment

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














