import os
import argparse

from PPMSplot import plot
from PPMSplot.parser import parse_file, extract_columns


parser = argparse.ArgumentParser(description='Plot PPMS .dat files columnwise')

parser.add_argument('filepath', metavar='F', type=str, nargs='?',
                    help='filepath of PPMS .dat file')

parser.add_argument('--xmin', metavar='m', type=float, nargs='?', default=None,
                    help='Minimum X trim value')

parser.add_argument('--xmax', metavar='M', type=float, nargs='?', default=None,
                    help='Maximum X trim value')

parser.add_argument('columns', metavar='C', type=int, nargs='*', default=None,
                    help='Columns desired for plotting')


def main():
	args = parser.parse_args()
	
	try:
		assert args.filepath
		assert args.columns
		assert isinstance(args.columns, list)
		assert len(args.columns) > 1
	except:
		print('Invalid syntax')
		parser.print_help()
		quit()

	name = os.path.splitext(args.filepath)[0]

	headings, rows = parse_file(args.filepath)
	headings, columns = extract_columns(headings, rows, *args.columns)
	plot(name, headings, columns, xmin=args.xmin, xmax=args.xmax)

if __name__ == "__main__":
	main()
