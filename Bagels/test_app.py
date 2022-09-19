from app import RandomNumberGenerator


def test_random():
    assert type(RandomNumberGenerator(5, 12)) == int
