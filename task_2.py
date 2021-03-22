#!/usr/local/bin/python
# -*- coding: utf-8
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests

'''
Второй вариант (ну или первый :)) реализации парсинга википедии.
Здесь нет лишних артефактов, т.к. парсинг проходил гораздо "чище" и целенаправленнее.
Можно было избежать написания функции рекурсии, однако в рамках обучения я решил вникнуть в вопрос
и поэтому удалять не стал.

Функция get_all_letter_count аналогична функции words_count в скрипте wiki.py.
Сортировка через список (закомментирована) опять была с различными ошибками. Предполагаю, что в списках животных
есть имена не совпадающие букве (список на букву В, а там закралось имя на букву Д).
Если есть комментарии на этот счёт - буду рад выслушать, хотелось бы понять, почему так происходит
'''

ua = UserAgent()
headers = {'User-Agent': ua.random}


def recursion(dirty_list):
    for item in dirty_list:
        if isinstance(item, list):
            yield from recursion(item)
        else:
            yield item


def get_all_letter_count(animals):
    animal_counts = {}
    for animal in animals:
        title = animal.task('a').text
        if title:
            count = animal_counts.get(title[0], 0)
            animal_counts[title[0]] = count + 1

    for k in sorted(animal_counts.keys()):
        print("{}: {}".format(k, animal_counts[k]))


def main():
    page = 'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0' \
           '%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82' \
           '%D1%83&from=%D0%90'
    all_animals = []
    for _ in range(92):
        req = requests.get(page, headers=headers).text
        soup = BeautifulSoup(req, 'lxml')
        category = soup.find('div', class_='mw-category').find('ul').find_all('li')
        page = 'https://ru.wikipedia.org' + soup.find('div', id='mw-pages').find_all('a')[1].get('href')
        all_animals.append(category)

    recursion_list = list(recursion(all_animals))
    return get_all_letter_count(recursion_list)

    # sort_list = sorted(pure_all_animals)
    # cur_count = 0
    # cur_letter = sort_list[0][0]
    # for i in sort_list:
    #     if cur_letter == i[0]:
    #         cur_count += 1
    #     else:
    #         print("{}: {}".format(cur_letter, cur_count))
    #         cur_count = 0
    #         cur_letter = i[0]


if __name__ == '__main__':
    main()
