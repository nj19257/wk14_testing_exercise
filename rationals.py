# Program to make a rationals calculator

from math import gcd  # greatest common divisor

class Rational():
    """
    This is a class for storing a rational number. 

    Attributes:
        numer (int): The numerator of the rational number.
        denom (int): The denominator of the rational number.
    """
    def __init__(self, numerator, denominator):
        """
        Constructs a new Rational. 
        
        Parameters:
            numerator (int): The numerator of the rational number.
            denominator (int): The denominator of the rational number. Defaults to 1.
                                ZeroDivisionError is raised if equal to zero.
        """

        if not isinstance(numerator, int):
            raise TypeError

        # Add code

        self.numer = numerator
        self.denom = denominator

    def __str__(self):
        """
        Returns a simple string representation of the Rational.
        """
        return str(self.numer)+"/"+str(self.denom)

    def simplify(self):
        """
        Simplifies the Rational by dividing numerator and denominator by the great common divisor.
        """
        # Add code
        return self

    def __add__(self, other):
        """
        Returns self + other as a new simplified Rational.
        Can accept other as a Rational or an int.
        """
        if not isinstance(other, Rational):
            if isinstance(other, int):
                other = Rational(other)
            else:
                raise TypeError

        new_numer = (self.numer * other.denom) + (other.numer * self.denom)
        new_denom = self.denom * other.denom

        return Rational(new_numer, new_denom).simplify()

    def __sub__(self, other):
        """
        Returns self - other as a new simplified Rational.
        Can accept other as a Rational or an int.
        """
        # Add code
        return

    def __mul__(self, other):
        """
        Returns self * other as a new simplified Rational.
        Can accept other as a Rational or an int.
        """
        # Add code
        return

    def __truediv__(self, other):
        """
        Returns self / other as a new simplified Rational.
        Can accept other as a Rational or an int.
        """
        # Add code
        return

    def square(self):
        """
        Returns self squared as a new simplified Rational.
        """
        return Rational(self.numer ** 2, self.denom ** 2).simplify()

    def cube(self):
        """
        Returns self cubed as a new simplified Rational.
        """
        # Add code
        return

    def power(self, n):
        """
        Returns self raised to power of n as a new simplified Rational if n is an int.
        """
        # Add code
        return

    def ret_float(self, ndigits):
        """
        Returns self as a float rounded to a given precision in decimal digits. 
        Defaults to two decimal places.
        """
        # Add code
        return

    