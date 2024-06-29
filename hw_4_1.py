from pathlib import Path

# Перше завдання

path = Path('C:/Users/Public/Pro/GoIt/hw_4')


def total_salary(path):
    file = ''
    for i in path.iterdir():
        if i.suffix in ['.doc', '.docm', '.docx', '.dot', '.rtf', '.txt', '.pdf']:
            file = i.name
    try:

        with open(file, 'r', encoding='utf-8') as fh:
            num = []
            while True:
                line = fh.readline().split(',')
                if len(line) == 1:
                    break
                num.append(int(line[1][:-1]))

            return (sum(num), sum(num) // len(num))

    except FileNotFoundError:
        return 'File not found'


print(total_salary(path))

