import matplotlib.pyplot as plt
import numpy as np
from glob import glob
import re, os

# 1. Set Arial as the global font family
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Liberation Sans']

def plot(search_string, filename):
	time = {}
	Mol = [ re.sub('A100/','',re.sub('-single-GPU.out','',i)) for i in glob('A100/*.out') ]
	for Dir in glob('*'):
		if os.path.isdir(Dir):
			time[Dir] = [ float(re.search(search_string+r'\s*=\s*([^\s(]+)',open(Dir+'/'+mol+'-single-GPU.out').read()).group(1)) for mol in Mol ]

	x = np.arange(len(Mol))
	width = 0.25  # Width of each bar

	fig, ax = plt.subplots(figsize=(8, 5))

	ax.bar(x - width, time['A100'], width, label='A100', color='royalblue')
	ax.bar(x, time['MI300A'], width, label='MI300A', color='seagreen')
	ax.bar(x + width, time['H200'], width, label='H200', color='crimson')

	ax.set_ylabel(search_string+' (sec)')
	ax.set_xticks(x)
	ax.set_xticklabels(Mol)
	labels = ax.get_xticklabels()
	for i, label in enumerate(labels):
		if i % 2 != 0:
			# Move alternating labels down (default y position is 0.0)
			label.set_y(-0.04)
	ax.tick_params(axis='x', labelsize=6)
	ax.legend()

	plt.savefig(filename, dpi=300, bbox_inches='tight')

if __name__=='__main__':
	plot('TOTAL TIME', 'total_time.png')
	plot('INITIAL GUESS TIME', 'guess_time.png')
	plot('TOTAL SCF TIME', 'scf_time.png')
	plot('TOTAL 2e TIME', '2e_time.png')
	plot('TOTAL EXC TIME', 'exc_time.png')
	plot('TOTAL DII TIME', 'diis_time.png')
	plot('TOTAL DIAG TIME', 'diagonalization_time.png')
	plot('TOTAL GRADIENT TIME', 'gradient_time.png')
	plot('TOTAL 2e GRADIENT TIME', '2e_gradient_time.png')
	plot('TOTAL EXC GRADIENT TIME', 'exc_gradient_time.png')
