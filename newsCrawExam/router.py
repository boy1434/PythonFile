from flask import Flask
from flask.templating import render_template
import newsExam_api as nea

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", newsExamList=nea.getNewsExamApi())

if __name__ == "__main__":
    app.run(debug=True, port=1004)