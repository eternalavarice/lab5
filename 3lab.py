#3 задача

matrix = np.random.randint(1, 11, size=(5, 5))

mean_val = np.mean(matrix)
max_val = np.max(matrix)
min_val = np.min(matrix)
sum_cols = np.sum(matrix, axis=0)

print("Матрица:\n", matrix)
print("Среднее значение:", mean_val)
print("Максимум:", max_val)
print("Минимум:", min_val)
print("Сумма по столбцам:", sum_cols)
