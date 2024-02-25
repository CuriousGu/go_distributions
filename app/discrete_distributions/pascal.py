from app.discrete_distributions.discretes import DiscreteDistributions
from app.discrete_distributions.utils import combinatory


class Pascal(DiscreteDistributions):

    '''
    p : proability of success (float)
    k : expected number of success (int)
    '''

    def __init__(self, p: float, k: int) -> None:
        self.__p = p
        self.__k = k
        self.__variance = None
        self.__expected = None
        super().__init__(n_min=k, n_max=int(self.expected*50))

    def __str__(self) -> str:
        return f'Pascal(p={self.p}, k={self.k})'

    @property
    def p(self) -> float:
        return self.__p

    @property
    def k(self) -> int:
        return self.__k

    @property
    def variance(self) -> float:
        if not self.__variance:
            self.__variance = self.k * (1-self.p) / (self.p**2)
        return self.__variance

    @property
    def expected(self) -> float:
        if not self.__expected:
            self.__expected = self.k * (1 - self.p) / self.p
        return self.__expected

    def mass(self, x: int) -> float:
        '''
        x : number of trials (int)
        '''
        comb = combinatory(x-1, self.k-1)
        return comb * (self.p ** self.k) * ((1 - self.p) ** (x - self.k))

    @classmethod
    def show_parameters(cls) -> str:
        return f"\n\n{'#'*4} Pascal Distribution {'#'*4}\n"\
                "\nParameters:\n"\
                f"{' '*3}p: proability of success (float)\n"\
                f"{' '*3}k : expected number of success (int)\n"\
                f"{' '*3}x : number of trials (int)"
