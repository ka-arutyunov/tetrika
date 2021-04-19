"""Решение получилось ооооочень монструозным и запутанным, с созданием кучи
разных массивов. Однозначно это не оптимальная реализация, но скрип
отрабатывает, как надо :) Хотелось бы увидеть эталонный вариант решение
данной задачи.

Так же нашел один из вариантов решения в виде: "Отсортировать все концы
отрезков и идти слева на право, храня список отрезков у которых уже было
начало, но еще не было конца. Отрезки, которые в какой-то момент
одновременно были в списке, пересекаются. В двумерном случае это называется
"метод сканирующей прямой". Время работы - O(n log n) на сортировку и O(n)
на проход по концам.

Реализовать не успел, т.к. нашел такой вариант решения поздно, да и потратил
на свой вариант уйму времени :) """


def appearance(intervals):
    A = intervals["lesson"]
    B = intervals["pupil"]
    C = intervals["tutor"]
    res = [A, B, C]

    currents = []
    for interval in res:
        currents.append({"start": interval[0], "end": interval[1], "index": 1})
    intersect = []
    for tic in range(max([A[0], B[0], C[0]]), min([A[-1], B[-1], C[-1]])):
        while True:
            check = check_intervals(tic, res, currents)
            if check:
                continue
            elif check is not None:
                break
            else:
                intersect.append(tic)
                break

    return len(intersect)


def check_intervals(tic, intervals, currents):
    i = 0
    for interval in intervals:
        current_info = currents[i]
        if not (current_info["start"] <= tic < current_info["end"]):
            if len(interval) > current_info["index"] + 1 and tic >= \
                    current_info["end"]:
                current_info["start"] = interval[current_info["index"] + 1]
                current_info["end"] = interval[current_info["index"] + 2]
                current_info["index"] = current_info["index"] + 2
                return True
            return False

        i += 1


tests = [
    {'data': {'lesson': [1594663200, 1594666800],
              'pupil': [1594663340, 1594663389, 1594663390, 1594663395,
                        1594663396, 1594666472],
              'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'data': {'lesson': [1594702800, 1594706400],
              'pupil': [1594702789, 1594704500, 1594702807, 1594704542,
                        1594704512, 1594704513, 1594704564, 1594705150,
                        1594704581, 1594704582, 1594704734, 1594705009,
                        1594705095, 1594705096, 1594705106, 1594706480,
                        1594705158, 1594705773, 1594705849, 1594706480,
                        1594706500, 1594706875, 1594706502, 1594706503,
                        1594706524, 1594706524, 1594706579, 1594706641],
              'tutor': [1594700035, 1594700364, 1594702749, 1594705148,
                        1594705149, 1594706463]},
     'answer': 3577
     },
    {'data': {'lesson': [1594692000, 1594695600],
              'pupil': [1594692033, 1594696347],
              'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        print(test_answer)
        assert test_answer == test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
