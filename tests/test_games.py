from brain_games.games import brain_even
from brain_games.games import brain_calc
from brain_games.games import brain_gcd
from brain_games.games import brain_prime
from brain_games.games import brain_progression
from brain_games.games import brain_balance


# brain_even tests
def test_is_even():
    assert brain_even.is_even(4) is True
    assert brain_even.is_even(3) is False
    assert brain_even.is_even(0) is True


def test_generate_game_even(monkeypatch):
    monkeypatch.setattr(brain_even.random, 'randint', lambda a, b: 4)
    question, answer = brain_even.generate_game()
    assert question == 4
    assert answer == 'yes'


def test_generate_game_odd(monkeypatch):
    monkeypatch.setattr(brain_even.random, 'randint', lambda a, b: 3)
    question, answer = brain_even.generate_game()
    assert question == 3
    assert answer == 'no'


# brain_calc tests
def test_calculate_operators():
    assert brain_calc.calculate(2, 3, '+') == 5
    assert brain_calc.calculate(10, 4, '-') == 6
    assert brain_calc.calculate(3, 4, '*') == 12


def test_generate_game_calc(monkeypatch):
    monkeypatch.setattr(brain_calc.random, 'choice', lambda x: '+')
    monkeypatch.setattr(brain_calc.random, 'randint', lambda a, b: 5)
    question, answer = brain_calc.generate_game()
    assert '5 + 5' == question
    assert answer == '10'


# brain_gcd tests
def test_get_gcd():
    assert brain_gcd.get_gcd(12, 8) == 4
    assert brain_gcd.get_gcd(13, 7) == 1
    assert brain_gcd.get_gcd(10, 10) == 10
    assert brain_gcd.get_gcd(5, 0) == 5


def test_generate_game_gcd(monkeypatch):
    counters = [0]

    def mock_randint(a, b):
        counters[0] += 1
        if counters[0] == 1:
            return 12
        return 8
    monkeypatch.setattr(brain_gcd.random, 'randint', mock_randint)
    question, answer = brain_gcd.generate_game()
    assert question == '12 8'
    assert answer == '4'


# brain_prime tests
def test_is_prime():
    assert brain_prime.is_prime(7) is True
    assert brain_prime.is_prime(97) is True
    assert brain_prime.is_prime(2) is True
    assert brain_prime.is_prime(1) is False
    assert brain_prime.is_prime(4) is False


def test_generate_game_prime(monkeypatch):
    monkeypatch.setattr(brain_prime.random, 'randint', lambda a, b: 7)
    question, answer = brain_prime.generate_game()
    assert question == 7
    assert answer == 'yes'


def test_generate_game_composite(monkeypatch):
    monkeypatch.setattr(brain_prime.random, 'randint', lambda a, b: 4)
    question, answer = brain_prime.generate_game()
    assert question == 4
    assert answer == 'no'


# brain_progression tests
def test_generate_game_progression(monkeypatch):
    def mock_randint(a, b):
        if a == -15:
            return 1
        if a == 1:
            return 2
        if a == 5:
            return 5
        return 2
    monkeypatch.setattr(brain_progression.random, 'randint', mock_randint)
    question, answer = brain_progression.generate_game()
    assert '1 3 .. 7 9' == question
    assert answer == '5'


# brain_balance tests
def test_balance_number():
    assert brain_balance.balance_number(123) == '222'
    assert brain_balance.balance_number(156) == '444'
    assert brain_balance.balance_number(9) == '9'
    assert brain_balance.balance_number(111) == '111'


def test_generate_game_balance(monkeypatch):
    monkeypatch.setattr(brain_balance.random, 'randint', lambda a, b: 156)
    question, answer = brain_balance.generate_game()
    assert question == '156'
    assert answer == '444'
