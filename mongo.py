from pymongo import MongoClient
from pymongo.errors import OperationFailure

def create_new_db_user(): 
	# initiate a new db and db user

	username = 'ronin'
	password = 'test123'

	try:
		client = MongoClient()
		admin_db = client['admin']
	
	except OperationFailure as e:
		print(f"Failed to connect to MongoDB: {e}")
		exit(1)

	try:
		admin_db.command('createUser', username, pwd=password, roles=['readWrite'])
		print(f"User {username} created successfully.")
	except OperationFailure as e:
		print(f"Failed to create user: {e}")

	# Disconnect from admin database
	client.close()

def init_new_db():

	username = 'ronin'
	password = 'test123'
	host = 'localhost'
	port = 27017
	database_name = 'ronindb'

	# Create the MongoDB connection string with the user's credentials
	connection_string = f"mongodb://{username}:{password}@{host}:{port}/"

	try:
		# Connect to MongoDB as 'ronin' user
	    client = MongoClient(connection_string)

	    # initialize new db
	    db = client[database_name]

	except OperationFailure as e:
	    print(f"Failed to connect to MongoDB: {e}")
	    exit(1)

	return client, db

def txt_to_doc(source, destination):
	# this function will read data from txt file (formatted as per destination document) and return a document with data filled

	with open(source, 'r') as file:
	    lines = file.readlines()

	# Process each line in the text file
	for line in lines:
	    # Remove leading/trailing spaces and newline characters
	    line = line.strip()
	    # print(line)

	    # Split the line into field name and value
	    field, value = line.split('=')
	    field = field.strip()
	    value = value.strip()  # Remove surrounding single quotes if present

	    # Update the corresponding field in the document
	    if field in destination:
	        destination[field] = value
	        # print(field)
	        # print(value)

	# print(destination)

	return destination

def target_info(db):
	# creating collection for storing target info
	collec_target_info = db['target_info']

	# defining template for target info
	doc_target_info = {
		'ipv4': '',
		'domain': '',
		'creation_time': '',
	}

	# adding target information into doc_target_info variable
	source = "target_info.txt"
	doc_target_info =  txt_to_doc(source, doc_target_info)

	# storing data in collec_target_info
	collec_target_info.insert_one(doc_target_info)

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

	

if __name__ == '__main__':
	# create_new_db_user()
	client, db = init_new_db()
	target_info(db)
	client.close()