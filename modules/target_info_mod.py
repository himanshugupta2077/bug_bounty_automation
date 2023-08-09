from modules import txt_to_doc_mod
from colorama import init, Fore, Style
from datetime import datetime

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

def get_target_info(db, current_directory,target):
	# creating collection for storing target info
	target_info_collection = db['target_info']

	target_name_document = {
            'target':target
	}

	# run dig tool
	ipv4_from_dig = "1.2.3.4"

	target_ipv4_document = {
            'target_ipv4_dig':ipv4_from_dig
	}
	# Get the current date and time
	current_datetime = datetime.now()

	# Format the date and time in the desired format
	formatted_datetime = current_datetime.strftime("%b-%d-%Y_%H:%M:%S")

	# current time and date
	time_date = formatted_datetime

	last_updated_document = {
            'last_updated':time_date
	}

	# defining template for target info
	doc_target_info = {
		'target': '',
        'ipv4': '',
		'creation_time': '',
        'last_updated': ''
	}

	# adding target information into doc_target_info variable
	source = current_directory + "/txts/target_info.txt"
	# doc_target_info =  txt_to_doc_mod.txt_to_doc(source, doc_target_info)

	# storing data in target_info_collection
	target_info_collection.insert_one(target_name_document)
	target_info_collection.insert_one(target_ipv4_document)
	target_info_collection.insert_one(last_updated_document)
	# target_info_collection.insert_one(doc_target_info)

	return target_info_collection
