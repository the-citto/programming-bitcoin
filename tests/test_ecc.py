"""Test ECC."""

import typing as t

import pydantic
import pytest

from programming_bitcoin.ecc import FieldElement



@pytest.mark.field_element
class TestFieldElement:
    """Test field element."""

    init_invalid_type = (None, 4.1, (1,), "spam")
    dunders_invalid_objs: tuple[tuple[FieldElement, t.Any], ...] = (
        (FieldElement(0, 2), "eggs"),
        (FieldElement(0, 2), ()),
        (FieldElement(0, 2), set()),
        (FieldElement(0, 2), 1),
    )
    field_sigle_values = (
        (0, 2),
        (1, 3),
        (3, 11),
    )
    fields_diff_all = (
        [FieldElement(1, 2), FieldElement(3, 5)],
        [FieldElement(3, 7), FieldElement(10, 11)],
    )
    fields_diff_el_same_order = (
        [FieldElement(1, 3), FieldElement(2, 3)],
        [FieldElement(4, 11), FieldElement(10, 11)],
    )
    fields_same_el_diff_order = (
        [FieldElement(1, 3), FieldElement(1, 2)],
        [FieldElement(4, 11), FieldElement(4, 13)],
    )

    @pytest.mark.parametrize("el", init_invalid_type)
    def test_init_invalid_el_type(self, el: int) -> None:
        with pytest.raises(pydantic.ValidationError):
            assert isinstance(FieldElement(el, 11), FieldElement)

    @pytest.mark.parametrize("order", [4, 6, 8, 9])
    def test_init_not_primes(self, order: int) -> None:
        with pytest.raises(pydantic.ValidationError):
            assert isinstance(FieldElement(0, order), FieldElement)

    @pytest.mark.parametrize("order", init_invalid_type)
    def test_init_invalid_order_type(self, order: int) -> None:
        with pytest.raises(pydantic.ValidationError):
            assert isinstance(FieldElement(0, order), FieldElement)

    @pytest.mark.parametrize("el", [-1, 100])
    def test_init_invalid_el_val(self, el: int) -> None:
        with pytest.raises(pydantic.ValidationError):
            assert isinstance(FieldElement(el, 2), FieldElement)

    @pytest.mark.parametrize("order", [-1, 0, 1, 4])
    def test_init_invalid_order_val(self, order: int) -> None:
        with pytest.raises(pydantic.ValidationError):
            assert isinstance(FieldElement(0, order), FieldElement)

    @pytest.mark.parametrize("el", [0, 1])
    @pytest.mark.parametrize(
        "order",
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],
    )
    def test_init_order_val(self, el: int, order: int) -> None:
        assert isinstance(FieldElement(el, order), FieldElement)

    @pytest.mark.parametrize(("el", "order"), field_sigle_values)
    def test_init_valid(self, el: int, order: int) -> None:
        assert isinstance(FieldElement(el, order), FieldElement)

    @pytest.mark.parametrize(("field_1", "field_2"), dunders_invalid_objs)
    def test_eq_invalid_object(self, field_1: FieldElement, field_2: object) -> None:
        with pytest.raises(TypeError):
            assert field_1 == field_2

    @pytest.mark.parametrize(("el", "order"), field_sigle_values)
    def test_eq(self, el: int, order: int) -> None:
        field_1 = FieldElement(el, order)
        field_2 = FieldElement(el, order)
        assert field_1 == field_2

    @pytest.mark.parametrize(("field_1", "field_2"), fields_diff_all)
    def test_eq_diff_all(self, field_1: FieldElement, field_2: FieldElement) -> None:
        with pytest.raises(AssertionError):
            assert field_1 == field_2

    @pytest.mark.parametrize(("field_1", "field_2"), fields_diff_el_same_order)
    def test_eq_diff_el(self, field_1: FieldElement, field_2: FieldElement) -> None:
        with pytest.raises(AssertionError):
            assert field_1 == field_2

    @pytest.mark.parametrize(("field_1", "field_2"), fields_same_el_diff_order)
    def test_eq_diff_order(self, field_1: FieldElement, field_2: FieldElement) -> None:
        with pytest.raises(AssertionError):
            assert field_1 == field_2

    @pytest.mark.parametrize(("field_1", "field_2"), dunders_invalid_objs)
    def test_ne_invalid_object(self, field_1: FieldElement, field_2: object) -> None:
        with pytest.raises(TypeError):
            assert field_1 != field_2

    @pytest.mark.parametrize(("field_1", "field_2"), fields_diff_all)
    def test_ne_diff_all(self, field_1: FieldElement, field_2: FieldElement) -> None:
        assert field_1 != field_2

    @pytest.mark.parametrize(("field_1", "field_2"), fields_diff_el_same_order)
    def test_ne_diff_el(self, field_1: FieldElement, field_2: FieldElement) -> None:
        assert field_1 != field_2

    @pytest.mark.parametrize(("field_1", "field_2"), fields_same_el_diff_order)
    def test_ne_diff_order(self, field_1: FieldElement, field_2: FieldElement) -> None:
        assert field_1 != field_2

    @pytest.mark.parametrize(("field_1", "field_2"), dunders_invalid_objs)
    def test_add_invalid_object(self, field_1: FieldElement, field_2: object) -> None:
        with pytest.raises(TypeError):
            assert isinstance(field_1 + field_2, FieldElement)

    @pytest.mark.parametrize(
        ("field_1", "field_2", "expected"),
        [
            (FieldElement(2, 31), FieldElement(16, 31), FieldElement(18, 31)),
            (FieldElement(18, 31), FieldElement(21, 31), FieldElement(8, 31)),
        ],
    )
    def test_add(self, field_1: FieldElement, field_2: FieldElement, expected: FieldElement) -> None:
        assert field_1 + field_2 == expected

    @pytest.mark.parametrize(("field_1", "field_2"), fields_same_el_diff_order)
    def test_add_diff_orders(self, field_1: FieldElement, field_2: FieldElement) -> None:
        with pytest.raises(ArithmeticError):
            assert isinstance(field_1 + field_2, FieldElement)

    @pytest.mark.parametrize(("field_1", "field_2"), dunders_invalid_objs)
    def test_sub_invalid_object(self, field_1: FieldElement, field_2: object) -> None:
        with pytest.raises(TypeError):
            assert isinstance(field_1 - field_2, FieldElement)

    @pytest.mark.parametrize(
        ("field_1", "field_2", "expected"),
        [
            (FieldElement(29, 31), FieldElement(4, 31), FieldElement(25, 31)),
            (FieldElement(15, 31), FieldElement(30, 31), FieldElement(16, 31)),
        ],
    )
    def test_sub(self, field_1: FieldElement, field_2: FieldElement, expected: FieldElement) -> None:
        assert field_1 - field_2 == expected

    @pytest.mark.parametrize(("field_1", "field_2"), fields_same_el_diff_order)
    def test_sub_diff_orders(self, field_1: FieldElement, field_2: FieldElement) -> None:
        with pytest.raises(ArithmeticError):
            assert isinstance(field_1 - field_2, FieldElement)

    @pytest.mark.parametrize(("field_1", "field_2"), dunders_invalid_objs)
    def test_mul_invalid_object(self, field_1: FieldElement, field_2: object) -> None:
        with pytest.raises(TypeError):
            assert isinstance(field_1 * field_2, FieldElement)

    @pytest.mark.parametrize(
        ("field_1", "field_2", "expected"),
        [
            (FieldElement(24, 31), FieldElement(19, 31), FieldElement(22, 31)),
            (FieldElement(15, 31), FieldElement(2, 31), FieldElement(30, 31)),
        ],
    )
    def test_mul(self, field_1: FieldElement, field_2: FieldElement, expected: FieldElement) -> None:
        assert field_1 * field_2 == expected

    @pytest.mark.parametrize(("field_1", "field_2"), fields_same_el_diff_order)
    def test_mul_diff_orders(self, field_1: FieldElement, field_2: FieldElement) -> None:
        with pytest.raises(ArithmeticError):
            assert isinstance(field_1 * field_2, FieldElement)

    @pytest.mark.parametrize("exponent", [1.0, None, (1,)])
    def test_pow_invalid_object(self, exponent: int) -> None:
        err_msg_patt = ".*integer.*"
        with pytest.raises(TypeError, match=err_msg_patt):
            assert isinstance(FieldElement(1, 2) ** exponent, FieldElement)

    @pytest.mark.parametrize(
        ("field", "exponent", "expected"),
        [
            (FieldElement(17, 31), 3, FieldElement(15, 31)),
            (FieldElement(15, 31), 4, FieldElement(2, 31)),
            (FieldElement(15, 31), 0, FieldElement(1, 31)),
        ],
    )
    def test_pow(self, field: FieldElement, exponent: int, expected: FieldElement) -> None:
        assert field**exponent == expected

    @pytest.mark.parametrize(("field_1", "field_2"), dunders_invalid_objs)
    def test_div_invalid_object(self, field_1: FieldElement, field_2: object) -> None:
        with pytest.raises(TypeError):
            assert isinstance(field_1 / field_2, FieldElement)

    @pytest.mark.parametrize(
        ("field_1", "field_2", "expected"),
        [
            (FieldElement(3, 31), FieldElement(24, 31), FieldElement(4, 31)),
            (FieldElement(2, 19), FieldElement(7, 19), FieldElement(3, 19)),
            (FieldElement(7, 19), FieldElement(5, 19), FieldElement(9, 19)),
        ],
    )
    def test_div(self, field_1: FieldElement, field_2: FieldElement, expected: FieldElement) -> None:
        assert field_1 / field_2 == expected

    @pytest.mark.parametrize(("field_1", "field_2"), fields_same_el_diff_order)
    def test_div_diff_orders(self, field_1: FieldElement, field_2: FieldElement) -> None:
        with pytest.raises(ArithmeticError):
            assert isinstance(field_1 / field_2, FieldElement)


@pytest.mark.point
class TestPoint:
    """Test point."""






