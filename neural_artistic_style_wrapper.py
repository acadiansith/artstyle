NEURAL_ARTISTIC_STYLE_DIR = '/home/daniel/app/neural_artistic_style'
import os
import subprocess
import shutil

def run():
	
	if os.path.isfile('.crunching.lck'):
		return False
	os.mknod('.crunching.lck')

	shutil.rmtree(os.path.join('images', 'animation'))
	args = ['python', '-u', os.path.join(NEURAL_ARTISTIC_STYLE_DIR, 'neural_artistic_style.py'), \
		'--style', os.path.join(NEURAL_ARTISTIC_STYLE_DIR, 'images', 'donelli.jpg'), \
		'--subject', os.path.join(NEURAL_ARTISTIC_STYLE_DIR, 'images', 'weird_al.jpg'), \
		'--iterations', '200', \
		'--vgg19', os.path.join(NEURAL_ARTISTIC_STYLE_DIR, 'imagenet-vgg-verydeep-19.mat'), \
		'--output', os.path.join('images', 'out.png'), \
		'--animation', os.path.join('images', 'animation')]
	
	with open('log.log', 'w') as log_file:
		p = subprocess.Popen(args, stdout=log_file)
		p.wait()

	os.remove('.crunching.lck')
	return True

if __name__ == '__main__':
	run()
