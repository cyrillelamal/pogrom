# Разработать фрагмент программы, который будет сохранять вводимые
# пользователем данные, по выбору в json, или csv-файле (использовать модули
# csv, json) с использованием протокола менеджеров контекста, а также
# расширенного синтаксиса исключений.
import json
import csv
import sys


fmt = ''
try:
    fmt = sys.argv[1]
except IndexError:
    exit(1)

data = sys.stdin.read()


try:
    path = 'data.csv' if fmt == 'csv' else 'data.json'
    with open(path, 'at') as file:
        if fmt == 'csv':
            writer = csv.writer(file)
            writer.writerow([data])
        else:
            dmp = json.dumps(json.loads(data))
        file.write(dmp)
except FileNotFoundError:
    print("no such file")
    exit(1)
except json.JSONDecodeError:
    print("invalid JSON")
    exit(1)
