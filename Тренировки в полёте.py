from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index/<title>')
def index(title):
    user = "Ученик Яндекс.Лицея"
    return render_template('base.html', title=title,
                           username=user)


@app.route('/training/<prof>')
def training(prof):
    if 'инженер' in prof or 'строитель' in prof:
        return render_template('training.html', title='Инженерные тренажеры',
                               prof_sim='Инженерные тренажеры',
                               img=url_for('static', filename='img/simulator.png'))
    else:
        return render_template('training.html', title='Научные симуляторы',
                               prof_sim='Научные симуляторы',
                               img=url_for('static', filename='img/simulator.png'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
