#4 задача

plt.imshow(matrix, cmap='viridis')
plt.colorbar()
plt.title('Тепловая карта матрицы')

for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        plt.text(j, i, matrix[i, j], ha='center', va='center', color='white')

plt.show()
