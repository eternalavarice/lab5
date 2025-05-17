#5 задача

fig, axs = plt.subplots(1, 3, figsize=(15, 4))

# 1. Линейный график
x = np.linspace(0, 10, 100)
axs[0].plot(x, x**2, color='green')
axs[0].set_title('y = x^2')
axs[0].grid(True)

# 2. Точечный график
x_rand = np.random.rand(100)
y_rand = np.random.rand(100)
axs[1].scatter(x_rand, y_rand, color='purple')
axs[1].set_title('Случайные точки')

# 3. Столбчатая диаграмма
categories = ['A', 'B', 'C']
values = [3, 7, 2]
axs[2].bar(categories, values, color='orange')
axs[2].set_title('Категориальные данные')

plt.tight_layout()
plt.show()
