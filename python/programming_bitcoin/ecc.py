"""ECC."""

import typing as t

import pydantic



FieldOrderType = t.Annotated[int, pydantic.Field(strict=True, gt=1)]


class FieldElement(pydantic.BaseModel):
    """Field element."""

    el: pydantic.NonNegativeInt
    order: FieldOrderType

    def __init__(self, el: int, order: int) -> None:
        """Init."""
        super().__init__(el=el, order=order)

    @pydantic.model_validator(mode="after")
    def _valid_values(self) -> t.Self:
        if self.el >= self.order:
            err_msg = f"element {self.el} out of field range '0 to {self.order - 1}'"
            raise ValueError(err_msg)
        return self

    @pydantic.field_validator("order")
    @classmethod
    def _valid_order(cls, order: FieldOrderType) -> FieldOrderType:
        div = 3
        if order <= div:
            return order
        err_msg = f"{order} is not a prime number."
        if order & 1 == 0:
            raise ValueError(err_msg)
        while div * div <= order:
            if order % div == 0:
                raise ValueError(err_msg)
            div += 2
        return order

    # @t.override
    def __eq__(self, other: object) -> bool:
        """Eq."""
        if not isinstance(other, type(self)):
            err_msg = f"Type {type(other)} incompatible with {self.__class__.__name__}."
            raise TypeError(err_msg)
        return self.el == other.el and self.order == other.order

    # @t.override
    def __ne__(self, other: object) -> bool:
        """Ne."""
        if not isinstance(other, type(self)):
            err_msg = f"Type {type(other)} incompatible with {self.__class__.__name__}."
            raise TypeError(err_msg)
        return self.el != other.el or self.order != other.order

    def __add__(self, other: object) -> t.Self:
        """Add."""
        if not isinstance(other, type(self)):
            err_msg = f"Type {type(other)} incompatible with {self.__class__.__name__}."
            raise TypeError(err_msg)
        if self.order != other.order:
            err_msg = "Addition of Fields of different order is not allowed."
            raise ArithmeticError(err_msg)
        el = (self.el + other.el) % self.order
        return self.__class__(el, self.order)

    def __sub__(self, other: object) -> t.Self:
        """Sub."""
        if not isinstance(other, type(self)):
            err_msg = f"Type {type(other)} incompatible with {self.__class__.__name__}."
            raise TypeError(err_msg)
        if self.order != other.order:
            err_msg = "Subtraction of Fields of different order is not allowed."
            raise ArithmeticError(err_msg)
        el = (self.el - other.el) % self.order
        return self.__class__(el, self.order)

    def __mul__(self, other: object) -> t.Self:
        """Mul."""
        if not isinstance(other, type(self)):
            err_msg = f"Type {type(other)} incompatible with {self.__class__.__name__}."
            raise TypeError(err_msg)
        if self.order != other.order:
            err_msg = "Multiplication of Fields of different order is not allowed."
            raise ArithmeticError(err_msg)
        el = (self.el * other.el) % self.order
        return self.__class__(el, self.order)

    def __pow__(self, exponent: int) -> t.Self:
        """Pow."""
        if not isinstance(exponent, int):
            err_msg = "Exponent is not an integer"
            raise TypeError(err_msg)
        field_exp = exponent % (self.order - 1)
        el = pow(base=self.el, exp=field_exp, mod=self.order)
        return self.__class__(el, self.order)

    def __truediv__(self, other: object) -> t.Self:
        """Truediv."""
        if not isinstance(other, type(self)):
            err_msg = f"Type {type(other)} incompatible with {self.__class__.__name__}."
            raise TypeError(err_msg)
        if self.order != other.order:
            err_msg = "Division of Fields of different order is not allowed."
            raise ArithmeticError(err_msg)
        el = (self.el * pow(other.el, self.order - 2, self.order)) % self.order
        return self.__class__(el, self.order)



