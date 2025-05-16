from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

WORDS = {
    "Easy": [
        {"word": "dog", "hint": "A common domestic animal, man’s best friend."},
        {"word": "cat", "hint": "A small domesticated feline animal."},
        {"word": "apple", "hint": "A red or green fruit often associated with health."},
        {"word": "ball", "hint": "A round object used in games and sports."}
    ],
    "Medium": [
        {"word": "python", "hint": "A popular programming language or a large snake."},
        {"word": "laptop", "hint": "A portable computer."},
        {"word": "school", "hint": "A place where students learn."},
        {"word": "bottle", "hint": "Used to store liquids."}
    ],
    "Hard": [
        {"word": "hangman", "hint": "The name of this very game!"},
        {"word": "interface", "hint": "Connects two systems or devices."},
        {"word": "developer", "hint": "Someone who writes software."},
        {"word": "keyboard", "hint": "Used to type on a computer."}
    ]
}

import random

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_word')
def get_word():
    difficulty = request.args.get('difficulty', 'Medium')
    words_list = WORDS.get(difficulty, WORDS['Medium'])
    selected = random.choice(words_list)
    return jsonify(selected)

if __name__ == '__main__':
    app.run(debug=True)
