import sys
import os
import pytest

app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(app_path)

from app import Pascal


@pytest.fixture
def pascal_fixture():
    return Pascal(p=0.37, k=8)


def test_pascal_properties(pascal_fixture):
    assert pascal_fixture.p == 0.37
    assert pascal_fixture.k == 8
    assert pytest.approx(pascal_fixture.variance, 0.0001) == 36.815193572
    assert pytest.approx(pascal_fixture.expected, 0.0001) == 13.6216216216
    assert pytest.approx(pascal_fixture.std, 0.0001) == 6.06755251909


def test_pascal_mass(pascal_fixture):
    assert pytest.approx(pascal_fixture.mass(30), 0.0001) == 0.0211080236374
    assert pytest.approx(pascal_fixture.mass(20), 0.00001) == 0.0691874790414
    assert pytest.approx(pascal_fixture.mass(10), 0.00001) == 0.00501877114294


def test_pascal_cumulative_distribution_two_parameters(pascal_fixture):
    expr_a = ">=8"
    expr_b = "<=20"
    result = pascal_fixture.cumulative(expr_a, expr_b)
    assert pytest.approx(result, 0.0001) == 0.473457744959


def test_pascal_cumulative_distribution_one_parameter(pascal_fixture):
    expr_a = ">=30"
    result = pascal_fixture.cumulative(expr_a)
    assert pytest.approx(result, 0.0001) == 0.104844431435

    expr_a = "<=36"
    result = pascal_fixture.cumulative(expr_a)
    assert pytest.approx(result, 0.0001) == 0.981113468469
