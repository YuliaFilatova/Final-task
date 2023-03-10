# дана функция f(x) = sin(x)^2 - cos(x)^2
# Определить корни
# Найти интервалы, на которых функция возрастает
# Найти интервалы, на которых функция убывает
# Построить график
# Вычислить вершину
# Определить промежутки, на котором f > 0
# Определить промежутки, на котором f < 0

from sympy import solve, plot, diff, symbols, sin, cos

print ('Дана функция f(x) = sin(x)^2 - cos(x)^2')
x = symbols('x')
ans = diff(sin(x)**2 - cos(x)**2, x)
print(f'Корни уравнения: {solve (sin(x)**2 - cos(x)**2, x)}')
print(f'Промежутки, на которых f > 0: {solve (sin(x)**2 - cos(x)**2 > 0, x)}')
print(f'Промежутки, на которых f < 0: {solve (sin(x)**2 - cos(x)**2 < 0, x)}')
print(f'Вершина ф-ии: {solve (ans)}')
print(f'Промежутки, на которых ф-я возрастает: {solve (ans>0)}')
print(f'Промежутки, на которых ф-я убывает: {solve (ans<0)}')
print(plot(sin(x)**2 - cos(x)**2)) #график