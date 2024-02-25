import sys
import os
import pytest

app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(app_path)

from app import Geometric


@pytest.fixture
def geometric_fixture():
    return Geometric(p=0.1)


def test_geometric_properties(geometric_fixture):
    assert geometric_fixture.p == 0.1
    assert geometric_fixture.variance == 90.0
    assert geometric_fixture.expected == 10.0
    assert pytest.approx(geometric_fixture.std, 0.0001) == 9.48683298051


def test_geometric_mass(geometric_fixture):
    assert pytest.approx(geometric_fixture.mass(5), 0.0001) == 0.06561
    assert pytest.approx(geometric_fixture.mass(1), 0.00001) == 0.1
    assert pytest.approx(geometric_fixture.mass(10), 0.00001) == 0.0387420489


def test_geometric_cumulative_distribution_two_parameters(geometric_fixture):
    expr_a = ">4"
    expr_b = "<8"
    result = geometric_fixture.cumulative(expr_a, expr_b)
    assert pytest.approx(result, 0.0001) == 0.1778031


def test_geometric_cumulative_distribution_one_parameter(geometric_fixture):
    expr_a = "<=5"
    result = geometric_fixture.cumulative(expr_a)
    assert pytest.approx(result, 0.0001) == 0.40951

    expr_a = "<7"
    result = geometric_fixture.cumulative(expr_a)
    assert pytest.approx(result, 0.0001) == 0.468559
