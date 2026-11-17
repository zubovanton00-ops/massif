import random

def binary_search(sorted_lst, target):
    left, right = 0, len(sorted_lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_lst[mid] == target:
            return mid
        elif sorted_lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

random.seed(42)
data = sorted(random.randint(1, 10000) for _ in range(100))


targets = [data[0], data[len(data) // 2], data[-1], 99999]
results = {t: binary_search(data, t) for t in targets}

print("Список (первые 10 элементов):", data[:10])
print("Результаты поиска:", results)