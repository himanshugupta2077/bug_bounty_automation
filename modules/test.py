import pymongo

def check_user_exist(username, db_url, db_name, db_user, db_password):
	try:
		# Establish a connection to the MongoDB database
		client = pymongo.MongoClient(db_url, username=db_user, password=db_password)
		db = client[db_name]

		# Fetch the list of users from the admin database
		admin_db = client.admin
		users = admin_db.command('usersInfo')

		# Check if the given username exists in the users list
		for user in users['users']:
			if user['user'] == username:
				return True

		return False

	except pymongo.errors.OperationFailure as e:
		print(f"Error: {e}")
		return False

if __name__ == "__main__":
	# Provide your MongoDB connection details
	db_user = 'ronin'
	db_password = 'test123'
	host = 'localhost'
	port = 27017
	db_name = 'ronindb'
	db_url = f"mongodb://{db_user}:{db_password}@{host}:{port}/"

	username_to_check = db_user
	if check_user_exist(username_to_check, db_url, db_name, db_user, db_password):
		print(f"User '{username_to_check}' exists in the database.")
	else:
		print(f"User '{username_to_check}' does not exist in the database.")
