#!/usr/bin/python3

"""
if getting python interpreter error, do this:
sudo apt-get install dos2unix
dos2unix main.py
now it should run
"""

from modules import tweak_mod
from modules import db_init_mod
from modules import target_col_mod
from modules import nmap_mod
from modules import arg_passing_mod
from modules import subdomain_enum_mod
import os

def main(target, target_type):

	# SYSTEM TWEAKING
	tweak_mod.logo()
	tweak_mod.show_system_info()
	# tweak_mod.apt_update()
	# tweak_mod.apt_upgrade()
	# tweak_mod.apt_autoremove()
	tweak_mod.install_mongodb()
	tweak_mod.install_docker()
	tweak_mod.install_subscrapper()

	# DATABASE TWEAKING
	db_init_mod.init_mongodb_service()
	client, db = db_init_mod.init_db()

	# Get a list of all database names
	# database_names = client.list_database_names()
	# db_init_mod.database_info(client, database_names)

	if target_type == 0:
		target = arg_passing_mod.extract_after_asterisk_dot(target[0])
		filename = subdomain_enum_mod.main(target)
	else: 
		filename = None

	target_col_mod.main(db, target, target_type, filename)

	print("")
	client.close()

if __name__ == "__main__":

	target, target_type = arg_passing_mod.main()
	main(target, target_type)