class Point(pydantic.BaseModel):
    """Point."""

    x: int | None
    y: int | None
    a: int
    b: int

    def __init__(self, a: int, b: int, x: int | None = None, y: int | None = None) -> None:
        """Init."""
        super().__init__(x=x, y=y, a=a, b=b)

    @pydantic.model_validator(mode="after")
    def _valid_values(self) -> t.Self:
        # if self.ev >= self.order:
        #     err_msg = f"element {self.el} out of field range '0 to {self.order - 1}'"
        #     raise ValueError(err_msg)
        return self


    #     if self.x is None and self.y is None:
    #         return
    #     if self.y**2 != self.x**3 + a * x + b:
    #         err_msg = f"({x}, {y}) is not on the curve"
    #         raise ValueError(err_msg)
    #
    # def __eq__(self, other: object) -> bool:
    #     """Eq."""
    #     return self.x == other.x and self.y == other.y \
    #         and self.a == other.a and self.b == other.b
    #
    # def __ne__(self, other: object) -> bool:
    #     """Ne."""
    #     # this should be the inverse of the == operator
    #     return not (self == other)
    #
    # def __repr__(self) -> str:
    #     """Repr."""
    #     if self.x is None:
    #         return "Point(infinity)"
    #     elif isinstance(self.x, FieldElement):
    #         return "Point({},{})_{}_{} FieldElement({})".format(
    #             self.x.num, self.y.num, self.a.num, self.b.num, self.x.prime)
    #     else:
    #         return "Point({},{})_{}_{}".format(self.x, self.y, self.a, self.b)
    #
    # def __add__(self, other):
    #     """Add."""
    #     if self.a != other.a or self.b != other.b:
    #         raise TypeError("Points {}, {} are not on the same curve".format(self, other))
    #     # Case 0.0: self is the point at infinity, return other
    #     if self.x is None:
    #         return other
    #     # Case 0.1: other is the point at infinity, return self
    #     if other.x is None:
    #         return self
    #
    #     # Case 1: self.x == other.x, self.y != other.y
    #     # Result is point at infinity
    #     if self.x == other.x and self.y != other.y:
    #         return self.__class__(None, None, self.a, self.b)
    #
    #     # Case 2: self.x ≠ other.x
    #     # Formula (x3,y3)==(x1,y1)+(x2,y2)
    #     # s=(y2-y1)/(x2-x1)
    #     # x3=s**2-x1-x2
    #     # y3=s*(x1-x3)-y1
    #     if self.x != other.x:
    #         s = (other.y - self.y) / (other.x - self.x)
    #         x = s**2 - self.x - other.x
    #         y = s * (self.x - x) - self.y
    #         return self.__class__(x, y, self.a, self.b)
    #
    #     # Case 4: if we are tangent to the vertical line,
    #     # we return the point at infinity
    #     # note instead of figuring out what 0 is for each type
    #     # we just use 0 * self.x
    #     if self == other and self.y == 0 * self.x:
    #         return self.__class__(None, None, self.a, self.b)
    #
    #     # Case 3: self == other
    #     # Formula (x3,y3)=(x1,y1)+(x1,y1)
    #     # s=(3*x1**2+a)/(2*y1)
    #     # x3=s**2-2*x1
    #     # y3=s*(x1-x3)-y1
    #     if self == other:
    #         s = (3 * self.x**2 + self.a) / (2 * self.y)
    #         x = s**2 - 2 * self.x
    #         y = s * (self.x - x) - self.y
    #         return self.__class__(x, y, self.a, self.b)
    #
    # def __rmul__(self, coefficient):
    #     """Rmul."""
    #     coef = coefficient
    #     current = self  # <1>
    #     result = self.__class__(None, None, self.a, self.b)  # <2>
    #     while coef:
    #         if coef & 1:  # <3>
    #             result += current
    #         current += current  # <4>
    #         coef >>= 1  # <5>
    #     return result




