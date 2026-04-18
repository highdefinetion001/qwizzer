from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

questions = [
    {"q": "What is output of print(2**3)?", "options": ["6", "8", "9", "5"], "a": "8"},
    {"q": "Which language is used for web apps?", "options": ["Python", "JavaScript", "C++", "All"], "a": "All"},
    {"q": "What is HTML?", "options": ["Programming", "Markup", "Database", "OS"], "a": "Markup"},
    {"q": "Which is loop?", "options": ["if", "for", "def", "class"], "a": "for"},
    {"q": "What is Python?", "options": ["Snake", "Language", "Game", "OS"], "a": "Language"},
    {"q": "Output of 10//3?", "options": ["3", "3.3", "4", "2"], "a": "3"},
    {"q": "Which is not datatype?", "options": ["int", "float", "char", "loop"], "a": "loop"},
    {"q": "Which is frontend?", "options": ["HTML", "Python", "C", "Java"], "a": "HTML"},
    {"q": "Which is backend?", "options": ["Flask", "CSS", "HTML", "JS"], "a": "Flask"},
    {"q": "What is variable?", "options": ["Storage", "Loop", "Function", "Class"], "a": "Storage"}
]

random.shuffle(questions)

score = 0
q_index = 0

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/quiz", methods=["GET", "POST"])
def quiz_page():
    global score, q_index

    if request.method == "POST":
        selected = request.form.get("answer")

        if selected == questions[q_index]["a"]:
            score += 1

        q_index += 1

    if q_index == len(questions):
        final_score = score
        score = 0
        q_index = 0
        return redirect(url_for("result", score=final_score))

    return render_template(
        "quiz.html",
        q=questions[q_index],
        current=q_index + 1,
        total=len(questions)
    )

@app.route("/result")
def result():
    score = request.args.get("score")
    return render_template("result.html", score=score)

if __name__ == "__main__":
    app.run(debug=True)