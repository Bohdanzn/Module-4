from pathlib import Path

def get_cats_info(path):
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                cat_id, name, age = line.split(",")

                cat = {
                    "id": cat_id.strip(),
                    "name": name.strip(),
                    "age": age.strip()
                }

                cats.append(cat)

        return cats

    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return []

    except (ValueError, OSError):
        print("Помилка: файл містить некоректні дані.")
        return []
