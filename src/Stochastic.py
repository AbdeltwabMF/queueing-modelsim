from math import factorial

EPS = 1e-9

# --------------------  --------------------  --------------------  -------------------- #


class MM1:

    def __init__(self, _lambda, mu):
        # lambda : mean arrival rate
        self.__lambda = eval(_lambda)

        # mu : mean service rate
        self.__mu = eval(mu)

        # rho : mean server utilization
        self.__rho = self.__lambda / self.__mu

    @property
    def capital_p0(self):
        # when rho < 1
        return 1 - self.__rho
        # else TODO: throw an exception

    def capital_p(self, n):
        return self.__rho ** n * self.capital_p0

    # L : Expected number of the customers in the system
    def capital_l(self):
        return self.__lambda * self.capital_w()

    # Lq : Expected number of the customers in the queue
    def capital_lq(self):
        return self.__lambda * self.capital_wq()

    # W : Expected waiting time in the system
    def capital_w(self):
        return 1 / (self.__mu - self.__lambda + EPS)

    # Wq : Expected waiting time in the queue
    def capital_wq(self):
        return self.__rho * self.capital_w()

    # setting variables
    def set_lambda(self, _lambda):
        self.__lambda = eval(_lambda)
        self.__rho = self.__lambda / self.__mu

    def set_mu(self, mu):
        self.__mu = eval(mu)
        self.__rho = self.__lambda / self.__mu

    # getting variables
    def get_lambda(self):
        return self.__lambda

    def get_mu(self):
        return self.__mu

    def get_rho(self):
        return self.__rho

# --------------------  --------------------  --------------------  -------------------- #


class MM1K:

    def __init__(self, _lambda, mu, k):
        # lambda : mean arrival rate
        self.__lambda = eval(_lambda)

        # mu : mean service rate
        self.__mu = eval(mu)

        # rho : mean server utilization
        self.__rho = self.__lambda / self.__mu

        # K : finite capacity buffer
        self.__k = eval(k)

    def capital_p0(self):
        if self.__rho != 1:
            return (1 - self.__rho) / (1 - self.__rho ** (self.__k + 1))
        else:
            return 1 / (self.__k + 1)

    def capital_p(self, n):
        # if n < k
        return self.capital_p0() * self.__rho ** n
        # else TODO: throw an exception

    def lambda_dash(self):
        return self.__lambda * (1 - self.capital_p(self.__k))

    # L : Expected number of the customers in the system
    def capital_l(self):
        if self.__rho == 1:
            return self.__k / 2
        else:
            num = 1 - (self.__k + 1) * self.__rho ** self.__k + self.__k * self.__rho ** (self.__k + 1)
            den = (1 - self.__rho) * (1 - self.__rho ** (self.__k + 1))
        return self.__rho * (num / den)

    # Lq : Expected number of the customers in the queue
    def capital_lq(self):
        return self.capital_wq() * self.lambda_dash()

    # W : Expected waiting time in the system
    def capital_w(self):
        return self.capital_l() / self.lambda_dash()

    # Wq : Expected waiting time in the queue
    def capital_wq(self):
        return self.capital_w() - (1 / self.__mu)

    # setting variables
    def set_lambda(self, _lambda):
        self.__lambda = eval(_lambda)
        self.__rho = self.__lambda / self.__mu

    def set_mu(self, mu):
        self.__mu = eval(mu)
        self.__rho = self.__lambda / self.__mu

    def set_k(self, k):
        self.__k = int(k)

    # getting variables
    def get_lambda(self):
        return self.__lambda

    def get_mu(self):
        return self.__mu

    def get_rho(self):
        return self.__rho

    def get_k(self):
        return self.__k

# --------------------  --------------------  --------------------  -------------------- #


