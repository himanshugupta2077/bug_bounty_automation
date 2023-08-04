import pymongo

def create_db_user(username, password):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["admin"]

    # Check if the user already exists
    existing_user = db.command("usersInfo", "ronin")
    if existing_user["users"]:
        print("User 'ronin' already exists. Skipping user creation.")
        return client, db

    # Create the new user
    db.command("createUser", username, pwd=password, roles=["readWrite"])
    print("User 'ronin' created successfully.")
    return client, db
