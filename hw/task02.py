# Задание 2.
#
# Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
# length (длина в метрах), width (ширина в метрах).
#
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
#
# Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
# всего дорожного полотна.
#
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
# метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
# Массу и толщину сделать публичными атрибутами.
# Проверить работу метода.
#
# Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
class Road:
    # __length = 0;
    # __width = 0;
    def __init__(self, width, length):
        self.__length = length
        self.__width = width

    def __repr__(self):
        return f'Road: length = {self.__length} width = {self.__width}'

    def get_mass(self, weigth1,  coating_thickness):
        return self.__length * self.__width * weigth1 * coating_thickness
road = Road(20, 1)
print(road)
print(f'Масса покрытия равна {road.get_mass(25, 0.3)}')