"""ECC."""

import typing as t



# tag::source1[]
class FieldElement:
    """Field element."""

    def __init__(self, num: int, prime: int) -> None:
        """Init."""
        if num >= prime or num < 0:  # <1>
            error = f"Num {num} not in field range 0 to {prime - 1}"
            raise ValueError(error)
        self.num = num  # <2>
        self.prime = prime

    def __repr__(self) -> str:
        """Repr."""
        return f"FieldElement_{self.prime}({self.num})"

    def __eq__(self, other: object) -> bool:
        """Eq."""
        if not isinstance(other, FieldElement):
            raise NotImplementedError
        return self.num == other.num and self.prime == other.prime  # <3>
    # end::source1[]

    def __ne__(self, other: object) -> bool:
        """Ne."""
        if not isinstance(other, FieldElement):
            raise NotImplementedError
        return self.num != other.num or self.prime != other.prime

    # tag::source2[]
    def __add__(self, other: object) -> t.Self:
        """Add."""
        if not isinstance(other, FieldElement):
            raise NotImplementedError
        if self.prime != other.prime:  # <1>
            error = "Cannot add two numbers in different Fields"
            raise TypeError(error)
        num = (self.num + other.num) % self.prime  # <2>
        return self.__class__(num, self.prime)  # <3>
    # end::source2[]

    def __sub__(self, other: object) -> None:
        """Sub."""
        if not isinstance(other, FieldElement):
            raise NotImplementedError
        if self.prime != other.prime:
            error = "Cannot subtract two numbers in different Fields"
            raise TypeError(error)
        # self.num and other.num are the actual values
        # self.prime is what we need to mod against
        # We return an element of the same class
        raise NotImplementedError

    def __mul__(self, other: object) -> None:
        """Mul."""
        if not isinstance(other, FieldElement):
            raise NotImplementedError
        if self.prime != other.prime:
            error = "Cannot multiply two numbers in different Fields"
            raise TypeError(error)
        # self.num and other.num are the actual values
        # self.prime is what we need to mod against
        # We return an element of the same class
        raise NotImplementedError

    # tag::source3[]
    def __pow__(self, exponent: int) -> t.Self:
        """Pow."""
        n = exponent % (self.prime - 1)  # <1>
        num = pow(self.num, n, self.prime)
        return self.__class__(num, self.prime)
    # end::source3[]

    def __truediv__(self, other: object) -> None:
        """Truediv."""
        if not isinstance(other, FieldElement):
            raise NotImplementedError
        if self.prime != other.prime:
            error = "Cannot divide two numbers in different Fields"
            raise TypeError(error)
        # use fermat's little theorem:
        # self.num**(p-1) % p == 1
        # this means:
        # 1/n == pow(n, p-2, p)
        # We return an element of the same class
        raise NotImplementedError



