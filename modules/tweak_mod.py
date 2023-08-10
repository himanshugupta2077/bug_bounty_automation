#!/usr/bin/env python
import os
import subprocess
import time
import importlib
from colorama import init, Fore, Style
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
    command = "sudo apt update > /dev/null 2>&1"
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("Error:", e)

def apt_upgrade():
    # print(f"{greenplus} running: sudo apt upgrade \n")
    command = "sudo apt -y upgrade > /dev/null 2>&1"
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("Error:", e)


def apt_autoremove():
    # print(f"\n{greenplus} running: sudo apt autoremove \n")
    command = "sudo apt -y autoremove > /dev/null 2>&1"
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
            command = "sudo apt install mongodb > /dev/null 2>&1"
            try:
                subprocess.run(command, shell=True, check=True)
            except subprocess.CalledProcessError as e:
                print("Error:", e)
            subprocess.run(["which", "mongod"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            print(f"\n{blueinfo} MongoDB successfully installed.")
        except subprocess.CalledProcessError:
            print(f"{redexclaim} Unable to install MongoDB.")
            exit()
