document = {
    'ipv4': 'test',
    'domain': 'test',
    'creation_time': 'test',
}

with open("target_info.txt", 'r') as file:
    lines = file.readlines()

# Process each line in the text file
for line in lines:
    # Remove leading/trailing spaces and newline characters
    line = line.strip()

    # Split the line into field name and value
    field, value = line.split('=')
    field = field.strip()
    value = value.strip()  # Remove surrounding single quotes if present

    # Update the corresponding field in the document
    if field in document:
        document[field] = value
        print(field)
        print(value)

print(document)