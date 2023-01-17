#! /usr/bin/env python

import os
import pandas as pd
from jinja2 import Template


df = pd.read_csv('chinews.csv')
df['number'] = df.reset_index().index
news_list = df.to_dict(orient='records')

def get_index():
    with open('index.jinja2') as f:
        view = Template(f.read())
    html = view.render(news_list=news_list)

    return html

def get_page():
    path = os.environ['PATH_INFO']
    # берем последнюю часть от адреса /pages/1 
    # и превращаем в число, чтобы по номеру достать из списка нужный элемент 
    news_id = int(path.split('/')[-1])
    news = news_list[news_id]

    with open('page.jinja2') as f:
        view = Template(f.read())
    html = view.render(news=news)

    return html

def get_error():
    return "error" 


def router(path):
    if path == "/":
        controller = get_index
    elif path.startswith("/pages"):
        controller = get_page
    else:
        controller = get_error

    return controller

print("Content-type:text/html\r\n\r\n")
print('<meta content="text/html;charset=utf-8" http-equiv="Content-Type">')
print("""
<div class="header"><div class="header-title">Сhinews</div></div>
""")

path = os.environ['PATH_INFO']

controller = router(path)

content = controller()

print(content)



print("""
<style>
body {
  padding: 0;
  margin: 8px;
  font-family: Verdana, Geneva, sans-serif;
}

a:link {
  color: #000000;
  text-decoration: none;
}

a:visited {
  color: #828282;
  text-decoration: none;
}


.header {
  background-color: #ff1100;
  white-space: nowrap;
  padding: 1.5rem;
  color: black;
  justify-content: space-between;
  align-items: center;
  display: flex;
}

.header-title {
  font-weight: 700;
  margin-left: 0.25rem;
  margin-right: 5px;
  color: black;
  text-decoration: none;
  font-size: 3.0rem;
}

ul {
    margin: 20px;
}

li {
    list-style-type: trad-chinese-informal;
}

</style>
""")