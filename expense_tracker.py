import json


def save_expenses(expenses, filename):
    with open(filename, "w") as file:
        json.dump(expenses, file, ensure_ascii=False, indent=4)
    print(f"Расходы сохранены в {filename}")


def load_expenses(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Файл не найден, начинаем с нуля")
        return {}


def add_expense(expenses, category, amount):
    expenses[category] = amount
    print(f"Добавлено: {category} — {amount} руб.")


def add_expense_safe(expenses):
    category = input("Введи категорию расхода: ")
    while True:
        text = input("Введи сумму: ")
        try:
            amount = int(text)
            add_expense(expenses, category, amount)
            return amount
        except ValueError:
            print("Ошибка: введи только цифры!")


def total_expenses(expenses):
    total = 0
    for category, amount in expenses.items():
        total = total + amount
    return total


def max_expense(expenses):
    max_amount = 0
    max_category = ""
    for category, amount in expenses.items():
        if amount > max_amount:
            max_amount = amount
            max_category = category
    return max_category, max_amount


def remove_expense(expenses, category):
    if category in expenses:
        del expenses[category]
        print(f"Удалено: {category}")
    else:
        print(f"Категория {category} не найдена")


# --- основная программа ---
expenses = load_expenses("expenses.json")

add_expense_safe(expenses)

print(f"Общая сумма расходов: {total_expenses(expenses)} руб.")

if expenses:
    category, amount = max_expense(expenses)
    print(f"Самая большая трата: {category} — {amount} руб.")

save_expenses(expenses, "expenses.json")