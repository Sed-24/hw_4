import sys
from pathlib import Path
from colorama import Fore


def directory_and_file(path, indent=0):

    # Перевірка, чи шлях існує і є директорією
    if not path.exists() or not path.is_dir():
        print(Fore.GREEN + f"Шлях {path} не існує або не директорія.")
        return

    print(" " * indent + Fore.YELLOW + f"{path.name}/")

    for item in path.iterdir():

        if item.is_dir():
            print(" " * (indent + 2) + Fore.CYAN + f"{item.name}/")
            directory_and_file(item, indent + 4)

        elif item.is_file():
            print(" " * (indent + 2) + Fore.BLUE + f"{item.name}")


if __name__ == "__main__":
    if len(sys.argv) != 1:
        print(Fore.RED + "Потрібен шлях.")
        sys.exit(1)

    path = Path('C:/Users/Public/Pro/GoIt/hw_4/Test')

    directory_and_file(path)
