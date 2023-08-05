#!/usr/bin/env python
import os
import subprocess
import time
from colorama import init, Fore, Style

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
    print("\n---------------------------------------------------------------------------------------------")

def show_system_info():
    print(f"\n{blueinfo} system info \n")
    print(f"user: {CURRENT_USER}")
    print(f"working directory: {CURRENT_LOCATION}")
    time.sleep(0.5)
    line()

def apt_update():
    print(f"\n{greenplus} running: sudo apt update \n")
    subprocess.run(["sudo", "apt", "-y", "update", "-o", "Dpkg::Progress-Fancy=1"], check=True)

def apt_upgrade():
    print(f"\n{greenplus} running: sudo apt upgrade \n")
    subprocess.run(["sudo", "apt", "-y", "upgrade", "-o", "Dpkg::Progress-Fancy=1"], check=True)

def apt_autoremove():
    print(f"\n{greenplus} running: sudo apt autoremove \n")
    subprocess.run(["sudo", "apt", "-y", "autoremove", "-o", "Dpkg::Progress-Fancy=1"], check=True)
    line()

def install_mongodb():
    APPLICATION_NAME = "mongodb"
    print(f"\n{greenplus} looking for {APPLICATION_NAME} \n")
    try:
        subprocess.run(["which", "mongod"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        print(f"{blueinfo} {APPLICATION_NAME} already installed")
    except subprocess.CalledProcessError:
        print(f"{yellowminus} {APPLICATION_NAME} is not installed \n")
        print(f"{greenplus} installing {APPLICATION_NAME}\n")
        try:
            subprocess.run(["sudo", "apt", "install", APPLICATION_NAME, "-y"], check=True)
            subprocess.run(["which", "mongod"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            print(f"\n{blueinfo} {APPLICATION_NAME} installed")
        except subprocess.CalledProcessError:
            print(f"{redexclaim} unable to install {APPLICATION_NAME}")
            exit()
