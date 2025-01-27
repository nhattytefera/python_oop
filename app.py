class Employee:
    raise_amount = 1.04
    num_of_emps = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@gmail.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    # @classmethod
    # def set_raise_amt(cls, amount):
    #     cls.raise_amount = amount

    # @classmethod
    # def from_string(cls, emp_str):
    #     first, last, pay = emp_str.split('-')
    #     return cls(first, last, pay)

class Developer(Employee):
    raise_amount = 1.10
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay):
        super().__init__(first, last, pay)


dev1 = Developer('Nati', 'Tefera', 50000, 'JavaScript')
dev2 = Developer('Bruick', 'Tefera', 60000, 'Python')


print(dev1.pay)
dev1.apply_raise()
print(dev1.pay)