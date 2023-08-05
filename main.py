#!/usr/bin/python3

"""
if getting python interpreter error, do this:
sudo apt-get install dos2unix
dos2unix main.py
now it should run
"""

from modules import db_init_mod
from modules import target_info_mod
from modules import nmap_mod
from modules import tweak_mod
from pprint import pprint
import os

def setup_system():
	tweak_mod.show_system_info()
	# tweak_mod.apt_update()
	# tweak_mod.apt_upgrade()
	# tweak_mod.apt_autoremove()
	tweak_mod.install_mongodb()

def talking_to_db():

	if db_init_mod.is_mongodb_running():
		pass
	else:
		db_init_mod.start_mongodb()

	username = "ronin"
	password = "securepass123"

	# Create a new user in the database
	client, db = db_init_mod.create_db_user(username, password)

	return client, db

if __name__ == "__main__":

	setup_system()

	current_directory = os.getcwd()
	client, db = talking_to_db()

	collec_target_info = target_info_mod.get_target_info(db, current_directory)

	document = collec_target_info.find_one(filter={}, projection={})
	pprint(document)



	client.close()
