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


@app.route('/promotion_image')
def promotion_image():
    topics = [
        'Человечество вырастает из детства.',
        'Человечеству мала одна планета.',
        'Мы сделаем обитаемыми безжизненные пока планеты.',
        'И начнем с Марса!',
        'Присоединяйся!'
    ]
    url_pic = url_for('static', filename='img/mars.jpeg')
    url_style = url_for('static', filename='css/style.css')
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                         rel="stylesheet"
                          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                           crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_style}" />
                        <title>Колонизация</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_pic}" alt="здесь должна была быть картинка, но не нашлась">
                        <div class="alert-dark" role="alert">
                          <br><h3>{topics[0]}</h3>
                        </div>
                        <div class="alert-success" role="alert">
                          <br><h3>{topics[1]}</h3>
                        </div>
                        <div class="alert-secondary" role="alert">
                          <br><h3>{topics[2]}</h3>
                        </div>
                        <div class="alert-warning" role="alert">
                          <br><h3>{topics[3]}</h3>
                        </div>
                        <div class="alert-danger" role="alert">
                          <br><h3>{topics[4]}</h3>
                        </div>
                      </body>
                    </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
