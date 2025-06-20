from flask import Flask, render_template, request
from gec import correct_text

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('home.html')
    elif request.method == 'POST':
        corrected = correct_text(request.form.get('input_text'))
        return render_template('home.html',
                               input=request.form.get('input_text'),
                               corrected=corrected)

if __name__ == '__main__':
    app.run()