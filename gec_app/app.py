from flask import Flask, render_template, request, Response
from gec import correct_text

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def text_correction():
    if request.method == 'GET':
        return render_template('home.html')
    elif request.method == 'POST':
        corrected = correct_text(request.form.get('input_text'))
        return render_template('home.html',
                               input=request.form.get('input_text'),
                               corrected=corrected)
    
@app.route('/file_correction', methods=['GET', 'POST'])
def file_correction():
    if request.method == 'GET':
        return render_template('file_correction.html')
    elif request.method == 'POST':
        uploaded_file = request.files.get('file')
        
        if uploaded_file and uploaded_file.filename.endswith('.txt'):
            file_content = uploaded_file.read().decode('utf-8')  # Read as text
            corrected = correct_text(file_content)
            headers = {
            'Content-Disposition': f'attachment; filename={uploaded_file.filename.split('.')[0]}_corrected.txt'
                }
            return Response(corrected, mimetype='text/plain', headers=headers)
        else:
            error = "* Only .txt files are supported currently."
            return render_template('file_correction.html', error=error)

if __name__ == '__main__':
    app.run()