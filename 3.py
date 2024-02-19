from flask import *

app = Flask(__name__)


@app.route('/')
def default():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    text = '''Человечество вырастает из детства.
    Человечеству мала одна планета.
    Мы сделаем обитаемыми безжизненные пока планеты.
    И начнем с Марса!
    Присоединяйся!'''
    return '</br>'.join(text.split('\n'))


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс</h1>
                    <img src="{url_for('static', filename='mars.jpeg')}"
                    alt="здесь должна была быть картинка, но не нашлась">
                    <h2>Вот она какая, красная планета</h2>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
