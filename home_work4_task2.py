import timeit


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [el for el in arr if el < pivot]
    middle = [el for el in arr if el == pivot]
    right = [el for el in arr if el > pivot]
    return quicksort(left) + middle + quicksort(right)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Масив молаємо на дві рівні частини
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'ємо менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи,
            # додємо їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def merge_k_lists(listing):
    merge_all_lists = []
    for arr in listing:
        merge_all_lists.extend(arr)

    return merge_sort(merge_all_lists)


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)

# перевірка функції при умові,
# що в кожному масиві є від'емні елементи
lists = [[1, 0, 4, 5], [-2, 1, 3, 4], [2, 6, -1]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
