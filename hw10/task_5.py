"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import subprocess
import chardet

for sites in ['yandex.ru', 'youtube.com']:
    ARGS = ['ping', sites]
    SITES_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
    for line in SITES_PING.stdout:
        result = chardet.detect(line)
        print(line.decode('cp866'))
