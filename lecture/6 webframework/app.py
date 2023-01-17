from flask import render_template, Flask, request
import pandas as pd

df = pd.read_csv('../chinews.csv')
df['number'] = df.reset_index().index + 1
news_list = df.to_dict(orient='records')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.jinja2', news_list=news_list[:10])

@app.route('/pages/<int:id>')
def page(id):
    news = news_list[id]
    
    return render_template('page.jinja2', news=news)

@app.route('/api/list')
def more():
    offset = int(request.args.get('offset'))
    sublist = news_list[offset:offset+10]
    return render_template('list.jinja2', news_list=sublist)
