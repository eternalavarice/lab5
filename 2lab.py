#2 задача

data = np.random.normal(loc=0, scale=1, size=1000)

plt.hist(data, bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.title('Гистограмма нормального распределения')
plt.grid(True)
plt.show()
