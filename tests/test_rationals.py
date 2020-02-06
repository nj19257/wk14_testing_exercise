import pytest
from rationals import Rational


def test_constructor():
    assert str(Rational(3, 4)) == "3/4"

def test_constructor_default_denom():
    assert str(Rational(3) == "3/1")

def test_constructor_numer_type_error():
    with pytest.raises(TypeError):
        Rational(3.4, 3)

def test_constructor_denom_type_error():
    with pytest.raises(TypeError):
        Rational(3, 3.4)

def test_constructor_denom_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        Rational(3, 0)

def test_constructor_negative():
    assert str(Rational(3, -4)) == "-3/4"

def test_simplify():
    assert str(Rational(3, 12).simplify()) == "1/4"

def test_add():
    a = Rational(3, 4)
    b = Rational(5, 6)
    assert str(a + b) == "19/12"

def test_add_type_error():
    a = Rational(3, 4)
    with pytest.raises(TypeError):
        a + 4.5

def test_add_int():
    a = Rational(3, 4)
    assert str(a + 2) == "11/4"

def test_sub():
    a = Rational(3, 4)
    b = Rational(5, 6)
    assert str(b - a) == "1/12"

def test_sub_type_error():
    a = Rational(3, 4)
    with pytest.raises(TypeError):
        a - 4.5

def test_sub_int():
    a = Rational(9, 4)
    assert str(a - 2) == "1/4"

def test_mul():
    a = Rational(3, 4)
    b = Rational(5, 6)
    assert str(a * b) == "5/8"

def test_mul_type_error():
    a = Rational(3, 4)
    with pytest.raises(TypeError):
        a * 4.5

def test_mul_int():
    a = Rational(9, 4)
    assert str(a * 2) == "9/2"

def test_truediv():
    a = Rational(3, 4)
    b = Rational(5, 6)
    assert str(a / b) == "9/10"

def test_truediv_type_error():
    a = Rational(3, 4)
    with pytest.raises(TypeError):
        a / 4.5

def test_truediv_int():
    a = Rational(9, 4)
    assert str(a / 2) == "9/8"

def test_square():
    assert str(Rational(3, 4).square()) == "9/16"

def test_cube():
    assert str(Rational(3, 4).cube()) == "27/64" 

def test_power():
    assert str(Rational(3, 4).power(5)) == "243/1024"

def test_power_square():
    a = Rational(17, 23)
    assert str(a.square()) == str(a.power(2))

def test_power_type_error():
    a = Rational(17, 23)
    with pytest.raises(TypeError):
        a.power(4.3)

def test_ret_float():
    assert Rational(3, 4).ret_float() == 0.75

def test_ret_float_default_ndigits():
    assert Rational(1, 3).ret_float() == 0.33

def test_ret_float_ndigits():
    assert Rational(1, 3).ret_float(6) == 0.333333
