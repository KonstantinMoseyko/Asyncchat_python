"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""

import yaml

DATA_IN = {'items': ['table', 'chair', 'door', 'window'],
           'items_quantity': 4,
           'items_price': {'table': '120₽',
                           'chair': '100₽',
                           'door': '2450₽',
                           'window': '2089₽'}
           }

with open('file.yaml', 'w', encoding='utf-8') as f_in:
    yaml.dump(DATA_IN, f_in, default_flow_style=False, allow_unicode=True, sort_keys=False
)

with open("file.yaml", 'r', encoding='utf-8') as f_out:
    DATA_OUT = yaml.load(f_out, Loader=yaml.SafeLoader)

print(DATA_IN == DATA_OUT)
