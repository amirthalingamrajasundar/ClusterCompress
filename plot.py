import matplotlib.pyplot as plt

# Output:
# root@5587707a5868:/app# python main.py --image ./image/input_image.jpg --num_clusters 2
# MSE: 0.03206917602224996
# root@5587707a5868:/app# python main.py --image ./image/input_image.jpg --num_clusters 5
# MSE: 0.009577312447572142
# root@5587707a5868:/app# python main.py --image ./image/input_image.jpg --num_clusters 10
# MSE: 0.0048920057823762285
# root@5587707a5868:/app# python main.py --image ./image/input_image.jpg --num_clusters 20
# MSE: 0.0026909937308160045
# root@5587707a5868:/app# python main.py --image ./image/input_image.jpg --num_clusters 50
# MSE: 0.0012847510149189027

# List of (K, MSE) tuples
data = [
    (2, 0.03206917602224996),
    (5, 0.009577312447572142),
    (10, 0.0048920057823762285),
    (20, 0.0026909937308160045),
    (50, 0.0012847510149189027)
]

# Separate into two lists
k_values, mse_values = zip(*data)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(k_values, mse_values, marker='o', linestyle='-', color='g')
plt.title('MSE vs Number of Clusters (K)')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Mean Squared Error (MSE)')
plt.grid(True)
plt.tight_layout()

plt.savefig('plots/mse_vs_k.png')

plt.show()
