class DiscreteDistributions:
    def __init__(self, n_max, n_min) -> None:
        self.n_max = n_max
        self.n_min = n_min
        self.__std = None

    @property
    def std(self) -> float:
        if not self.__std:
            self.__std = self.variance**0.5
        return self.__std

    def cumulative(self, expr_a: str, expr_b: str = ">-1") -> float:
        '''
        expr_a : The probability expression, Eg: ">=5" or "<27" (str)
        expr_b: The same as expr_a. So it's possible to apply an interval using both (str)
        '''
        prob = 0
        stopper = True

        for it in range(self.n_min, self.n_max + 1):
            if eval('it' + expr_a) and eval('it' + expr_b) and stopper:
                iter_mass = self.mass(it)
                prob += iter_mass

                stopper = iter_mass > 1e-8

        return prob
