from static import QUIZ, CATEGORIES, TRIVIA, OPERATORS, LEVELS
import random
import sys
import pyinputplus as pyip
import re
import argparse
import cowsay
import pyttsx3

engine = pyttsx3.init()


def main():
    # Check for CLI arguments
    parser = argparse.ArgumentParser(description="Quizzia Quick Access")

    parser.add_argument(
        "-q",
        "--quiz",
        type=str,
        choices=["Mathematics", "State Capitals", "General Trivia"],
        help="Select a Quiz from the applicable choices in {}",
    )

    args = parser.parse_args()
    if args.quiz:
        quiz_selected = args.quiz
    else:
        quiz_selected = None

    message = game_message("Welcome")
    for _ in message:
        print(_)
        engine.say(_)
        engine.runAndWait()

    print()

    # Game Loop until player chooses Quit
    state = "Play"
    while state != "Quit Game":
        if not quiz_selected:
            quiz_selected = select_quiz()

        # Choose a game mode
        match quiz_selected:
            case "Mathematics":
                final_score = maths_quiz()
            case "State Capitals":
                final_score = capitals_quiz()
            case "General Trivia":
                final_score = general_trivia()

        print(
            game_message("score")[0]
            + str(final_score[0])
            + " out of "
            + str(final_score[1])
            + "\n"
        )
        engine.say(
            game_message("score")[0]
            + str(final_score[0])
            + " out of "
            + str(final_score[1])
            + "\n"
        )
        engine.runAndWait()

        # Replay Option (or Quit) or New Quiz
        engine.say("Choose: Play Quiz Again, Choose New Quiz or Quiz Game")
        engine.runAndWait()
        state = pyip.inputMenu(
            ["Play Quiz Again", "Choose New Quiz", "Quit Game"],
            numbered=True,
            lettered=False,
        )
        engine.say(state)
        engine.runAndWait()

        match state:
            case "Choose New Quiz":
                quiz_selected = None

    message = game_message("Game Over")
    for _ in message:
        print(_)
        engine.say(_)
        engine.runAndWait()
    return 0


def game_message(state: str):
    message = {
        "Welcome": ["	Welcome to Quizzia	", "The All-In-One Quiz and Trivia Platform"],
        "Game Over": ["Thank you for playing Quizzia", "	Come Back Soon	"],
        "Math Quiz": ["Math Quiz", "Level "],
        "State Capitals": ["US State Capitals Quiz"],
        "Trivia": ["General Trivia", "Category: "],
        "score": ["Your Score: "],
    }
    return message[state]


def select_quiz(quiz=None):
    engine.say("Choose a Quiz: State Capitals, Mathematics or General Trivia")
    engine.runAndWait()
    if not quiz:
        quiz = pyip.inputMenu(
            ["State Capitals", "Mathematics", "General Trivia"],
            prompt="Choose a Quiz\n",
            lettered=False,
            numbered=True,
        )
    return quiz


def check_capitals_response(answer, response):
    result = None
    if response == answer:
        print("Correct!!!")
        engine.say('Correct!!!')
        engine.runAndWait()
        result = 1
    else:
        print("Incorrect!!!")
        engine.say("Incorrect!!!")
        engine.runAndWait()
        print("Correct Answer: " + answer)
        engine.say("The correct answer is " + answer)
        engine.runAndWait()
        result = 0

    return result


def capitals_quiz():
    print()
    score = 0
    no_questions = 0

    print(game_message("State Capitals")[0])
    engine.say(game_message("State Capitals")[0])
    engine.runAndWait()
    print()

    random.shuffle(QUIZ, lambda: random.random())

    for question in QUIZ:
        no_questions += 1
        answer = question[1][0]
        random.shuffle(question[1], lambda: random.random())
        
        engine.say("What is the capital of " + question[0] + "?")
        engine.runAndWait()
        
        engine.say(f'A. {question[1][0]}, B. {question[1][1]}, C. {question[1][2]}, D. {question[1][3]}')
        engine.runAndWait()

        response = pyip.inputMenu(
            question[1],
            prompt="What is the capital of " + question[0] + "?\n",
            lettered=True,
            numbered=False,
        )

        score += check_capitals_response(answer, response)

        if no_questions >= 25:
            break

    return score, no_questions


