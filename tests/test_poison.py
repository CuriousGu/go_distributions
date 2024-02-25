import sys
import os
import pytest

app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(app_path)

from app import Poison


@pytest.fixture
def poison_fixture():
    return Poison(frequency=0.73)


def test_poison_properties(poison_fixture):
    assert poison_fixture.frequency == 0.73
    assert poison_fixture.variance == 0.73
    assert poison_fixture.expected == 0.73
    assert pytest.approx(poison_fixture.std, 0.0001) == 0.854400374532


def test_poison_mass(poison_fixture):
    assert pytest.approx(poison_fixture.mass(3), 0.0001) == 0.0312451315997
    assert pytest.approx(poison_fixture.mass(2), 0.00001) == 0.12840465041
    assert pytest.approx(poison_fixture.mass(1), 0.00001) == 0.351793562766


def test_poison_cumulative_distribution_two_parameters(poison_fixture):
    expr_a = ">=1"
    expr_b = "<=8"
    result = poison_fixture.cumulative(expr_a, expr_b)
    assert pytest.approx(result, 0.0001) == 0.518090925617


def test_poison_cumulative_distribution_one_parameter(poison_fixture):
    expr_a = ">2"
    result = poison_fixture.cumulative(expr_a)
    assert pytest.approx(result, 0.0001) == 0.0378927967344
    
    expr_a = "<=1"
    result = poison_fixture.cumulative(expr_a)
    assert pytest.approx(result, 0.0001) == 0.833702552856
