#! /usr/bin/env python

import os
import pandas as pd


df = pd.read_csv('chinews.csv')
df['number'] = df.reset_index().index
news_list = df.to_dict(orient='records')


def get_index():
    html_news_list = ""

    for news in news_list[:5]:
        html_news = f"""
            <li>
                <h3>
                    <a href="pages/{news['number']}">
                        {news['ru_title']}
                    </a>
                </h3>
            </li>
        """
        html_news_list += html_news


    html = f"""
    <ul>
        {html_news_list}
    </ul>
    """
    
    return html

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
        {news['title']}
        </h2>


        <p size="20">
        {news['content']}
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
print('<h1>Chinews</h1>')

path = os.environ['PATH_INFO']

if path == "/":
    content = get_index()
elif path.startswith("/pages"):
    content = get_page()
else:
    content = get_error()

print(content)




