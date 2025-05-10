from flask import Flask, jsonify, render_template
import random
#import requests  # Для запросов к внешнему API (если нужно)

app = Flask(__name__)

# Локальная база цитат (можно заменить на запрос к внешнему API)
quotes = [
    {"content": "Жизнь — это то, что происходит, пока ты строишь другие планы.", "author": "Джон Леннон"},
    {"content": "Единственный способ сделать великую работу — любить то, что ты делаешь.", "author": "Стив Джобс"},
    {"content": "Будь тем изменением, которое ты хочешь видеть в мире.", "author": "Махатма Ганди"},
    {"content": "Учитесь так, как будто вы будете жить вечно; живите так, как будто вы умрёте завтра.",
     "author": "Махатма Ганди"},
    {"content": "Успех — это способность идти от неудачи к неудаче, не теряя энтузиазма.", "author": "Уинстон Черчилль"}
]


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/random-quote')
def random_quote():
    # Можно выбрать случайную цитату из локальной базы
    quote = random.choice(quotes)

    # Или получить цитату из внешнего API (раскомментируйте, если нужно)
    # response = requests.get('https://api.quotable.io/random')
    # quote = response.json()

    return jsonify(quote)


if __name__ == '__main__':
    app.run(debug=True)
