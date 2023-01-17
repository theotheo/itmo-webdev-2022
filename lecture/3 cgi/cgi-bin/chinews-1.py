#! /usr/bin/env python3

import os


def get_index():
    html = """
    <h1>Chinews</h1>

    <ul>
        <li>
            <h3>
                <a href="/pages/1.html">
                    Чтобы противостоять США, Китай создаст список управления технической безопасностью, чтобы запретить
                    экспорт ключевых технологий.

                </a>
            </h3>
        </li>
        <li>
            <h3>
                <a href="/pages/2.html">
                    Лай Циндэ уже так много сделал, что больше не может сдаваться! Депутат Лай Лай: Правила игры невыгодны,
                    и он все равно будет баллотироваться на выборах до конца
                </a>
            </h3>
        </li>
        <li>
            <h3>
                <a href="/pages/3.html">
                    Почему японо-южнокорейские отношения внезапно ухудшились после того, как их исключили из торгового
                    белого списка и отменили регулярную деятельность по обмену?
                </a>
            </h3>
        </li>
    </ul>
    """
    print(html)

def get_page():
    path = os.environ['PATH_INFO']
    # берем последнюю часть от адреса /pages/1 
    # и превращаем в число, чтобы по номеру достать из списка нужный элемент 
    news_id = int(path.split('/')[-1])
    # if news_id == 1:
    #     print()
    print(news_id)


print("Content-type:text/html\r\n\r\n")
print('<meta content="text/html;charset=utf-8" http-equiv="Content-Type">')

path = os.environ['PATH_INFO']

if path == "/":
    get_index()
elif path.startswith("/pages"):
    get_page()
else:
    print("error")


