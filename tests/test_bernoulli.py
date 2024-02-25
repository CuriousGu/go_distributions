import sys
import os
import pytest

app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(app_path)

from app import Bernoulli


@pytest.fixture
def bernoulli_fixture():
    return Bernoulli(p=0.35)


def test_bernoulli_properties(bernoulli_fixture):
    assert bernoulli_fixture.p == 0.35
    assert bernoulli_fixture.expected == 0.35
    assert pytest.approx(bernoulli_fixture.std, 0.0001) == 0.476969600708
    assert pytest.approx(bernoulli_fixture.variance, 0.0001) == 0.2275


def test_bernoulli_mass(bernoulli_fixture):
    assert pytest.approx(bernoulli_fixture.mass(1), 0.0001) == 0.35
    assert pytest.approx(bernoulli_fixture.mass(0), 0.0001) == 0.65


def test_bernoulli_mass_raises_valueerror_not_0_or_1(bernoulli_fixture):
    with pytest.raises(ValueError, match="x must be 0 or 1. To multiple"\
                                         "trials use Binomial Distribution"):
        bernoulli_fixture.mass(2)
