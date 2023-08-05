from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# status indicators
blueinfo = f"{Fore.BLUE}[i]{Style.RESET_ALL}"
greenplus = f"{Fore.GREEN}[+]{Style.RESET_ALL}"
blueplus = f"{Fore.BLUE}[+]{Style.RESET_ALL}"
yellowinfo = f"{Fore.YELLOW}[i]{Style.RESET_ALL}"
yellowplus = f"{Fore.YELLOW}[+]{Style.RESET_ALL}"
yellowminus = f"{Fore.YELLOW}[-]{Style.RESET_ALL}"
redminus = f"{Fore.RED}[-]{Style.RESET_ALL}"
redexclaim = f"{Fore.RED}[!]{Style.RESET_ALL}"
redstar = f"{Fore.RED}[*]{Style.RESET_ALL}"

def line():
    print("\n---------------------------------------------------------------------------------------------")

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