class MMc:

    def __init__(self, _lambda, mu, c):
        self.__lambda = eval(_lambda)
        self.__mu = eval(mu)
        self.__c = eval(c)
        self.__r = self.__lambda / self.__mu
        self.__rho = self.__r / self.__c

    def capital_p0(self):
        acc = 0
        if self.__c > self.__r:
            for i in range(self.__c):
                acc += self.__r ** i / factorial(i)
            acc += self.__c * self.__r ** self.__c / (factorial(self.__c) * (self.__c - self.__r + EPS))
        else:
            for i in range(self.__c):
                acc += (1 // factorial(i)) * self.__r ** i
            acc += (1 // factorial(self.__c)) * self.__r ** self.__c * (
                        (self.__c * self.__mu) / (self.__c * self.__mu - self.__lambda + EPS))
        return round(1 / acc, 6)

    def capital_p(self, n):
        num = self.__lambda ** n
        if 0 <= n < self.__c:
            den = factorial(n) * self.__mu ** n
        else:
            den = self.__c ** (n - self.__c) * factorial(self.__c) * self.__mu ** n
        return (num / den) * self.capital_p0()

    def capital_l(self):
        return round(self.capital_lq() + self.__r, 3)

    def capital_lq(self):
        num = self.__r ** (self.__c + 1) / self.__c
        den = factorial(self.__c) * (1 - self.__r / self.__c + EPS) ** 2
        return round(num * self.capital_p0() / den, 3)

    def capital_w(self):
        return round(self.capital_wq() + 1 / self.__mu, 3)

    def capital_wq(self):
        return round(self.capital_lq() / self.__lambda, 3)

    def set_lambda(self, _lambda):
        self.__lambda = eval(_lambda)
        self.__r = self.__lambda / self.__mu
        self.__rho = self.__r / self.__c

    def set_mu(self, mu):
        self.__mu = eval(mu)
        self.__r = self.__lambda / self.__mu
        self.__rho = self.__r / self.__c

    def set_c(self, c):
        self.__c = int(c)
        self.__rho = self.__r / self.__c

    def get_mu(self):
        return self.__mu

    def get_lambda(self):
        return self.__lambda

    def get_c(self):
        return self.__c

    def get_rho(self):
        return self.__rho

    def get_r(self):
        return self.__r


class MMcK:

    def __init__(self, _lambda, mu, c, k):
        self.__lambda = eval(_lambda)
        self.__mu = eval(mu)
        self.__c = eval(c)
        self.__k = eval(k)

        self.__r = self.__lambda / self.__mu
        self.__rho = self.__r / self.__c

    def capital_p0(self):
        if self.__c != self.__r:
            acc = (1 - self.__rho ** (self.__k + 1 - self.__c)) * self.__r ** self.__c / (
                        factorial(self.__c) * (1 - self.__rho))
        else:
            acc = (self.__k + 1 - self.__c) * self.__r ** self.__c / factorial(self.__c)

        for i in range(self.__c):
            acc += (self.__r ** i / factorial(i))

        return round(1 / acc, 9)

    def capital_p(self, n):
        num = self.__lambda ** n
        if n < self.__c:
            den = factorial(n) * self.__mu ** n
        else:
            den = self.__c ** (n - self.__c) * factorial(self.__c) * self.__mu ** n
        return round(num / den * self.capital_p0(), 9)

    def capital_l(self):
        acc = 0.0
        for i in range(self.__c):
            acc += (self.__c - i) * self.__r ** i / factorial(i)
        return round(self.capital_lq() + self.__c - self.capital_p0() * acc, 9)

    def capital_lq(self):
        acc = 1 - (self.__rho ** (self.__k - self.__c) * (self.__k - self.__c + 1) * (
                    1.0 - self.__rho + EPS) + self.__rho ** (self.__k + 1 - self.__c))
        num = self.__rho * self.__r ** self.__c * self.capital_p0()
        den = factorial(self.__c) * (1.0 - self.__rho + EPS) ** 2
        return round(num / den * acc, 9)

    def capital_w(self):
        return round(self.capital_l() / (self.__lambda * (1 - self.capital_p(self.__k))), 9)

    def capital_wq(self):
        return round(self.capital_lq() / (self.__lambda * (1 - self.capital_p(self.__k))), 9)

    def set_lambda(self, _lambda):
        self.__lambda = eval(_lambda)
        self.__r = self.__lambda / self.__mu
        self.__rho = self.__r / self.__c

    def set_mu(self, mu):
        self.__mu = eval(mu)
        self.__r = self.__lambda / self.__mu
        self.__rho = self.__r / self.__c

    def set_k(self, k):
        self.__k = int(k)

    def set_c(self, c):
        self.__c = int(c)
        self.__rho = self.__r / self.__c

    def get_mu(self):
        return self.__mu

    def get_lambda(self):
        return self.__lambda

    def get_k(self):
        return self.__k

    def get_c(self):
        return self.__c

    def get_rho(self):
        return self.__rho

    def get_r(self):
        return self.__r
