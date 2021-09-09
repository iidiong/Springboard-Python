from stories import story
from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/')
def ask_questions():
    prompts = story.prompts
    print(prompts)
    return render_template("questions.html", prompts=prompts)

@app.route('/story')
def display_story():
    text = story.generate(request.args)
    return render_template("story.html", text=text)