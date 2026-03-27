import pytest

from brain_games.games import brain_even
from brain_games.games import brain_calc
from brain_games.games import brain_gcd
from brain_games.games import brain_prime
from brain_games.games import brain_progression
from brain_games.games import brain_balance


class TestBrainEven:
    def test_is_even_true(self):
        assert brain_even.is_even(4) is True

    def test_is_even_false(self):
        assert brain_even.is_even(3) is False

    def test_is_even_zero(self):
        assert brain_even.is_even(0) is True

    def test_generate_even_game_even(self, monkeypatch):
        monkeypatch.setattr(brain_even.random, 'randint', lambda a, b: 4)
        question, answer = brain_even.generate_even_game()
        assert question == 4
        assert answer == 'yes'

    def test_generate_even_game_odd(self, monkeypatch):
        monkeypatch.setattr(brain_even.random, 'randint', lambda a, b: 3)
        question, answer = brain_even.generate_even_game()
        assert question == 3
        assert answer == 'no'


class TestBrainCalc:
    def test_calculate_plus(self):
        assert brain_calc.calculate(2, 3, '+') == 5

    def test_calculate_minus(self):
        assert brain_calc.calculate(10, 4, '-') == 6

    def test_calculate_multiply(self):
        assert brain_calc.calculate(3, 4, '*') == 12

    def test_calculate_unknown_operator(self):
        assert brain_calc.calculate(1, 1, '/') is None

    def test_generate_calc_game(self, monkeypatch):
        counters = [0]

        def mock_randint(a, b):
            counters[0] += 1
            if counters[0] == 3:
                return 0
            return 5
        monkeypatch.setattr(brain_calc.random, 'randint', mock_randint)
        question, answer = brain_calc.generate_calc_game()
        assert '5 + 5' == question
        assert answer == '10'

    def test_generate_calc_game_minus(self, monkeypatch):
        def mock_randint(a, b):
            if a == 0:
                return 1
            return 5
        monkeypatch.setattr(brain_calc.random, 'randint', mock_randint)
        question, answer = brain_calc.generate_calc_game()
        assert '5 - 5' == question
        assert answer == '0'


class TestBrainGcd:
    def test_get_gcd(self):
        assert brain_gcd.get_gcd(12, 8) == 4

    def test_get_gcd_coprime(self):
        assert brain_gcd.get_gcd(13, 7) == 1

    def test_get_gcd_same_numbers(self):
        assert brain_gcd.get_gcd(10, 10) == 10

    def test_get_gcd_one_zero(self):
        assert brain_gcd.get_gcd(5, 0) == 5

    def test_generate_gcd_game(self, monkeypatch):
        counters = [0]

        def mock_randint(a, b):
            counters[0] += 1
            if counters[0] == 1:
                return 12
            return 8
        monkeypatch.setattr(brain_gcd.random, 'randint', mock_randint)
        question, answer = brain_gcd.generate_gcd_game()
        assert question == '12 8'
        assert answer == '4'


class TestBrainPrime:
    def test_is_prime_true(self):
        assert brain_prime.is_prime(7) is True

    def test_is_prime_false_one(self):
        assert brain_prime.is_prime(1) is False

    def test_is_prime_false_composite(self):
        assert brain_prime.is_prime(4) is False

    def test_is_prime_two(self):
        assert brain_prime.is_prime(2) is True

    def test_is_prime_large(self):
        assert brain_prime.is_prime(97) is True

    def test_generate_prime_game_prime(self, monkeypatch):
        monkeypatch.setattr(brain_prime.random, 'randint', lambda a, b: 7)
        question, answer = brain_prime.generate_prime_game()
        assert question == 7
        assert answer == 'yes'

    def test_generate_prime_game_composite(self, monkeypatch):
        monkeypatch.setattr(brain_prime.random, 'randint', lambda a, b: 4)
        question, answer = brain_prime.generate_prime_game()
        assert question == 4
        assert answer == 'no'


class TestBrainProgression:
    def test_take_element_of_progression(self):
        assert brain_progression.take_element_of_progression(1, 2, 3) == 7

    def test_generate_progression(self):
        result = brain_progression.generate_progression(1, 2, 5)
        assert result == [1, 3, 5, 7, 9]

    def test_mask_element(self):
        result = brain_progression.mask_element([1, 3, 5, 7, 9], 2)
        assert result == [1, 3, '..', 7, 9]

    def test_generate_progression_game(self, monkeypatch):
        def mock_randint(a, b):
            if a == -15:
                return 1
            if a == 1:
                return 2
            if a == 5:
                return 5
            return 2
        monkeypatch.setattr(brain_progression.random, 'randint', mock_randint)
        question, answer = brain_progression.generate_progression_game()
        assert '1 3 .. 7 9' == question
        assert answer == '5'


class TestBrainBalance:
    def test_balance_number_simple(self):
        assert brain_balance.balance_number(123) == '222'

    def test_balance_number_with_remainder(self):
        assert brain_balance.balance_number(156) == '444'

    def test_balance_number_single_digit(self):
        assert brain_balance.balance_number(9) == '9'

    def test_balance_number_equal_digits(self):
        assert brain_balance.balance_number(111) == '111'

    def test_generate_balance_game(self, monkeypatch):
        monkeypatch.setattr(brain_balance.random, 'randint', lambda a, b: 156)
        question, answer = brain_balance.generate_balance_game()
        assert question == '156'
        assert answer == '444'
