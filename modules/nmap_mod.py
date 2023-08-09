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

def nmap_result():
	collec_nmap_result = db['nmap_results']

	doc_nmap_result = {
		'scan_date': '',
		'target_ipv4': '',
		'open_ports': [],
		'os_details': '',
		'vulnerabilities': {}
	}

	collec_nmap_result.insert_one(doc_nmap_result)
