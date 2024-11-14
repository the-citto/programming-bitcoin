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





