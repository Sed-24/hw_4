from pathlib import Path

path = Path('C:/Users/Public/Pro/GoIt/hw_4/Test/text_cat.txt')


def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as fh:
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
