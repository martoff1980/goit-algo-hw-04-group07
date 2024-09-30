import random
import timeit
import matplotlib.pyplot as plt

# Сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Timsort через вбудовану функцію sorted
def timsort(arr):
    return sorted(arr)

# Функція для тестування часу виконання
def test_sorting_algorithm(sort_function, data):
    start_time = timeit.default_timer()
    sort_function(data)
    return timeit.default_timer() - start_time


if __name__ == "__main__":
    # Генерація тестових даних
    sizes = [100, 1000, 5000, 10000]

    for size in sizes:
        data = [random.randint(0, 10000) for _ in range(size)]

        # Копіювання даних для кожного алгоритму
        data_for_merge = data.copy()
        data_for_insertion = data.copy()

        # Тестування
        merge_time = test_sorting_algorithm(merge_sort, data_for_merge)
        insertion_time = test_sorting_algorithm(
            insertion_sort, data_for_insertion)
        timsort_time = test_sorting_algorithm(timsort, data)

        print(f"Розмір: {size}")
        print(f"Час сортування злиттям: {merge_time:.5f} секунд")
        print(f"Час сортування вставками: {insertion_time:.5f} секунд")
        print(f"Час Timsort: {timsort_time:.5f} секунд")
        print()
