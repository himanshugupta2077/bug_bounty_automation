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

def main(db, target):
	# creating collection for storing target info
	target_info_collection = db['target_info']

	# run dig tool
	records_from_dig, ipv4_from_dig = run_dig_mod.main(target[0])

	# Get the current date and time
	current_datetime = datetime.now()

	# Format the date and time in the desired format
	time_date = current_datetime.strftime("%b-%d-%Y_%H:%M:%S")

	target_name_document = {
			'target':target
	}

	target_ipv4_document = {
			'target_ipv4_dig':ipv4_from_dig
	}

	last_updated_document = {
			'last_updated':time_date
	}

	# storing data in target_info_collection
	target_info_collection.insert_one(target_name_document)
	target_info_collection.insert_one(target_ipv4_document)
	target_info_collection.insert_one(last_updated_document)

	projection = {'_id': 0, 'target': 1, 'target_ipv4_dig': 1, 'last_updated': 1}
	documents = target_info_collection.find({}, projection)

	# Print the specified fields for each document
	for document in documents:
		pprint(document)
