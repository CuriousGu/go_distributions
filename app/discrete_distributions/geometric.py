from app.discrete_distributions.discretes import DiscreteDistributions


class Geometric(DiscreteDistributions):

    '''
    p : proability of success (float)
    '''

    def __init__(self, p: float) -> None:
        self.__p = p
        self.__variance = None
        self.__expected = None
        super().__init__(n_min=1, n_max=int(self.expected)*50)

    def __str__(self) -> str:
        return f'Geometric(p={self.p})'

    @property
    def p(self) -> float:
        return self.__p

    @property
    def variance(self) -> float:
        if not self.__variance:
            self.__variance = (1-self.p) / round(self.p**2, 6)
        return self.__variance

    @property
    def expected(self) -> float:
        if not self.__expected:
            self.__expected = 1 / self.p
        return self.__expected

    def mass(self, x: int) -> float:
        '''
        x : number of trials (int)
        '''
        prob = self.p * ((1-self.p)**(x-1))
        return prob

    @classmethod
    def show_parameters(cls) -> str:
        return f"\n\n{'#'*4} Geometric Distribution {'#'*4}\n"\
                "\nParameters:\n"\
                f"{' '*3}p: proability of success (float)\n"\
                f"{' '*3}n : number of trials (int)\n"
