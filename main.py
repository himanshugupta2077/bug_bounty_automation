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
import os

def main(target, target_info_string):

	# SYSTEM TWEAKING
	tweak_mod.logo()
	tweak_mod.show_system_info()
	tweak_mod.apt_update()
	tweak_mod.apt_upgrade()
	tweak_mod.apt_autoremove()
	tweak_mod.install_mongodb()

	# DATABASE TWEAKING
	db_init_mod.init_mongodb_service()
	client, db = db_init_mod.init_db()

	# Get a list of all database names
	database_names = client.list_database_names()
	db_init_mod.database_info(client, database_names)

	print(target_info_string)

	# current_directory = os.getcwd()
	target_info_mod.main(db, target)


	print("")
	client.close()

if __name__ == "__main__":

	target, target_info_string = arg_passing_mod.main()
	main(target, target_info_string)
