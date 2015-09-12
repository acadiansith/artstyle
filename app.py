from flask import Flask, render_template, request, send_from_directory
import os
import base64
import json

NEURAL_ARTISTIC_STYLE_DIR = '/home/daniel/app/neural_artistic_style'
UPLOAD_FOLDER = '/home/daniel/app/artstyle/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'bmp'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello():
	return render_template('index.html')

@app.route('/css/<path:path>')
def send_css(path):
	return send_from_directory('css', path)

@app.route('/js/<path:path>')
def send_js(path):
	return send_from_directory('js', path)

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

if __name__ == '__main__':
	app.run(
		port=int(8000),
		debug=True
	)
