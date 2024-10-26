import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def f(x):
    return x**2

def monte_carlo_integrate(f, a, b, n_points=100000):
    # Генеруємо випадкові точки
    x = np.random.uniform(a, b, n_points)
    y = np.random.uniform(0, f(b), n_points)
    
    # Знаходимо точки під кривою
    points_under_curve = y <= f(x)
    
    # Обчислюємо площу
    area_box = (b-a) * f(b)
    points_ratio = np.sum(points_under_curve) / n_points
    integral = area_box * points_ratio
    
    return integral, points_under_curve, x, y

# Параметри інтегрування
a, b = 0, 2
n_points = 100000

# Метод Монте-Карло
mc_result, points_under, x_points, y_points = monte_carlo_integrate(f, a, b, n_points)

# Точне значення через quad
exact_result, _ = integrate.quad(f, a, b)

# Візуалізація результатів
plt.figure(figsize=(12, 6))

# Графік 1: Метод Монте-Карло
plt.subplot(1, 2, 1)
plt.scatter(x_points[points_under], y_points[points_under], 
            c='blue', alpha=0.1, s=1, label='Точки під кривою')
plt.scatter(x_points[~points_under], y_points[~points_under], 
            c='red', alpha=0.1, s=1, label='Точки над кривою')

x = np.linspace(a, b, 1000)
plt.plot(x, f(x), 'k-', label='f(x) = x²')
plt.grid(True)
plt.legend()
plt.title(f'Метод Монте-Карло\n({n_points:,} точок)')
plt.xlabel('x')
plt.ylabel('y')

# Графік 2: Порівняння результатів
plt.subplot(1, 2, 2)
methods = ['Монте-Карло', 'Точне значення']
values = [mc_result, exact_result]
plt.bar(methods, values)
plt.title('Порівняння результатів')
plt.ylabel('Значення інтеграла')
for i, v in enumerate(values):
    plt.text(i, v, f'{v:.6f}', ha='center', va='bottom')
plt.grid(True)

plt.tight_layout()
plt.show()

# Виведення результатів
print(f"Результат методу Монте-Карло: {mc_result:.6f}")
print(f"Точне значення (quad): {exact_result:.6f}")
print(f"Абсолютна похибка: {abs(mc_result - exact_result):.6f}")
print(f"Відносна похибка: {abs(mc_result - exact_result)/exact_result*100:.4f}%")