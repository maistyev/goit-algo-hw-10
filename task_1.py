from pulp import *

# Створюємо задачу максимізації
prob = LpProblem("Оптимізація_виробництва_напоїв", LpMaximize)

# Визначаємо змінні
lemonade = LpVariable("Лимонад", 0, None, LpInteger)  # кількість лимонаду
fruit_juice = LpVariable("Фруктовий_сік", 0, None, LpInteger)  # кількість фруктового соку

# Цільова функція (максимізація загальної кількості продуктів)
prob += lemonade + fruit_juice, "Загальна кількість напоїв"

# Обмеження
# Вода: 2 од. на лимонад + 1 од. на фруктовий сік <= 100
prob += 2 * lemonade + fruit_juice <= 100, "Обмеження_води"

# Цукор: 1 од. на лимонад <= 50
prob += lemonade <= 50, "Обмеження_цукру"

# Лимонний сік: 1 од. на лимонад <= 30
prob += lemonade <= 30, "Обмеження_лимонного_соку"

# Фруктове пюре: 2 од. на фруктовий сік <= 40
prob += 2 * fruit_juice <= 40, "Обмеження_фруктового_пюре"

# Розв'язуємо задачу
prob.solve()

# Виводимо результати
print("Статус:", LpStatus[prob.status])
print("\nОптимальний план виробництва:")
print(f"Лимонад: {round(value(lemonade))} одиниць")
print(f"Фруктовий сік: {round(value(fruit_juice))} одиниць")
print(f"\nЗагальна кількість вироблених напоїв: {round(value(lemonade) + value(fruit_juice))} одиниць")

# Виводимо використання ресурсів
print("\nВикористання ресурсів:")
print(f"Вода: {2*value(lemonade) + value(fruit_juice)}/100 одиниць")
print(f"Цукор: {value(lemonade)}/50 одиниць")
print(f"Лимонний сік: {value(lemonade)}/30 одиниць")
print(f"Фруктове пюре: {2*value(fruit_juice)}/40 одиниць")