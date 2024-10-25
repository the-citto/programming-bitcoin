"""Test ECC."""

# import pytest

from programming_bitcoin.ecc import FieldElement



class TestFieldElement:
    """Test field element."""

    def test_ne(self) -> None:
        a = FieldElement(2, 31)
        b = FieldElement(2, 31)
        c = FieldElement(15, 31)
        assert a == b
        # self.assertEqual(a, b)
        assert a != c
        # self.assertTrue(a != c)
        # self.assertFalse(a != b)

    def test_add(self) -> None:
        a = FieldElement(2, 31)
        b = FieldElement(15, 31)
        assert a + b == FieldElement(17, 31)
        a = FieldElement(17, 31)
        b = FieldElement(21, 31)
        assert a + b == FieldElement(7, 31)

    def test_sub(self) -> None:
        a = FieldElement(29, 31)
        b = FieldElement(4, 31)
        assert a - b == FieldElement(25, 31)
        a = FieldElement(15, 31)
        b = FieldElement(30, 31)
        assert a - b == FieldElement(16, 31)

    def test_mul(self) -> None:
        a = FieldElement(24, 31)
        b = FieldElement(19, 31)
        assert a * b == FieldElement(22, 31)

    def test_pow(self) -> None:
        a = FieldElement(17, 31)
        assert a**3 == FieldElement(15, 31)
        a = FieldElement(5, 31)
        b = FieldElement(18, 31)
        assert a**5 * b == FieldElement(16, 31)

    def test_div(self) -> None:
        a = FieldElement(3, 31)
        b = FieldElement(24, 31)
        assert a / b == FieldElement(4, 31)
        a = FieldElement(17, 31)
        assert a**-3 == FieldElement(29, 31)
        a = FieldElement(4, 31)
        b = FieldElement(11, 31)