def check_maths_response(answer, response):
    result = None
    if response is None:
        print("Timed Out")
        engine.say("Timed Out!!!")
        engine.runAndWait()
    elif round(answer, 2) == round(response, 2):
        print("Correct!!!")
        engine.say("Correct!!!")
        engine.runAndWait()
        result = 1
    else:
        print("Incorrect!!!")
        engine.say("Incorrect!!!")
        engine.runAndWait()
        print("Correct Answer: " + str(round(answer, 2)) + "\n")
        engine.say("The correct answer is " + str(round(answer, 2)))
        engine.runAndWait()
        result = 0

    return result


def maths_quiz():
    print()
    score = 0
    no_questions = 0
    print(game_message("Math Quiz")[0])
    engine.say(game_message("Math Quiz")[0])
    engine.runAndWait()
    level = pyip.inputNum(prompt="Choose a math quiz level: ", min=1, max=3)
    print(game_message("Math Quiz")[1] + str(level))
    engine.say(game_message("Math Quiz")[1] + str(level))
    engine.runAndWait()
    print()

    x_list = [i for i in range(LEVELS[str(level)][0], LEVELS[str(level)][1])]
    y_list = [i for i in range(LEVELS[str(level)][0], LEVELS[str(level)][1])]

    timeout = None
    match level:
        case 1:
            timeout = 10
        case 2:
            timeout = 60
        case 3:
            timeout = 600

    random.shuffle(x_list)
    random.shuffle(y_list)

    for index in range(len(x_list)):
        no_questions += 1
        operator = random.choice(OPERATORS)

        answer = None
        match operator:
            case "*":
                answer = x_list[index] * y_list[index]
            case "/":
                answer = x_list[index] / y_list[index]
            case "+":
                answer = x_list[index] + y_list[index]
            case "-":
                answer = x_list[index] - y_list[index]
        
        engine.say(str(x_list[index])
                + " "
                + operator
                + " "
                + str(y_list[index])
                + " = ")
        engine.runAndWait()

        try:
            response = pyip.inputNum(
                prompt=str(x_list[index])
                + " "
                + operator
                + " "
                + str(y_list[index])
                + " = ",
                timeout=timeout,
            )
        except pyip.TimeoutException:
            response = None

        score += check_maths_response(answer, response)

        if no_questions >= 25:
            break

    return score, no_questions


def check_trivia_response(response, answer):
    result = None
    if re.search(response, answer):
        print("Correct!!!")
        engine.say("Correct!!!")
        engine.runAndWait()
        result = 1
    else:
        print("Incorrect!!!")
        engine.say("Incorrect!!!")
        engine.runAndWait()
        print("Correct Answer: " + answer)
        engine.say("The correct answer is " + answer)
        engine.runAndWait()
        result = 0

    return result


def general_trivia():
    print()
    score = 0
    no_questions = 0

    print(game_message("Trivia")[0])
    engine.say(game_message("Trivia")[0])
    engine.runAndWait()

    get_category = pyip.inputMenu(
        CATEGORIES, prompt="Choose a category\n", numbered=True, lettered=False
    )
    print()

    print(game_message("Trivia")[1] + get_category)
    print()

    engine.say(get_category)
    engine.runAndWait()

    get_category = get_category.split(":")[0]
    
    random.shuffle(TRIVIA[get_category], lambda: random.random())

    for question in TRIVIA[get_category]:
        no_questions += 1

        engine.say(question[0])
        engine.runAndWait()
        response = pyip.inputStr(prompt=question[0] + " ")

        score += check_trivia_response(response.lower(), question[1].lower())

        if no_questions >= 25:
            break

    return score, no_questions


if __name__ == "__main__":
    main()
