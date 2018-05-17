from matplotlib import pyplot as plt


def trim(xmin, xmax, columns):
	# Set up container
	trimmed = [[] for i in columns]

	# For each row
	for i, x in enumerate(columns[0]):
		if not xmin is None and x < xmin:
			pass
		elif not xmax is None and x > xmax:
			pass
		else:
			for j, element in enumerate(columns):
				trimmed[j].append(element[i])

	return trimmed



def plot(name, headings, columns, xmin, xmax):
	# Trim data based on xlimits
	columns = trim(xmin, xmax, columns)

	
	# Get a list of axes
	graph_count = len(headings) - 1
	for i in range(graph_count):


		# Set up axis
		fig, axis = plt.subplots(1, 1)
		axis.set_xlabel(headings[0])
		axis.set_ylabel(headings[i+1])

		# Set up figure layout
		plt.tight_layout()

		# Render data
		axis.plot(columns[0], columns[i+1], linestyle='-')



		# Save figure & clear virtual canvas
		plt.savefig(name + '-' + headings[0][:4] + '-' + headings[i+1][:4] + '.png')
		plt.clf()





