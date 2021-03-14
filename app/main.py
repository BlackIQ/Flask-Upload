import os

from flask import Flask, redirect, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['SECRET_KEY'] = '12345678'
app.config['UPLOAD_FOLDER'] = './upload'

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        try:
            f = request.files['file']
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        except Exception as e:
            return 'Error in uploading file <br> {}'.format(str(e))
        return redirect('/upload')
    return render_template('upload.html')


if __name__ == '__main__':
    app.run('192.168.1.5', 5000, debug=True)
