"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""
import re
import  csv

def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = ["Изготовитель системы:", "Название ОС:",
                 "Код продукта","Тип системы:" ]
    for i in range(1, 4):
        f = open(f'info_{i}.txt')
        line = f.read()
        os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
        os_name_reg = re.compile(r'Название ОС:\s*\S*\s\S*')
        os_code_reg = re.compile(r'Код продукта:\s*\S*')
        os_type_reg = re.compile(r'Тип системы:\s*\S*')
        os_prod_list.append(os_prod_reg.findall(line)[0].split()[2])
        os_name_list.append(os_name_reg.findall(line)[0].split()[3])
        os_code_list.append(os_code_reg.findall(line)[0].split()[2])
        os_type_list.append(os_type_reg.findall(line)[0].split()[2])
        main_data.append(f'{os_prod_list[i-1]}, {os_name_list[i-1]}, '
                         f'{os_code_list[i-1]}, {os_type_list[i-1]} ')
        f.close()
    # print(os_prod_list)
    # print(os_name_list)
    # print(os_code_list)
    # print(os_type_list)
    return main_data

def write_to_csv(main_data):
    with open('data.csv',"w") as f:
        f_csv = csv.writer(f)
        f_csv.writerows([main_data])
        # for row in main_data:
        #     f_csv.writerow(row)
        #     print(row)

def read_to_csv():
    with open('data.csv') as f:
        print(f.read())




write_to_csv(get_data())
read_to_csv()