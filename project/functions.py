import hashlib
from datetime import datetime
from decimal import Decimal


def div(a, b):
    return a / b


def analyze_pesel(pesel):
    if isinstance(pesel, int):
        pesel = str(pesel)
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    weight_index = 0
    digits_sum = 0
    for digit in pesel[:-1]:
        digits_sum += int(digit) * weights[weight_index]
        weight_index += 1
    pesel_modulo = digits_sum % 10
    validate = 10 - pesel_modulo
    if validate == 10:
        validate = 0
    gender = "male" if int(pesel[-2]) % 2 != 0 else "female"
    if int(pesel[2]) == 2 or int(pesel[2]) == 3:
        birth_year = int("20" + pesel[0:2])
    elif int(pesel[2]) == 4 or int(pesel[2]) == 5:
        birth_year = int("21" + pesel[0:2])
    elif int(pesel[2]) == 6 or int(pesel[2]) == 7:
        birth_year = int("22" + pesel[0:2])
    elif int(pesel[2]) == 8 or int(pesel[2]) == 9:
        birth_year = int("18" + pesel[0:2])
    else:
        birth_year = int("19" + pesel[0:2])
    birth_date = datetime(
        birth_year,
        int(pesel[2:4]),
        int(pesel[4:6]),
    )
    result = {
        "pesel": pesel,
        "valid": validate == int(pesel[-1]),
        "gender": gender,
        "birth_date": birth_date,
    }
    return result

def calculate_vat(gross_price, tax):
    if isinstance(tax, float):
        result = Decimal((Decimal(gross_price) / (Decimal(tax) + 1)) * (Decimal(tax) / 100))
    else:
        result = (gross_price / (tax / 100 + 1)) * tax
    return result

def test_calculate_vat():
    gross_price = 246
    tax = 0.23
    result = calculate_vat(gross_price, tax)
    assert result == 46


def hash_password(password):
    special_mark = """!@#$%^&*()_+-={}[]|\:";'<>?,./"""
    if isinstance(password, int) or isinstance(password, float):
        password = str(password)
    if len(password) < 8:
        return None
    elif not any(mark.isupper() for mark in password):
        return None
    elif not any(mark.islower() for mark in password):
        return None
    elif not any(mark.isdigit() for mark in password):
        return None
    elif any(mark in special_mark for mark in password) is False:
        return None
    else:
        return hashlib.md5(password.encode()).hexdigest()


def fizz_buzz(value):
    result = ''
    for i in range(1, value + 1):
        if i % 3 == 0:
            result += 'Fizz'
        if i % 5 == 0:
            result += 'Buzz'
        if i % 3 != 0 and i % 5 != 0:
            result += str(i)
    return result


def leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False


def word_wrap(string, length):
    if string[length] == ' ':
        new_string = string[:length] + ' ...'
    else:
        cut = string[0:length-1].rindex(' ')
        new_string = string[:cut] + ' ...'
    return new_string


def prime_factors(n):
    pass