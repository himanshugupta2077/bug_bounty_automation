from modules import db_init_mod
from modules import txt_to_doc_mod
from modules import target_info_mod
from modules import nmap_mod
import os
from pprint import pprint

def talking_to_db():
	username = "ronin"
	password = "securepass123"

	# Create a new user in the database
	client, db = db_init_mod.create_db_user(username, password)

	return client, db

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

if __name__ == "__main__":
	current_directory = os.getcwd()
	client, db = talking_to_db()

	collec_target_info = target_info_mod.get_target_info(db, current_directory)

	document = collec_target_info.find_one(filter={}, projection={})

	# Print the document beautifully using pprint
	pprint(document)

	client.close()
