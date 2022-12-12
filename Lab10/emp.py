# SuperClass
class Employee:
    def __init__(self, emp_name, emp_number):
        self.name = emp_name
        self.number = emp_number

    def set_emp_name(self, e_name):
        self.name = e_name

    def set_emp_number(self, e_number):
        self.number = e_number

    def get_emp_name(self):
        return self.name

    def get_emp_number(self):
        return self.number


# Subclass
class ProductionWorker(Employee):
    def __init__(self, worker_shift_num, worker_pay_rate, worker_name, worker_number):
        self.shift = worker_shift_num
        self.pay = worker_pay_rate
        super().__init__(worker_name, worker_number)

    def set_shift_num(self, shift_num):
        self.shift = shift_num

    def set_hourly_pay_rate(self, pay_rate):
        self.pay = pay_rate

    def get_shift_num(self):
        return self.shift

    def get_hourly_pay_rate(self):
        return self.pay
