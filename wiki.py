#!/usr/local/bin/python
# -*- coding: utf-8
import wikipediaapi
import re

'''
Быстрое и оптимальное решение, однако вылезают "артефакты" из других категорий
Как от них избавиться - не разобрался :)
Предполагаю, что надо было бы залезть в category.categorymembers (т.к. это пользовательский 
объект похожий на словарь), но мои попытки успехом не увенчались

В функции words_count2 почему-то оч плохо сортируются данным (даже при условии сортировок).
Если есть комментарии на этот счёт - буду рад выслушать, хотелось бы понять, почему так происходит
'''

wiki = wikipediaapi.Wikipedia('ru')


def words_count(words):
    animal_counts = {}
    for word in words:
        animal = re.search(r'^[А-Я]\w.*', word.title)
        if animal:
            animal = animal.group()
            count = animal_counts.get(animal[0], 0)
            animal_counts[animal[0]] = count + 1

    for k in sorted(animal_counts.keys()):
        print("{}: {}".format(k, animal_counts[k]))


# def words_count2(words):
#     filtered_words = []
#     for word in words:
#         animal = re.search(r'^[А-Я]\w.*', word.title)
#         if animal:
#             filtered_words.append(animal.group())
#
#     filtered_words[:-4].sort()
#     cur_count = 0
#     cur_letter = filtered_words[0][0]
#     for i in filtered_words:
#         if cur_letter == i[0]:
#             cur_count += 1
#         else:
#             print("{}: {}".format(cur_letter, cur_count))
#             cur_count = 0
#             cur_letter = i[0][0]


category = wiki.page("Категория:Животные_по_алфавиту")
values = category.categorymembers.values()
words_count(values)
# words_count2(values)


