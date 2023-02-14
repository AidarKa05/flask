from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = "Ученик Яндекс.Лицея"
    return render_template('index.html', title='Домашняя страница',
                           username=user)


@app.route('/promotion')
def return_sample_page():
    return """Человечество вырастает из детства.</br>
                Человечеству мала одна планета.</br>
                Мы сделаем обитаемыми безжизненные пока планеты.</br>
                И начнем с Марса!</br>
                Присоединяйся!</br>"""


@app.route('/image_mars')
def image():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                      <img src="{url_for('static', filename='img/MARS.png')}" 
                      alt="здесь должна была быть картинка, но не нашлась">
                    <br>Вот она какая, красная планета</br>
                  </body>
                </html>'''


@app.route('/promotion_image')
def bootstrap():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Привет, Яндекс!</h1>
                    <div class="text-bs-dark-bg-subtle">
                    А мы тут компонентами Bootstrap балуемся</div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
