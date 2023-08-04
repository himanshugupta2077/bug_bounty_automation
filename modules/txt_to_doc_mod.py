def txt_to_doc(source, destination):
	# this function will read data from txt file (formatted as per destination document) and return a document with data filled

	with open(source, 'r') as file:
		lines = file.readlines()

	# Process each line in the text file
	for line in lines:
		# Remove leading/trailing spaces and newline characters
		line = line.strip()
		# print(line)

		# Split the line into field name and value
		field, value = line.split('=')
		field = field.strip()
		value = value.strip()  # Remove surrounding single quotes if present

		# Update the corresponding field in the document
		if field in destination:
			destination[field] = value
			# print(field)
			# print(value)

	# print(destination)

	return destination
