from flask import Flask
from flask import render_template
# Объект класса Flask создается
app = Flask(__name__)
# Во  строке app= создается объект Flask.
# Для этого конструктору Flask назначается аргумент __name__.
# Конструктор Flask должен иметь один обязательный аргумент.
# Им служит название пакета. В большинстве случаев значение __name__ подходит.
# Название пакета приложения используется фреймворком Flask, чтобы находить статические файлы, шаблоны.

# Создание route (путей)
@app.route('/')
@app.route('/main/')
# Маршрут (или путь) используется во фреймворке Flask для привязки URL к функции представления.
# Эта функция отвечает на запрос.
# Во Flask декоратор route используется, чтобы связать URL адрес с функций.
def main_page():
    context = {'title': 'Интернет-магазин: Главная'}
    return render_template('main.html', **context)

@app.route('/clothes/')
def clothes_page():
    context = {'title': 'Интернет-магазин: Одежда'}
    return render_template('clothes.html', **context)

@app.route('/footwear/')
def footwear_page():
    context = {'title': 'Интернет-магазин: Обувь'}
    return render_template('footwear.html', **context)

@app.route('/jacket/')
def jacket_page():
    context = {'title': 'Интернет-магазин: Куртка'}
    return render_template('jacket.html', **context)


if __name__=='__main__':
    app.run()
    # Условие __name__ == "__main__" гарантирует,
    # что метод run() будет вызван только в том случае,
    # если main.py будет запущен,
    # как основная программа.
    # Если попытаться использовать метод run() при импорте main.py в другой модуль Python,
    # он не вызовется.