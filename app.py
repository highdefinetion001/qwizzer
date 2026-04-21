from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# 🔥 QUESTIONS (10 TOTAL - CODING + DS + PYTHON)
questions = [
    # 🔹 CODING
    {"q": "Output of print(2**8)?", "options": ["256", "128", "64", "16"], "a": "256"},
    {"q": "Which language is used for web apps?", "options": ["Python", "JavaScript", "C++", "All"], "a": "All"},
    {"q": "Which keyword is used to define a function in Python?", "options": ["def", "fun", "function", "define"], "a": "def"},

    # 🔹 DATA STRUCTURES
    {"q": "Which data structure uses FIFO?", "options": ["Stack", "Queue", "Tree", "Graph"], "a": "Queue"},
    {"q": "Which data structure uses LIFO?", "options": ["Queue", "Stack", "Array", "Tree"], "a": "Stack"},
    {"q": "Which is a non-linear data structure?", "options": ["Array", "Linked List", "Tree", "Queue"], "a": "Tree"},

    # 🔹 PYTHON
    {"q": "What is the output of print(type([]))?", "options": ["list", "dict", "tuple", "set"], "a": "list"},
    {"q": "Which symbol is used for comments in Python?", "options": ["//", "#", "/* */", "--"], "a": "#"},
    {"q": "Which data type is immutable?", "options": ["List", "Dictionary", "Set", "Tuple"], "a": "Tuple"},
    {"q": "Which function is used to get input from user?", "options": ["get()", "input()", "scan()", "read()"], "a": "input()"}
]

# Shuffle questions
random.shuffle(questions)

# Global variables
score = 0
q_index = 0


# 🔹 HOME
@app.route("/")
def home():
    return render_template("index.html")


# 🔹 QUIZ
@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    global score, q_index

    if request.method == "POST":
        selected = request.form.get("answer")

        if selected == questions[q_index]["a"]:
            score += 1

        q_index += 1

    # End quiz
    if q_index >= len(questions):
        final_score = score

        # reset
        score = 0
        q_index = 0
        random.shuffle(questions)

        return redirect(url_for("result", score=final_score))

    return render_template(
        "quiz.html",
        q=questions[q_index],
        current=q_index + 1,
        total=len(questions)
    )


# 🔹 RESULT
@app.route("/result")
def result():
    final_score = request.args.get("score")
    return render_template("result.html", score=final_score)


# 🔹 RUN
if __name__ == "__main__":
    app.run(debug=True)