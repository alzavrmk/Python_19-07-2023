#
class NonNegative:
    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Не может быть отрицательным")
        instance.__dict__[self.my_attr] = value

    def __delete__(self, instance):
        del instance.__dict__[self.my_attr]

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr
class Worker:
    hours = NonNegative()
    rate = NonNegative()
    def __init__(self, name, surname, position, hours, rate):
        self.name = name
        self.surname = surname
        self.position = position
        self.hours = hours
        self.rate = rate

        # if hours < 0 :
        #     raise ValueError("Значение часов не может быть отрицательным")
        # self._hours = hours
        #
        # if rate < 0:
        #     raise ValueError("Значение ставки не может быть отрицательным")
        # self._rate = rate

    def total_profit(self):
        return self.hours * self.rate



    def __str__(self):
        return f'Name: {self.name};\n'\
               f'Surname: {self.surname};\n' \
               f'position: {self.position};\n'




worker1 = Worker("Анастасия", "Банщикова", "разработчик", 10, 10000)
print(worker1.total_profit())
worker1.hours = 10
worker1.rate = 100

print(worker1.total_profit())
