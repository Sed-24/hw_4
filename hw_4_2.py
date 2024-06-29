from pathlib import Path

# Перше завдання

path = Path('C:/Users/Public/Pro/GoIt/hw_4/Test')


def get_cats_info(path):
    file = ''
    for i in path.iterdir():
        if i.suffix in ['.doc', '.docm', '.docx', '.dot', '.rtf', '.txt', '.pdf']:
            file = i.name

    try:
        with open(file, 'r', encoding='utf-8') as fh:

            cats = []
            while True:
                line = fh.readline().split(',')
                if len(line) == 1:
                    break
                cats.append({"id": line[0], "name": line[1], "age": line[2][:-1]})
        return cats
    except FileNotFoundError:
        'File not found'


print(get_cats_info(path))
