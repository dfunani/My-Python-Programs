from project import (
    check_maths_response,
    check_capitals_response,
    check_trivia_response,
    select_quiz,
    game_message,
)


def test_select_quiz():
    assert select_quiz("Mathematics") == "Mathematics"


def test_game_message():
    assert game_message("Welcome") == [
        "	Welcome to Quizzia	",
        "The All-In-One Quiz and Trivia Platform",
    ]


def test_capitals_response():
    assert check_capitals_response("Santa Fe", "Santa Fe") == 1
    assert check_capitals_response("Santa Fe", "US Capital") == 0


def test_maths_response():
    assert check_maths_response(4, 4.00) == 1
    assert check_maths_response(4.00, 4.22) == 0


def test_trivia_response():
    assert check_trivia_response("2007".lower(), "2007".lower()) == 1
    assert check_trivia_response("Karl Benz".lower(), "Karl Benz".lower()) == 1
    assert check_trivia_response("Soocer".lower(), "Football".lower()) == 0
