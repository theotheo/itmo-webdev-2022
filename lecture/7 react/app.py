from flask import render_template, Flask, request
import pandas as pd
import json

df = pd.read_csv('../chinews.csv')
df['number'] = df.reset_index().index + 1
news_list = df.to_dict(orient='records')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('app.jinja2', news_list=news_list[:10])

@app.route('/pages/<int:id>')
def page(id):
    news = news_list[id]
    
    return render_template('page.jinja2', news=news)

@app.route('/api/list')
def list():
    offset = int(request.args.get('offset'))
    sublist = news_list[offset:offset+10]
    text = json.dumps(sublist)

    return text

@app.route('/api/page/<int:id>')
def more(id):
    sublist = news_list[id]
    text = json.dumps(sublist)

    return text