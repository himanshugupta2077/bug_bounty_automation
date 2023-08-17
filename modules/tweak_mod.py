#!/usr/bin/env python
import os
import subprocess
import time
import importlib
from colorama import init, Fore, Style
import shutil
import sys

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
redstar = f"{Fore.RED}[*]{Style.RESET_ALL}"

# current location
CURRENT_LOCATION = os.getcwd()

# current user
try:
    CURRENT_USER = os.getlogin()
except OSError:
    # If os.getlogin() fails, use an alternative method
    CURRENT_USER = os.getenv('USERNAME') if os.name == 'nt' else os.getenv('USER')

# package folder to download packages to install
PACKAGE_FOLDER = f"/home/{CURRENT_USER}/Downloads/"

def line():
    print("\n----------------------------------------------------------------------------------------------------------------")

def logo():
    print("""
   ___                 ___                   _             _         _                        _   _             
  / __\_   _  __ _    / __\ ___  _   _ _ __ | |_ _   _    /_\  _   _| |_ ___  _ __ ___   __ _| |_(_) ___  _ __  
 /__\// | | |/ _` |  /__\/// _ \| | | | '_ \| __| | | |  //_ \| | | | __/ _ \| '_ ` _ \ / _` | __| |/ _ \| '_ \ 
/ \/  \ |_| | (_| | / \/  \ (_) | |_| | | | | |_| |_| | /  _  \ |_| | || (_) | | | | | | (_| | |_| | (_) | | | |
\_____/\__,_|\__, | \_____/\___/ \__,_|_| |_|\__|\__, | \_/ \_/\__,_|\__\___/|_| |_| |_|\__,_|\__|_|\___/|_| |_|
             |___/                               |___/                                                          

----------------------------------------------------------------------------------------------------------------
""")

def show_system_info():
    print(f"{blueinfo} System Info \n")
    print(f"Current User: {CURRENT_USER}")
    print(f"Working Directory: {CURRENT_LOCATION}")
    time.sleep(0.5)

def apt_update():
    print(f"\n{greenplus} Updating System... \n")
    # print(f"{greenplus} running: sudo apt update \n")
    command = "sudo apt update"
    # command = "sudo apt update > /dev/null 2>&1"
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("Error:", e)

def apt_upgrade():
    # print(f"{greenplus} running: sudo apt upgrade \n")
    command = "sudo apt -y upgrade"
    # command = "sudo apt -y upgrade > /dev/null 2>&1"
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("Error:", e)

def apt_autoremove():
    # print(f"\n{greenplus} running: sudo apt autoremove \n")
    command = "sudo apt -y autoremove"
    # command = "sudo apt -y autoremove > /dev/null 2>&1"
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("Error:", e)

def install_mongodb():
    try:
        subprocess.run(["which", "mongod"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        print(f"\n{blueinfo} MongoDB already installed. Skipping Installation.")
    except subprocess.CalledProcessError:
        print(f"\n{yellowminus} MongoDB not found. Installing MongoDB...\n")
        try:
            command = "sudo apt install mongodb -y"
            # command = "sudo apt install mongodb > /dev/null 2>&1"
            try:
                subprocess.run(command, shell=True, check=True)
            except subprocess.CalledProcessError as e:
                print("Error:", e)
            subprocess.run(["which", "mongod"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            print(f"\n{blueinfo} MongoDB successfully installed.")
        except subprocess.CalledProcessError:
            print(f"{redexclaim} Unable to install MongoDB.")
            exit()

def install_docker():
    def check_docker_installed():
        try:
            subprocess.run(['docker'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            return True
        except FileNotFoundError:
            return False

    def install_docker():
        try:
            subprocess.run(['sudo', 'apt', 'install', 'docker.io', '-y'], check=True)
            print("Docker has been installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install Docker: {e}")

    def check_docker_running():
        try:
            subprocess.run(['sudo', 'systemctl', 'is-active', 'docker'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            print("Docker is currently running.")
        except subprocess.CalledProcessError:
            print("Docker is not running.")

    if check_docker_installed():
        print("Docker is already installed.")
    else:
        print("Docker is not installed. Installing...")
        install_docker()

    check_docker_running()

def install_subscrapper():
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

def install_subfinder():
    pass

def install_assetfinder():
    pass

def install_pip_pymongo():
    command = "pip install pymongo"
    subprocess.run(command, shell=True, check=True)

def install_go():
    command = "bash modules/install_go.sh"
    subprocess.run(command, shell=True)

def install_project_discovery_tools():
    command = "bash modules/install_pdtm.sh"
    subprocess.run(command, shell=True)

print(f"\n{blueinfo} Installing pip pymongo:\n")
install_pip_pymongo()