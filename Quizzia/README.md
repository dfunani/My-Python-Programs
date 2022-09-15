# Program Title:
	Quizzia The Game

#### Video Demo:  
	<https://www.youtube.com/watch?v=nfmSUvQ14bU>

#### Description:
Quizzia is a python developed game, which will allow a user to choose from 3 game modes:
	1. US State Capitals Quiz (25 Questions)
	2. Maths Quiz (25 Questions maximum) 
	3. General Trivia (25 Questions)

No Repeat Questions Allowed

The user will be able to choose from one of the 3 options and once game is done, will be prompted to quiz or replay or choose a new game. Score will not persist between game modes.

The user will be able to run the game with a command line argument -q --quiz and a choice CHOICE = ['Mathematics', 'State Capitals', 'General Trivia'] choice should be enclosed in [""].

Text to Speech shall be used for the project to increase user experience and accessibility considerations for those visually impaired.

#### US State Capitals Quiz

Multiple Choice Quiz, containing 25 MC Questions. The quiz will only cover US Capital Cities. The user will select an MCQ option and will be prompted with "correct" or "not" (No second chances). A final result will be included at the end. The 25 quiz questions will be a random selection from the full 50 states options.

What is the Capital City of [State Name]:
A. 
B.
C.
D.

Answer:

#### Maths Quiz

Arithmetic quiz using a Standard maths format (x operator y = ). Operators allowed will be "+", "-" , "*" and "/". User will have the option to choose a level from 1 - 3 (similarily to the professor program) 1 = [1 - 10], 2 = [11 - 100] and 3 = [101 - 1000]. Please note, user will have only one guess but will have a limited timer based on the level chosen 1 - 10 seconds, 2 - 60 seconds/1 minute and 3 - 600 seconds/10 minutes. If timer lapses, question is deemed incorrect.

X: [Int] op Y: [Int]

Answer: 

#### General Trivia

Similar to the State capitals quiz, however the collection of 50 questions will be general knowledge questions in an Q&A format extracted from <https://www.opinionstage.com/blog/trivia-questions/> User will be able to choose a category 
Categories:
	"Category 1: Technology, Science, Geography, History, Modern Literature",
    "Category 2: Comics, Movies & TV, Music, Fashion, Design",
    "Category 3: Cars, Sports, Games, Food & Drinks, Human Health",
    "Category 4: People, Celebrities, Performing Arts, Politics, Law",
    "Category 5: Riddles, Holidays, Religion, Mythology, Animals",

What is the Answer to Trivia Question Below:
A. 
B.
C.
D.

Answer: 