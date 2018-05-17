import codecs


def parse_file(filename):
	rows = []
	skip_flag = True
	with codecs.open(filename, "r", encoding='utf-8', errors='replace') as data_file:
		for line in data_file.readlines():
			# Strip the newline from each line
			line = line.strip('\n').strip('\r')
			# Split into an array of strings at each comma
			line = line.split(',')

			# Get headings
			if 'Comment' in line[0]:
				skip_flag = False
				headings = line
			# Skip header
			elif skip_flag:
				continue
			# Collect data
			else:
				for i, element in enumerate(line):
					try:
						if '.' in element:
							line[i] = float(element)
						elif element:
								line[i] = int(element)
						elif element == u'':
							line[i] = None
					except ValueError:
						pass
				rows.append(line)
		
	return headings, rows

def extract_columns(headings, data, *indices):
	'''
	Extracts selected columns from data
	'''
	new_headings = [headings[x] for x in indices]

	columns = [ [] for i in indices]
	for row in data:
		new_row = []
		for index, element in enumerate(indices):
			columns[index].append(row[element])
	return new_headings, columns

