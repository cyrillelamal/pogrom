# Создание программы по заполнению массивов случайными значениями.
# Сортировка значений в списке методом вставки, плавной сортировки, с
# помощью встроенных функций языка.
import random


def fill(nb: int) -> list:
    return [random.randint(0, 9) for _ in range(nb)]


def insertion_sort(array):
    for i in range(1, len(array)):
        current_value = array[i]
        current_position = i
        while current_position > 0 and array[current_position - 1] > current_value:
            array[current_position] = array[current_position - 1]
            current_position = current_position - 1
        array[current_position] = current_value


def smooth_sort(lst):
    leo_nums = leonardo_numbers(len(lst))
    heap = []
    for i in range(len(lst)):
        if len(heap) >= 2 and heap[-2] == heap[-1] + 1:
            heap.pop()
            heap[-1] += 1
        else:
            if len(heap) >= 1 and heap[-1] == 1:
                heap.append(0)
            else:
                heap.append(1)
        restore_heap(lst, i, heap, leo_nums)
    for i in reversed(range(len(lst))):
        if heap[-1] < 2:
            heap.pop()
        else:
            k = heap.pop()
            t_r, k_r, t_l, k_l = get_child_trees(i, k, leo_nums)
            heap.append(k_l)
            restore_heap(lst, t_l, heap, leo_nums)
            heap.append(k_r)
            restore_heap(lst, t_r, heap, leo_nums)


def leonardo_numbers(hi):
    a, b = 1, 1
    numbers = []
    while a <= hi:
        numbers.append(a)
        a, b = b, a + b + 1
    return numbers


def restore_heap(lst, i, heap, leo_nums):
    current = len(heap) - 1
    k = heap[current]
    while current > 0:
        j = i - leo_nums[k]
        if (lst[j] > lst[i] and
                (k < 2 or lst[j] > lst[i - 1] and lst[j] > lst[i - 2])):
            lst[i], lst[j] = lst[j], lst[i]
            i = j
            current -= 1
            k = heap[current]
        else:
            break
    while k >= 2:
        t_r, k_r, t_l, k_l = get_child_trees(i, k, leo_nums)
        if lst[i] < lst[t_r] or lst[i] < lst[t_l]:
            if lst[t_r] > lst[t_l]:
                lst[i], lst[t_r] = lst[t_r], lst[i]
                i, k = t_r, k_r
            else:
                lst[i], lst[t_l] = lst[t_l], lst[i]
                i, k = t_l, k_l
        else:
            break


def get_child_trees(i, k, leo_nums):
    t_r, k_r = i - 1, k - 2
    t_l, k_l = t_r - leo_nums[k_r], k - 1
    return t_r, k_r, t_l, k_l


if __name__ == "__main__":
    arr = fill(1000)
    sorted(arr)

    arr = fill(1000)
    insertion_sort(arr)

    arr = fill(1000)
    smooth_sort(arr)
