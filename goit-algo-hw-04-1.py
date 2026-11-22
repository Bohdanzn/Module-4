from pathlib import Path

def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                name, salary = line.split(",")
                total += int(salary.strip())
                count += 1

        if count == 0:
            return 0, 0

        average = total / count

        return total, average

    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return 0, 0

    except (ValueError, OSError):
        print("Помилка: файл містить некоректні дані.")
        return 0, 0