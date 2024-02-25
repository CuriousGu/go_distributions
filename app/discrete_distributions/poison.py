from app.discrete_distributions.discretes import DiscreteDistributions
from math import e
from app.discrete_distributions.utils import factorial


class Poison(DiscreteDistributions):

    '''
    frequency : average occurrences (float)
    '''

    def __init__(self, frequency: float) -> None:
        self.__frequency = frequency
        self.__variance = None
        self.__expected = None
        super().__init__(n_min=0, n_max=int(frequency*50))

    def __str__(self) -> str:
        return f'Poison(frequency={self.frequency})'

    @property
    def frequency(self) -> float:
        return self.__frequency

    @property
    def variance(self) -> float:
        if not self.__variance:
            self.__variance = self.frequency
        return self.__variance

    @property
    def expected(self) -> float:
        if not self.__expected:
            self.__expected = self.frequency
        return self.__expected

    def mass(self, x: int) -> float:
        '''
        x : number of successes (int)
        '''
        numerator = (e**(-self.frequency)) * (self.frequency**x)
        denominator = factorial(x)
        return numerator / denominator

    @classmethod
    def show_parameters(cls) -> str:
        return f"\n\n{'#'*4} Poison Distribution {'#'*4}\n"\
                "\nParameters:\n"\
                f"{' '*3}frequency: average occurrences (float)\n"
