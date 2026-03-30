import flask
import datetime
import os
import re
from random import choice


app = flask.Flask(__name__)

car = ["Chevrolet", "Renault", "Ford", "Lada"]
cat_breed = ["корниш-рекс", "русская голубая", "шотландская вислоухая", "мейн-кун", "манчкин"]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')

with open(BOOK_FILE, encoding='utf-8') as book:
    text = book.read()

def load_words():
    word = re.findall(r'\b\w+\b', text)
    return word

word_list = load_words()

@app.route('/hello_world')
def hello_world():
    return 'Hello World!'

@app.route('/cars')
def cars():
    return car

@app.route('/cats')
def cats():
    cat = choice(cat_breed)
    return cat

@app.route('/get_time/now')
def get_time():
    current_time = datetime.datetime.now()
    return f'Точное время: {current_time}'

@app.route('/get_time/future')
def get_time_future():
    current_time_after_hour = datetime.datetime.now() + datetime.timedelta(hours=1)
    return f'Точное время через час будет: {current_time_after_hour}'

@app.route('/get_random_word')
def get_random_word():
    words = choice(word_list)
    return words


@app.route('/counter')
def counter():
    counter.visits += 1
    return f'Страничку открыли: {counter.visits} раз'

counter.visits = 0

if __name__ == '__main__':
    app.run(debug=True)
    pass