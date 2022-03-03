from flask import Flask, render_template, url_for, flash, redirect, request
from model.model_toxicity import detoxify
app = Flask(__name__)


@app.route("/")

@app.route("/home")
def home_page():
    return render_template('home.html')


@app.route("/sentence", methods=['POST', 'GET'])
def sentence():

    if request.method == "POST":
        answer = request.form.get('Sentence')
        result_model = detoxify(answer)
        return render_template('sentence.html', asw=result_model)
    else:
        answer = ""
        return render_template('sentence.html', asw=answer)



if __name__ == '__main__':
    app.run(debug=True)