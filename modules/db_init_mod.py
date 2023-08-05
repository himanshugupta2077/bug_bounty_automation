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
    print("\n---------------------------------------------------------------------------------------------")

def is_mongodb_running():
    try:
        # Run the "sudo systemctl status mongod" command and capture the output
        result = subprocess.run(["sudo", "systemctl", "status", "mongod"], capture_output=True, text=True)

        # Check if the output contains "active (running)" indicating MongoDB is running
        if "active (running)" in result.stdout:
            print(f"\n{blueinfo} mongodb is already running; skipping initialization")
            line()
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        # Handle any exceptions that might occur during the subprocess execution
        return False

def start_mongodb():
    try:
        # Run the "sudo systemctl start mongod" command
        print(f"\n{blueinfo} initializing database")
        subprocess.run(["sudo", "systemctl", "start", "mongod"])
        print(f"\n{blueinfo} database started successfully")
        line()
    except subprocess.CalledProcessError as e:
        # Handle any exceptions that might occur during the subprocess execution
        print(f"\n{redexclaim} error starting mongodb: {e}")
        line()

def create_db_user(username, password):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["admin"]

    # Check if the user already exists
    existing_user = db.command("usersInfo", "ronin")
    if existing_user["users"]:
        print(f"\n{blueinfo} user 'ronin' already exists; skipping user creation")
        line()
        return client, db

    # Create the new user
    db.command("createUser", username, pwd=password, roles=["readWrite"])
    print(f"\n{blueinfo} user 'ronin' created successfully")
    line()
    return client, db
