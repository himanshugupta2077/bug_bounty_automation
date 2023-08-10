from colorama import init, Fore, Style
import pymongo
import subprocess

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

def line():
	print("\n----------------------------------------------------------------------------------------------------------------")

def is_mongodb_service_running():
	try:
		# Run the "sudo systemctl status mongod" command and capture the output
		result = subprocess.run(["sudo", "systemctl", "status", "mongodb"], capture_output=True, text=True)

		# Check if the output contains "active (running)" indicating MongoDB is running
		if "active (running)" in result.stdout:
			print(f"{blueinfo} MongoDB service is already running. Skipping Initialization.")
			line()
			return True
		else:
			return False
	except subprocess.CalledProcessError:
		# Handle any exceptions that might occur during the subprocess execution
		return False

def start_mongodb_service():
	try:
		# Run the "sudo systemctl start mongod" command
		print(f"\n{blueinfo} Initializing Database...")
		subprocess.run(["sudo", "systemctl", "start", "mongodb"])
		print(f"{blueinfo} Database started successfully.")
		line()
	except subprocess.CalledProcessError as e:
		# Handle any exceptions that might occur during the subprocess execution
		print(f"\n{redexclaim} Error starting MongoDB: {e}")
		line()

def init_db():

	client = pymongo.MongoClient("mongodb://localhost:27017/")
	db = client["ronindb"]

	return client, db

def database_info(client, database_names):
	print(f"\n{blueinfo} Database Info\n")
	for db_name in database_names:
		print("Database:", db_name)
		
		# Get a list of all collection names in the current database
		db = client[db_name]
		collection_names = db.list_collection_names()
		
		# Iterate through each collection and print its name
		for collection_name in collection_names:
			print("Collection:", collection_name)
			
	print("")

	print(f"{blueinfo} Target Info\n")

	return client, db

def init_mongodb_service():
	if is_mongodb_service_running():
		pass
	else:
		start_mongodb_service()
