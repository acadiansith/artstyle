from flask import Flask, render_template, request, send_from_directory, redirect, \
	url_for
from werkzeug import secure_filename
import os
import base64
import json

NEURAL_ARTISTIC_STYLE_DIR = '/home/daniel/app/neural_artistic_style'
UPLOAD_FOLDER = '/home/daniel/app/artstyle/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'bmp'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
	return '.' in filename and \
		filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def hello():
	return render_template('index.html')

@app.route('/2')
def hello2():
	return render_template('index2.html')

@app.route('/css/<path:path>')
def send_css(path):
	return send_from_directory('css', path)

@app.route('/js/<path:path>')
def send_js(path):
	return send_from_directory('js', path)

@app.route('/semantic/<path:path>')
def send_semantic(path):
	return send_from_directory('semantic', path)

@app.route('/testget', methods=['GET'])
def testget():
	val = request.args.get('test', '')
	return val

@app.route('/getimage',methods=['GET'])
def getimage():
	with open(os.path.join(NEURAL_ARTISTIC_STYLE_DIR, 'images', 'donelli.jpg'), 'rb') as image_file:
		image64 = base64.b64encode(image_file.read())
	n = 256
	data = {'base64': image64.decode('utf-8')}
	return json.dumps(data) #'{"base64": "%s"}' % image64

@app.route('/putimage', methods=['POST'])
def putimage():
	file = request.files['file']
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		return redirect(url_for('uploaded_file', filename=filename))

@app.route('/uploaded', methods=['GET'])
def uploaded_file():
	val = request.args.get('filename')
	return val
	

if __name__ == '__main__':
	app.run(
		port=int(8000),
		debug=True
	)
