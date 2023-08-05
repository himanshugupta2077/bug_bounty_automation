from modules import txt_to_doc_mod
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

def get_target_info(db, current_directory):
	# creating collection for storing target info
	collec_target_info = db['target_info']

	# defining template for target info
	doc_target_info = {
		'ipv4': '',
		'domain': '',
		'creation_time': '',
	}

	# adding target information into doc_target_info variable
	source = current_directory + "/txts/target_info.txt"
	doc_target_info =  txt_to_doc_mod.txt_to_doc(source, doc_target_info)

	# storing data in collec_target_info
	collec_target_info.insert_one(doc_target_info)

	return collec_target_info
