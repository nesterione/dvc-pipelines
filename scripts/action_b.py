import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input')
parser.add_argument('--output')
args = parser.parse_args()

with open(args.input, 'r') as f_in:
	with open(args.output, 'w') as f_out:
		s = f_in.read() + ' --> Action B'
		f_out.write(s)