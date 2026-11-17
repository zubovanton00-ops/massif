import time
import matplotlib.pyplot as plt

def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

sizes = [10, 100, 1000, 5000, 20000]
reps = 3000
results = {}

for name, fn in [("Линейный", linear_search), ("Бинарный", binary_search)]:
    times = []
    for n in sizes:
        data = list(range(n))
        start = time.perf_counter()
        for _ in range(reps):
            fn(data, -1)
        times.append((time.perf_counter() - start) / reps * 1e6)
    results[name] = times
    for n, t in zip(sizes, times):
        print(f"{name}, размер {n}: {t:.2f} мкс")

plt.plot(sizes, results["Линейный"], 'o-', label='Линейный поиск')
plt.plot(sizes, results["Бинарный"], 's-', label='Бинарный поиск')
plt.xlabel('Размер списка, элементов')
plt.ylabel('Время поиска, мкс')
plt.title('Линейный vs бинарный поиск: время от размера списка')
plt.legend()
plt.grid(True, alpha=0.4)
plt.savefig('binary_vs_linear.png', dpi=150)
plt.show()