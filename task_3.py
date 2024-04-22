def quicksort(arr):
    """Использование метода QuickSort"""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

"""Данная функция соответствует заданным критериям эффективности, так как она обеспечивает быструю сортировку
в среднем случае за счет использования алгоритма QuickSort. Кроме того, она проста в реализации и универсальна
для различных размеров и порядка чисел в массиве."""