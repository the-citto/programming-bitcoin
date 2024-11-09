"""Test ECC."""

import typing as t

import pytest

from programming_bitcoin.ecc import FieldElement



class TestFieldElement:
    """Test field element."""

    excepts_init = (
        "vals",
        [
            (3, 2),
            (4, 3),
            (-4, 3),
        ],
    )
    params_compare = (
        "vals_1, vals_2",
        [
            ((2, 31), (15, 31)),
            ((2, 29), (5, 11)),
        ],
    )
    excepts_type = (
        "field, obj",
        [
            (FieldElement(1, 2), 1),
            (FieldElement(1, 2), "eggs"),
            (FieldElement(1, 2), (1, 2)),
        ],
    )
    params_calcs = (
        "field_1, field_2, expected",
        [
            (FieldElement(1, 13), FieldElement(2, 13), FieldElement(3, 13)),
        ],
    )
    excepts_calcs = (
        "field_1, field_2",
        [
            (FieldElement(1, 13), FieldElement(2, 11)),
        ],
    )


    @pytest.mark.parametrize(*excepts_init)
    def test_init_except(self, vals: tuple[int, int]) -> None:
        reg = r"Num [-\d]+ not in field range 0 to [\d]+"
        with pytest.raises(ValueError, match=reg):
            _ = FieldElement(*vals)

    @pytest.mark.parametrize(*params_compare)
    def test_eq(self, vals_1: tuple[int, int], vals_2: tuple[int, int]) -> None:
        _ = vals_2
        fe_1 = FieldElement(*vals_1)
        fe_2 = FieldElement(*vals_1)
        assert fe_1 == fe_2

    @pytest.mark.xfail
    @pytest.mark.parametrize(*params_compare)
    def test_eq_fail(self, vals_1: tuple[int, int], vals_2: tuple[int, int]) -> None:
        fe_1 = FieldElement(*vals_1)
        fe_2 = FieldElement(*vals_2)
        assert fe_1 == fe_2

    @pytest.mark.parametrize(*params_compare)
    def test_eq_except(self, vals_1: tuple[int, int], vals_2: tuple[int, int]) -> None:
        _ = vals_2
        fe_1 = FieldElement(*vals_1)
        with pytest.raises(TypeError):
            assert fe_1 == "foo"

    @pytest.mark.parametrize(*excepts_type)
    def test_eq_type(self, field: FieldElement, obj: t.Any) -> None:
        with pytest.raises(TypeError):
            assert field == obj

    @pytest.mark.parametrize(*params_compare)
    def test_ne(self, vals_1: tuple[int, int], vals_2: tuple[int, int]) -> None:
        fe_1 = FieldElement(*vals_1)
        fe_2 = FieldElement(*vals_2)
        assert fe_1 != fe_2

    @pytest.mark.xfail
    @pytest.mark.parametrize(*params_compare)
    def test_ne_fail(self, vals_1: tuple[int, int], vals_2: tuple[int, int]) -> None:
        _ = vals_2
        fe_1 = FieldElement(*vals_1)
        fe_2 = FieldElement(*vals_1)
        assert fe_1 != fe_2

    @pytest.mark.parametrize(*params_compare)
    def test_ne_except(self, vals_1: tuple[int, int], vals_2: tuple[int, int]) -> None:
        _ = vals_2
        fe_1 = FieldElement(*vals_1)
        with pytest.raises(TypeError):
            assert fe_1 == "foo"

    @pytest.mark.parametrize(*excepts_type)
    def test_ne_type(self, field: FieldElement, obj: t.Any) -> None:
        with pytest.raises(TypeError):
            assert field != obj

    def test_add(self) -> None:
        a = FieldElement(2, 31)
        b = FieldElement(15, 31)
        assert a + b == FieldElement(17, 31)
        a = FieldElement(17, 31)
        b = FieldElement(21, 31)
        assert a + b == FieldElement(7, 31)

    # def test_sub(self) -> None:
    #     a = FieldElement(29, 31)
    #     b = FieldElement(4, 31)
    #     assert a - b == FieldElement(25, 31)
    #     a = FieldElement(15, 31)
    #     b = FieldElement(30, 31)
    #     assert a - b == FieldElement(16, 31)
    #
    # def test_mul(self) -> None:
    #     a = FieldElement(24, 31)
    #     b = FieldElement(19, 31)
    #     assert a * b == FieldElement(22, 31)
    #
    # def test_pow(self) -> None:
    #     a = FieldElement(17, 31)
    #     assert a**3 == FieldElement(15, 31)
    #     a = FieldElement(5, 31)
    #     b = FieldElement(18, 31)
    #     assert a**5 * b == FieldElement(16, 31)
    #
    # def test_div(self) -> None:
    #     a = FieldElement(3, 31)
    #     b = FieldElement(24, 31)
    #     assert a / b == FieldElement(4, 31)
    #     a = FieldElement(17, 31)
    #     assert a**-3 == FieldElement(29, 31)
    #     a = FieldElement(4, 31)
    #     b = FieldElement(11, 31)



