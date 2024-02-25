from app.discrete_distributions.discretes import DiscreteDistributions

'''
    p : proability of success (float)
'''


class Bernoulli(DiscreteDistributions):

    def __init__(self, p: float = 0) -> None:
        self.__p = p
        self.__variance = None
        self.__expected = None
        super().__init__(None, None)

    def __str__(self) -> str:
        return f'Bernoulli(p={self.p})'

    @property
    def p(self) -> float:
        return self.__p

    @property
    def expected(self) -> float:
        if not self.__expected:
            self.__expected = self.p
        return self.__expected

    @property
    def variance(self) -> float:
        if not self.__variance:
            self.__variance = self.p * (1 - self.p)
        return self.__variance

    def mass(self, x: int) -> float:
        if x == 1:
            return self.p
        elif x == 0:
            return 1 - self.p
        else:
            raise ValueError("x must be 0 or 1. To multiple" \
                             "trials use Binomial Distribution")

    @classmethod
    def show_parameters(cls) -> str:
        return f"\n\n{'#'*4} Bernoulli Distribution {'#'*4}\n"\
                "\nParameters:\n"\
                f"{' '*3}proability of success (float)\n\n"
