import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)

def print_directory_tree(path, prefix=""):
    try:
        items = sorted(
            path.iterdir(),
            key = lambda items: (not items.is_dir(), items.name.lower())
        )
    except PermissionError:
        print(prefix + "└── [Немає доступу]")
        return
    except OSError as error:
        print(prefix + f"└── [Помилка: {error}]")
        return
    for index, item in enumerate(items):
        is_last = index == len(items) - 1
        connector = "└── " if is_last else "├── "
        if item.is_dir():
            print(prefix + connector + Fore.BLUE + item.name + Style.RESET_ALL)
            new_prefix = prefix + ("    " if is_last else "│   ")
            print_directory_tree(item, new_prefix)
def main():
    if len(sys.argv) != 2:
        print("Будь ласка, вкажіть шлях до директорії.")
        sys.exit(1)

    directory_path = Path(sys.argv[1])

    if not directory_path.exists():
        print(f"Директорія '{directory_path}' не існує.")
        sys.exit(1)

    if not directory_path.is_dir():
        print(f"'{directory_path}' не є директорією.")
        sys.exit(1)

    print(Fore.GREEN + f"Дерево директорії: {directory_path}" + Style.RESET_ALL)
    print_directory_tree(directory_path)
if __name__ == "__main__":
    main()