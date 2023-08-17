import subprocess
import os

def check_subscraper_installed():
    try:
        # Check if subscraper is available by running "subscraper -h"
        subprocess.run(['subscraper', '-h'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except FileNotFoundError:
        return False

print("Checking if subscraper is installed...")

if not check_subscraper_installed():
    print("subscraper is not installed. Installing...")
    
    try:
        # Clone the subscraper repository
        subprocess.run(['git', 'clone', 'https://github.com/m8sec/subscraper'], check=True)

        cwd = os.getcwd()  # Get the current working directory
        print("Current Working Directory:", cwd)

        # Change directory to subscraper
        os.chdir("subscraper")

        cwd = os.getcwd()  # Get the current working directory
        print("Current Working Directory:", cwd)

        # Build the Docker image
        subprocess.run(['sudo', 'docker', 'build', '-t', 'm8sec/subscraper', '.'], check=True)
        
        print("subscraper installed successfully.")
    except subprocess.CalledProcessError as e:
        print("Error during installation:", e)
else:
    print("subscraper is already installed and available.")


