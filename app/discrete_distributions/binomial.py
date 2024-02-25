from app.discrete_distributions.discretes import DiscreteDistributions
from app.discrete_distributions.utils import combinatory


class Binomial(DiscreteDistributions):

    '''
    p : proability of success (float)
    n : number of trials (int)
    '''

    def __init__(self, p: float = 0, n: int = 0) -> None:
        self.__p = p
        self.__n = n
        self.__variance = None
        self.__expected = None
        super().__init__(n_max=n, n_min=0)

    def __str__(self) -> str:
        return f'\nBinomial(p={self.p}, n={self.n})\n'

    @property
    def p(self) -> float:
        return self.__p

    @property
    def n(self) -> float:
        return self.__n

    @property
    def variance(self) -> float:
        if not self.__variance:
            self.__variance = self.p * (1 - self.p) * self.n
        return self.__variance

    @property
    def expected(self) -> float:
        if not self.__expected:
            self.__expected = self.p * self.n
        return self.__expected

    def mass(self, x: int) -> float:
        '''
        x : number of successes (int)
        '''
        comb = combinatory(self.n, x)
        bernoulli_n = (self.p**x) * ((1-self.p)**(self.n-x))

        return comb * bernoulli_n

    @classmethod
    def show_parameters(cls) -> str:
        return f"\n\n{'#'*4} Binomial Distribution {'#'*4}\n"\
                "\nParameters:\n"\
                f"{' '*3}p: proability of success (float)\n"\
                f"{' '*3}n : number of trials (int)\n"\
                f"{' '*3}x : number of successes (int)\n"
