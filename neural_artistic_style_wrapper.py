NEURAL_ARTISTIC_STYLE_DIR = '/home/daniel/app/neural_artistic_style'
import os
import subprocess
import shutil
import sys

def run():
	
	if os.path.isfile('.crunching.lck'):
		return False
	os.mknod('.crunching.lck')

	style = sys.argv[1]
	subject = sys.argv[2]
	
	if os.path.isdir(os.path.join('images', 'animation')):
		shutil.rmtree(os.path.join('images', 'animation'))
	args = ['python', '-u', os.path.join(NEURAL_ARTISTIC_STYLE_DIR, 'neural_artistic_style.py'), \
		'--style', style, \
		'--subject', subject, \
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
