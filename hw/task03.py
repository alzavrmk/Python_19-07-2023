# Задание 3.
#
# Реализовать базовый класс Worker (работник),
# в котором определить публичные атрибуты name, surname, position (должность),
# и защищенный атрибут income (доход). Последний атрибут должен ссылаться
# на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
#
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
# получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
#
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).
#
# П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку str
# str(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            "wage": 50000,
            "bonus": 10000
        }

    def get_income_wage(self):
        return self._income["wage"]

    def get_income_bonus(self):
        return self._income["bonus"]

    # def get_income(self):
    #     return f'Wage: {self.get_income_wage()}; ' \
    #            f'bonus: {self.get_income_bonus()}'

    def set_income_wage(self, wage, bonus):
        if wage > 0 and bonus >= 0:
            self._income["wage"] = wage
            self._income["bonus"] = bonus

    def __str__(self):
        return f'Name: {self.name};\n'\
               f'Surname: {self.surname};\n' \
               f'position: {self.position};\n'\
               f'Wage: {self.get_income_wage()};\n' \
               f'bonus: {self.get_income_bonus()}.\n' \

class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'Wage: {self.get_income_wage()}; ' \
               f'bonus: {self.get_income_bonus()}'
    # def __str__(self):
    #     return f'{self.get_total_income()}'

worker1 = Worker("Анастасия", "Банщикова", "разработчик")
worker1.set_income_wage(100000, 20000)
print(worker1)

worker = Position("Иванов", "Иван", "менеджер")
worker.set_income_wage(60000, 5000)
print(worker)
print(worker.get_full_name())
print(worker.get_total_income())
