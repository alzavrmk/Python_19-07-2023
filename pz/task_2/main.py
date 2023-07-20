"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

{
    "orders": []
}

вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""
import json
def write_order_to_json(item, quantity, price, buyer, date):
    dict_order = dict()
    dict_order["item"] = item
    dict_order["quantity"] = quantity
    dict_order["price"] = price
    dict_order["buyer"] = buyer
    dict_order["date"] = date

    with open('orders.json') as f_n:
        obj = json.load(f_n)
        print(type(obj))
        obj["orders"].append(dict_order)
        print(obj)

    with open('orders01.json', 'w') as f_n:
        json.dump(obj, f_n, sort_keys=True, indent=4)




    # with open('orders.json', 'a') as f_n:
    #     json.dump(dict_order, f_n)

write_order_to_json("colon", 5, 1500, "man", "20.07.2023")

