#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pandas as pd
from jinja2 import Template


df = pd.read_csv('chinews.csv')
df['number'] = df.reset_index().index
news_list = df.to_dict(orient='records')

def get_index():
    with open('5 js/templates/index.jinja2') as f:
        view = Template(f.read())
    html = view.render(news_list=news_list[:10])

    return html

def get_page():
    path = os.environ['PATH_INFO']
    # берем последнюю часть от адреса /pages/1 
    # и превращаем в число, чтобы по номеру достать из списка нужный элемент 
    news_id = int(path.split('/')[-1])
    news = news_list[news_id]

    with open('5 js/templates/page.jinja2') as f:
        view = Template(f.read())
    html = view.render(news=news)

    return html

def get_error():
    return "error" 

def get_more():
    query = os.environ['QUERY_STRING']
    offset = int(query.split('=')[1])

    sublist = news_list[offset:offset+10]
    with open('5 js/templates/list.jinja2') as f:
        view = Template(f.read())
    html = view.render(news_list=sublist)

    return html


def router(path):
    if path == "/":
        controller = get_index
    elif path.startswith("/pages"):
        controller = get_page
    elif path.startswith("/api/list"):
        controller = get_more
    else:
        controller = get_error

    return controller

path = os.environ['PATH_INFO']

controller = router(path)

content = controller()

print("Content-type: text/html\n")
print(content)



