import matplotlib.pyplot as plt
import random

# Создание простого графика
fig, ax = plt.subplots()
ax.plot([1,2,3,4,5],[1,5,2,4,3])
plt.savefig('test.png')


# Создание столбчатой диаграммы
x = []
y = []
for _ in range(10):
    num = random.randint(1, 50)
    x.append(num)

for _ in range(10):
    num = random.randint(10, 30)
    y.append(num)

plt.bar(x, y)
plt.xlabel('x label')
plt.ylabel('y label')
plt.savefig('test_1.png')


# Создание круговой диаграммы
x = []
labels = ['Chel', 'Msk', 'Spb', 'Kazn', 'Klng']

for _ in range(5):
    num = random.randint(10, 30)
    x.append(num)

plt.pie(x, labels=labels)
plt.title('label')
plt.savefig('test_2.png')

