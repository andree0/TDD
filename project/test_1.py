from datetime import datetime
from decimal import Decimal

import pytest
from functions import analyze_pesel, hash_password, fizz_buzz, leap_year, word_wrap


def div(a, b):
    if isinstance(a, str) or isinstance(b, str):
        result = float(a) / float(b)
        if result % 1 == 0:
            return str(int(result))
        return str(result)
    return a / b

def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(2, 0)


@pytest.mark.parametrize("a, b, result", (
    (0, 9, 0),
    (8, 4, 2),
    (7, 2, 3.5),
    (99, 3, 33),
    (5.5, 2.75, 2)
))
def test_div_by_numbers(a, b, result):
    assert div(a, b) == result

def test_div_by_string_values():
    a = '6'
    b = '2'
    result = '3'
    assert div(a, b) == result


def test_pesel_string():
    assert analyze_pesel('55030101230')

def test_pesel_number():
    assert analyze_pesel(55030101230)

@pytest.mark.parametrize("pesel", (
    ('55030101193'),
    (55030101230),
))
def test_pesel_valid(pesel):
    assert analyze_pesel(pesel)['valid']


@pytest.mark.parametrize("pesel, gender", (
    ('55030101193', 'male'),
    (55030101230, 'male'),
))
def test_pesel_digit_sum(pesel, gender):
    assert analyze_pesel(pesel)['gender'] == gender

@pytest.mark.parametrize("pesel, birth_date", (
    ('55030101193', datetime(1955, 3, 1)),
    ('55030101230', datetime(1955, 3, 1)),
))
def test_pesel_birth_date(pesel, birth_date):
    assert analyze_pesel(pesel)['birth_date'] == birth_date


def calculate_vat(gross_price, tax):
    if isinstance(tax, float):
        tax *= 100
    result = (gross_price * tax) / (tax + 100)
    return result

def test_calculate_vat():
    gross_price = 246
    tax = 23
    result = calculate_vat(gross_price, tax)
    assert result == 0.46


@pytest.mark.parametrize("password, result", (
        ('andrzej', None),
        ('Andrzejeee', None),
        ('Andrzej1ee', None),
        ('Andrzej&ee', None),
        ('andrzej&ee', None),
        ('ANDRZEj!EE', None),
        ('ANDRZEj80EE', None),
        ('andrzej80ee', None),
        ('Andej8#ee', None),
))
def test_hash_password(password, result):
    assert hash_password(password) == result

@pytest.mark.parametrize("value, result", (
        (3, '12Fizz'),
        (15, '12Fizz4BuzzFizz78FizzBuzz11Fizz1314FizzBuzz'),
        (5, '12Fizz4Buzz'),
))
def test_fizzbuzz(value, result):
    assert fizz_buzz(value) == result


@pytest.mark.parametrize("year, result", (
        (2000, True),
        (2002, False),
        (2020, True),
        (2024, True),
        (2021, False),
))
def test_leap_year(year, result):
    assert leap_year(year) is result


@pytest.mark.parametrize("string, length, result", (
        ('Ala ma kota.', 10, 'Ala ma ...'),
        ('Ole ole łyse pole, hej!', 15, 'Ole ole łyse ...'),
))
def test_word_wrap(string, length, result):
    assert word_wrap(string, length) == result