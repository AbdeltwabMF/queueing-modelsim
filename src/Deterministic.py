from math import floor

EPS = 1e-9


class DD1K:

    def __init__(self, _lambda, mu, k, initial_customers=0):
        self.__lambda = eval(_lambda)
        self.__mu = eval(mu)
        self.__k = int(k)
        self.__initial_customers = int(initial_customers)

        self.customer_limit = 100
        self.time_limit = 100

        self.customer_arrival_time = []  # DONE
        self.system_size_per_time = []  # DONE
        self.balking_list = {}  # DONE
        self.queue_time = []  # DONE
        self.total_time = []  # DONE
        self.departures = []  # DONE

        # calculating ti
        if self.__lambda > self.__mu:
            self.__ti = self.ti_case_1()
        elif self.__lambda == self.__mu:
            self.__ti = 0
        else:
            self.__ti = self.ti_case_2()

        # queue waiting time for each customer
        self.queue_time = [0] * self.customer_limit
        for i in range(self.customer_limit):
            self.queue_time[i] = self.wq(i)

        # calculate customer arrival time up to customers limit
        self.customer_arrival_time = [0] * self.customer_limit
        for i in range(1, self.customer_limit):
            self.customer_arrival_time[i] = self.customer_arrival_time[i - 1] + 1 / self.__lambda

        if self.__lambda >= self.__mu:
            # the time of occurrence of all balking processes  "Time":"number of balking process so far"
            # balking list construction
            service_time = 1 / self.__lambda
            balk_counter = 0
            system_size_per_customer = 1

            # step = multiple of lambda
            for i in range(1, self.customer_limit):
                if i / self.__lambda >= service_time:
                    service_time += 1 / self.__mu
                else:
                    system_size_per_customer += 1

                if system_size_per_customer >= self.__k:
                    balk_counter += 1
                    self.balking_list[i / self.__lambda] = balk_counter
                    system_size_per_customer -= 1

            # Number of Customers in System Per unit
            self.system_size_per_time = [0] * self.time_limit
            for i in range(self.time_limit):
                for member in self.balking_list:
                    if member > i:
                        self.system_size_per_time[i] -= self.balking_list[member] - 1
                        break

                if self.__initial_customers == 0:
                    self.system_size_per_time[i] += self.f_without_m(i)
                else:
                    self.system_size_per_time[i] += self.f_with_m(i)
        else:
            departure_so_far = 0
            arrivals_so_far = self.__initial_customers
            system_size_so_far = self.__initial_customers
            arrival_time = 1 / self.__lambda
            self.system_size_per_time = [0] * self.time_limit
            self.system_size_per_time[0] = self.__initial_customers

            # step = multiple of mu
            for i in range(1, self.time_limit):
                self.system_size_per_time[i] = arrivals_so_far - departure_so_far

                if system_size_so_far > 0:
                    departure_so_far += 1
                    system_size_so_far -= 1

                if i >= arrival_time:
                    arrivals_so_far += 1
                    arrival_time += 1 / self.__lambda
                    system_size_so_far += 1

        self.total_time = [0] * self.customer_limit
        self.departures = [0] * self.customer_limit

        for i in range(self.customer_limit):
            self.total_time[i] = 1 / self.__mu + self.queue_time[i]
            self.departures[i] = self.total_time[i] + self.customer_arrival_time[i]

    @staticmethod
    def unstable_system():
        print("The queues will tend to infinity as Lambda is greater than 1 times Mu")

    # m here stands for initial customers number
    def f_without_m(self, t):
        return int(int(t * self.__lambda) - int((t * self.__mu) - (self.__mu / self.__lambda) + EPS))

    def f_with_m(self, t):
        return int(self.__initial_customers + floor(self.__lambda * t) - floor(self.__mu * t))

    def waiting_time_1(self, n):
        return int(1 / self.__mu - 1 / self.__lambda + EPS) * (n - 1)

    # {time when the service starts for customer n} – {time when the customer n arrives}
    def waiting_time_2(self, n):
        return (self.__initial_customers + n - 1) * (1 / self.__mu) - self.time_corresponding_to_customer(n)

    @property
    def first_balked_customer(self):
        return floor(self.customer_corresponding_to_time(self.get_ti()))

    def customer_corresponding_to_time(self, t):
        t = float(t)
        return int(self.__lambda * t)

    def time_corresponding_to_customer(self, customer):
        return floor(int(customer) / self.__lambda)

    # -- ti represents the time of occurrence of the first balk -- #
    def ti_case_1(self):
        # Find the integer value of ti using bi-section method
        _l, _r, _mid = 0, 1e10, 0
        while _l < _r:
            _mid = (_l + _r) // 2

            if self.__initial_customers == 0:
                small_k = self.f_without_m(_mid)
            else:
                small_k = self.f_with_m(_mid)

            if small_k == self.__k:
                _r = _mid
            elif small_k < self.__k:
                _l = _mid + 1
            else:
                _r = _mid - 1

        return int(_l)

    def ti_case_2(self):
        _l, _r, _mid = 0, 1e10, 0
        while _l < _r:
            _mid = (_l + _r) // 2
            small_k = floor(self.__mu * _mid) - floor(self.__lambda * _mid)
            if small_k == self.__initial_customers:
                _r = _mid
            elif small_k < self.__initial_customers:
                _l = _mid + 1
            else:
                _r = _mid - 1

        return int(_l)

    def is_lambda_mul_of_mu(self):
        temp = self.__lambda / self.__mu
        return temp - int(temp) < EPS

    # n(t)
    def nt(self, t):
        t = int(t)
        if self.__lambda > self.__mu:
            if t < 1 / self.__lambda:
                return self.__initial_customers
            elif 1 / self.__lambda <= t < self.get_ti():
                if self.__initial_customers == 0:
                    return self.f_without_m(t)
                else:
                    return self.f_with_m(t)
            else:  # steady state
                if self.is_lambda_mul_of_mu():
                    return self.__k - 1
                else:
                    if t < self.time_corresponding_to_customer(self.customer_limit):
                        return self.system_size_per_time[t]
                    else:
                        return self.__k - 1, self.__k - 2
        else:
            if self.__initial_customers == 0:
                if self.is_lambda_mul_of_mu():
                    return 0 if t < 1 / self.__lambda else 1
                elif t < self.time_corresponding_to_customer(self.customer_limit):
                    return self.system_size_per_time[t]
                else:
                    return 0, 1
            else:
                if self.is_lambda_mul_of_mu():
                    return self.__initial_customers
                else:
                    if t < self.get_ti():
                        return self.f_with_m(t)
                    elif t < self.time_corresponding_to_customer(self.customer_limit):
                        return self.system_size_per_time[t]
                    else:
                        return 0, 1

    def average_waiting(self):
        return (self.__initial_customers - 1) / (2 * self.__mu)

    # Wq(n)
    def wq(self, n):
        if self.__lambda > self.__mu:
            if n == 0 and self.__initial_customers == 0:
                return 0
            elif n == 0 and self.__initial_customers != 0:
                return self.average_waiting()

            if n < self.first_balked_customer:
                return self.waiting_time_1(n)
            else:
                if self.is_lambda_mul_of_mu():
                    return self.waiting_time_1(self.first_balked_customer - 1)
                else:
                    if self.__initial_customers == 0:
                        if (self.time_corresponding_to_customer(n) - 1 / self.__lambda) % (1 / self.__mu) == 0:
                            return self.waiting_time_1(self.first_balked_customer - 1)
                        else:
                            return self.waiting_time_1(self.first_balked_customer - 2)
                    else:
                        if self.time_corresponding_to_customer(n) % (1 / self.__mu) == 0:
                            return self.waiting_time_1(self.first_balked_customer - 1)
                        else:
                            return self.waiting_time_1(self.first_balked_customer - 2)
        else:
            if n == 0:
                return self.average_waiting()

            if self.__initial_customers == 0:
                return 0
            else:
                if n <= floor(self.__lambda * self.get_ti()):
                    return self.waiting_time_2(n)
                else:
                    return 0

    def set_lambda(self, _lambda):
        self.__lambda = eval(_lambda)

    def set_mu(self, mu):
        self.__mu = eval(mu)

    def set_k(self, k):
        self.__k = int(k)

    def set_initial_customers(self, initial_customers):
        self.__initial_customers = int(initial_customers)

    def set_customer_limit(self, cl):
        self.customer_limit = int(cl)

    def set_time_limit(self, t):
        self.time_limit = int(t)

    def get_lambda(self):
        return self.__lambda

    def get_mu(self):
        return self.__mu

    def get_k(self):
        return self.__k

    def get_initial_customers(self):
        return self.__initial_customers

    def get_ti(self):
        return self.__ti
