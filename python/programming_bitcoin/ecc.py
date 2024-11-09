"""ECC."""

import typing as t

import pydantic



class FieldElement(pydantic.BaseModel):
    """Field element."""



class FieldElementSimple:
    """Field element."""

    def __init__(self, num: int, prime: int) -> None:
        """Init."""
        if not isinstance(num, int):
            err_msg = f"{num} is not an integer."
            raise TypeError(err_msg)
        if num >= prime or num < 0:
            error = f"Num {num} not in field range 0 to {prime - 1}"
            raise ValueError(error)
        self.num = num
        self.prime = prime

    @t.override
    def __repr__(self) -> str:
        """Repr."""
        return f"{self.__class__.__name__}_{self.prime}({self.num})"

    @t.override
    def __eq__(self, other: object) -> bool:
        """Eq."""
        if not isinstance(other, type(self)):
            error = f"Type {type(other)} incompatible with {self.__class__.__name__}."
            raise TypeError(error)
        return self.num == other.num and self.prime == other.prime

    @t.override
    def __ne__(self, other: object) -> bool:
        """Ne."""
        if not isinstance(other, type(self)):
            error = f"Type {type(other)} incompatible with {self.__class__.__name__}."
            raise TypeError(error)
        return self.num != other.num or self.prime != other.prime

    def __add__(self, other: object) -> t.Self:
        """Add."""
        if not isinstance(other, type(self)):
            error = f"Type {type(other)} incompatible with {self.__class__.__name__}."
            raise TypeError(error)
        if self.prime != other.prime:
            error = "Cannot add two numbers in different Fields"
            raise ValueError(error)
        num = (self.num + other.num) % self.prime
        return self.__class__(num, self.prime)

    def __sub__(self, other: object) -> None:
        """Sub."""
        if not isinstance(other, type(self)):
            error = f"Type {type(other)} incompatible with {self.__class__.__name__}."
            raise TypeError(error)
        if self.prime != other.prime:
            error = "Cannot subtract two numbers in different Fields"
            raise ValueError(error)
        # self.num and other.num are the actual values
        # self.prime is what we need to mod against
        # We return an element of the same class
        raise NotImplementedError

    def __mul__(self, other: object) -> None:
        """Mul."""
        if not isinstance(other, type(self)):
            error = f"Type {type(other)} incompatible with {self.__class__.__name__}."
            raise TypeError(error)
        if self.prime != other.prime:
            error = "Cannot multiply two numbers in different Fields"
            raise TypeError(error)
        # self.num and other.num are the actual values
        # self.prime is what we need to mod against
        # We return an element of the same class
        raise NotImplementedError

    def __pow__(self, exponent: int) -> t.Self:
        """Pow."""
        n = exponent % (self.prime - 1)
        num = pow(self.num, n, self.prime)
        return self.__class__(num, self.prime)

    def __truediv__(self, other: object) -> None:
        """Truediv."""
        if not isinstance(other, type(self)):
            error = f"Type {type(other)} incompatible with {self.__class__.__name__}."
            raise TypeError(error)
        if self.prime != other.prime:
            error = "Cannot divide two numbers in different Fields"
            raise TypeError(error)
        # use fermat's little theorem:
        # self.num**(p-1) % p == 1
        # this means:
        # 1/n == pow(n, p-2, p)
        # We return an element of the same class
        raise NotImplementedError






