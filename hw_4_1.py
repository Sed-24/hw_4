from pathlib import Path

path = Path('C:/Users/Public/Pro/GoIt/hw_4/text.txt')


def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as fh:
            num = []
            while True:
                line = fh.readline().split(',')
                if len(line) == 1:
                    break
                num.append(int(line[1]))

            total = sum(num)
            average = sum(num) // len(num)
            return total, average

    except FileNotFoundError:
        return 'File not found'
    except ZeroDivisionError:
        return 'The file is empty'


print(total_salary(path))
