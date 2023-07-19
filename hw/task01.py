# Задание 1.
#
# Создать класс TrafficLight (светофор)
# и определить у него один приватный атрибут color (цвет) и публичный
# метод running (запуск).
#
# В рамках метода running реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный)
# составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
# на ваше усмотрение.
# Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time
#
# Переключение между режимами должно осуществляться только
# в указанном порядке (красный, желтый, зеленый).
#
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

import time
import keyboard


class TrafficLight:
    __color = "red";

    def run(self):

        for i in range(3):

                print("красный");

                time.sleep(1);
                print("желтый");
                time.sleep(1);
                print("зеленый");
                time.sleep(1);


traffic_lights = TrafficLight()
traffic_lights.run();