#!/usr/bin/python3

"""
if getting python interpreter error, do this:
sudo apt-get install dos2unix
dos2unix main.py
now it should run
"""

from modules import tweak_mod
from modules import db_init_mod
from modules import target_info_mod
from modules import nmap_mod
from modules import arg_passing_mod
from modules import subdomain_enum_mod
from pprint import pprint
import os
import sys


def main(target, target_info_string):

	setup_system()

	current_directory = os.getcwd()
	client, db = talking_to_db()

	# Get a list of all database names
	database_names = client.list_database_names()
	db_init_mod.database_info(client, database_names)

	target_info_collection = target_info_mod.get_target_info(db, current_directory, target)

	print(target_info_string)

	projection = {'_id': 0, 'target': 1, 'target_ipv4_dig': 1, 'last_updated': 1}
	documents = target_info_collection.find({}, projection)

	# Print the specified fields for each document
	for document in documents:
		pprint(document)

	print("")
	client.close()
	print("DB Closed")

def setup_system():
	tweak_mod.logo()
	tweak_mod.show_system_info()
	# tweak_mod.apt_update()
	# tweak_mod.apt_upgrade()
	# tweak_mod.apt_autoremove()
	tweak_mod.install_mongodb()

def talking_to_db():

	db_init_mod.init_mongodb()
	client, db = db_init_mod.init_db()

	return client, db

if __name__ == "__main__":

	target, target_info_string = arg_passing_mod.main()
	main(target, target_info_string)
