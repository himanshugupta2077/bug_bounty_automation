import argparse
import sys
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

def line():
    print("\n----------------------------------------------------------------------------------------------------------------")

def parse_single_target(target):

    result = extract_after_asterisk_dot(target)

    if result:
        target = [target]
        # target = [result]
        target_type = 0
        return target, target_type

    else:
        target_type = 1
        target = [target]
        return target, target_type

def parse_multiple_targets(filename):
    with open(filename, "r") as file:
        targets = file.read().splitlines()

    target_type = 2
    return targets, target_type

def extract_after_asterisk_dot(target):
    # Find the index of the first occurrence of "*." in the input string
    asterisk_dot_index = target.find("*.")
    
    # Check if "*." is present in the input string
    if asterisk_dot_index != -1:
        # Extract the substring after "*."
        result_string = target[asterisk_dot_index + 2:]
        return result_string
    else:
        return None  # Return None if "*." is not found in the input string

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Parse single or multiple targets")

    # Add the -t argument for single target
    parser.add_argument("-t", "--target", help="Specify a single target to parse")

    # Add the -f argument for multiple targets in a file
    parser.add_argument("-f", "--file", help="Specify a text file with multiple targets")

    # Parse the arguments
    args = parser.parse_args()

    if args.target and args.file:
        print("Error: Both single target and file options cannot be used together.")
        return

    if args.target:
        target, target_type = parse_single_target(args.target)
    elif args.file:
        target, target_type = parse_multiple_targets(args.file)
    else:
        print(f"\n{redexclaim} Error: No target given. Please provide a target.")
        print("\nusage: main.py [-h] [-t TARGET] [-f FILE]")
        print("""
options:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        Specify a single target to parse
  -f FILE, --file FILE  Specify a text file with multiple targets\n""")
        sys.exit()

    return target, target_type
