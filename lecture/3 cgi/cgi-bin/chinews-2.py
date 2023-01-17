#! /usr/bin/env python3

import os
import pandas as pd

df = pd.read_csv('chinews.csv')
df['number'] = df.reset_index().index
news_list = df.to_dict(orient='records')


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
    news = news_list[news_id]

    html = f"""
        <p>
            Дата: <i>{news['date']}</i>
        </p>
        <h2>
        {news['ru_title']}
        </h2>


        <p size="20">
        {news['ru_desc']}
        </p>

        <dl>
            <dt>источник</dt>
            <dd>
                <a href="{news['url']}">{news['source']}</a>
            </dd>
        </dl>
    """
    return html

def get_error():
    return "error" 

print("Content-type:text/html\r\n\r\n")
print('<meta content="text/html;charset=utf-8" http-equiv="Content-Type">')


path = os.environ['PATH_INFO']

if path == "/":
    content = get_index()
elif path.startswith("/pages"):
    content = get_page()
else:
    content = get_error()

print(content)

