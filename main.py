from flask import Flask, render_template

app = Flask(__name__)

SKILLS = [
  {
    "id" : "1.",
    "Skill" : "Python intermediate"
  },
  {
    "id" : "2.",
    "Skill" : "Web development beginner"
  },
  {
    "id" : "3.",
    "Skill" : "Chess"
  }
]

@app.route("/")
def hello():
  return render_template("home.html", skills = SKILLS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)