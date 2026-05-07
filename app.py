from flask import Flask, render_template, request

app = Flask(__name__)

quizzes = {
    "python": [
        {"q": "What is Python?", "options": ["Language", "Snake", "Game", "Car"], "ans": "Language"},
        {"q": "Keyword for function?", "options": ["fun", "def", "function", "define"], "ans": "def"},
        {"q": "List is?", "options": ["Mutable", "Immutable", "None", "Error"], "ans": "Mutable"},
        {"q": "Tuple is?", "options": ["Mutable", "Immutable", "Both", "None"], "ans": "Immutable"},
        {"q": "Which loop?", "options": ["for", "loop", "iterate", "repeat"], "ans": "for"},
        {"q": "Python file extension?", "options": [".py", ".java", ".cpp", ".txt"], "ans": ".py"},
        {"q": "Input function?", "options": ["scan()", "input()", "get()", "read()"], "ans": "input()"},
        {"q": "Output function?", "options": ["print()", "echo()", "show()", "display()"], "ans": "print()"},
        {"q": "Boolean values?", "options": ["True/False", "Yes/No", "1/0", "None"], "ans": "True/False"},
        {"q": "Operator for power?", "options": ["^", "**", "*", "//"], "ans": "**"}
    ]
}

@app.route('/')
def index():
    return render_template('index.html', quizzes=quizzes)

@app.route('/quiz/<quiz_name>')
def quiz(quiz_name):
    return render_template('quiz.html', questions=quizzes[quiz_name], quiz_name=quiz_name)

@app.route('/submit/<quiz_name>', methods=['POST'])
def submit(quiz_name):
    questions = quizzes[quiz_name]
    score = 0

    for i, q in enumerate(questions):
        if request.form.get(f'q{i}') == q['ans']:
            score += 1

    return render_template('result.html', score=score, total=len(questions))

if __name__ == '__main__':
    app.run(debug=True)