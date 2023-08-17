from modules import run_dig_mod
from colorama import init, Fore, Style
from datetime import datetime
from pprint import pprint

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
	print("\n----------------------------------------------------------------------------------------------------------------")

def main(db, target, target_type, filename):
	# creating collection for storing target info
	target_col = db['target_col']

	# run dig tool
	records_from_dig, ipv4_from_dig = run_dig_mod.main(target[0])

	# Get the current date and time
	current_datetime = datetime.now()
	time_date = current_datetime.strftime("%b-%d-%Y_%H:%M:%S")

	target_lvl_1 = []

	if target_type == 0:
		# Open the input file in read mode
		with open(filename, 'r') as file:
			# Read each line from the file and add it to the list
			for line in file:
				target_lvl_1.append(line.strip())  # Remove leading/trailing whitespace

		target_doc = {
			'target_lvl_0': target,
			'target_type':target_type,
			'created_on': time_date,
			'target_lvl_1': [{'target': item} for item in target_lvl_1]
		}

	elif target_type == 1:
		target_doc = {
			'target_lvl_0': target[0],
			'target_type':target_type,
			'created_on': time_date,
			'target_lvl_1': target[0]
		}

	elif target_type == 2:
		target_doc = {
			'target_lvl_0': target,
			'target_type':target_type,
			'created_on': time_date,
			'target_lvl_1': [{'target': item} for item in target]
		}

	# storing data in target_col
	target_col.insert_one(target_doc)

	projection = {'_id': 0, 'target': 1, 'target_ipv4_dig': 1, 'last_updated': 1}
	documents = target_col.find({})

	# Print the specified fields for each document
	for document in documents:
		pprint(document)
