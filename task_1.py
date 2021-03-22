import time


'''
Предполагаю, что в данном случае бинарный поиск будет оптимальным решением. Однако, реализация task_2
почему-то дает такую же скорость выполнения при разной длине массива.

task - бинарный поиск, имеет временную сложность O(logn)
task_2 - линейный поиск (?), имеет времменную сложность O(n)

Был бы рад комментариям по task_2 :)
'''


def task(array):
    target = '0'
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] > target:
            low = mid + 1
        elif array[mid] < target:
            high = mid - 1
        else:
            if mid - 1 < 0:
                return mid
            if array[mid - 1] != target:
                return mid
            high = mid - 1
    return None


def task_2(array):
    return array.count('1')


c = time.time()
print(task('111111111111111111111111100000000'))
b = time.time()
print(b - c)


# d = time.time()
# print(task_2('111111111111111111111111100000000'))
# e = time.time()
# print(e - d)