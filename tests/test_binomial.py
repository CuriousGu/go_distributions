import sys
import os
import pytest

app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(app_path)

from app import Binomial


@pytest.fixture
def binomial_fixture():
    return Binomial(p=0.5, n=10)


def test_binomial_properties(binomial_fixture):
    assert binomial_fixture.p == 0.5
    assert binomial_fixture.n == 10
    assert binomial_fixture.variance == 2.5
    assert binomial_fixture.expected == 5.0
    assert pytest.approx(binomial_fixture.std, 0.0001) == 1.5811


def test_binomial_mass(binomial_fixture):
    assert pytest.approx(binomial_fixture.mass(5), 0.0001) == 0.24609375
    assert pytest.approx(binomial_fixture.mass(0), 0.00001) == 0.0009765625
    assert pytest.approx(binomial_fixture.mass(10), 0.00001) == 0.0009765625


def test_binomial_cumulative_distribution_two_parameter(binomial_fixture):
    expr_a = ">4"
    expr_b = "<8"
    result = binomial_fixture.cumulative(expr_a, expr_b)
    assert pytest.approx(result, 0.0001) == 0.568359375


def test_binomial_cumulative_distribution_one_parameter(binomial_fixture):
    expr_a = ">=5"
    result = binomial_fixture.cumulative(expr_a)
    assert pytest.approx(result, 0.0001) == 0.623046875

    expr_a = "<7"
    result = binomial_fixture.cumulative(expr_a)
    assert pytest.approx(result, 0.0001) == 0.828125
