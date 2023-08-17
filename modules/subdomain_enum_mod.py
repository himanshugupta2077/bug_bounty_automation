#!/usr/bin/python3

import subprocess
import argparse
import os

def subscrapper_runner(tool_output_file_path, domain_name, output_file_path):
    print("[+] Running subscrapper")
    cmd = f"subscraper -r {tool_output_file_path}" + "/subscraper_out1.txt " + f"{domain_name}" + " > /dev/null && cat " + f"{tool_output_file_path}" + "/subscraper_out1.txt " + "> " + f"{output_file_path}"
    subprocess.run(cmd, shell=True)

    cmd = f"subscraper -r {tool_output_file_path}" + "/subscraper_out2.txt " + f"{domain_name}" + " > /dev/null && cat " + f"{tool_output_file_path}" + "/subscraper_out2.txt " + ">> " + f"{output_file_path}"
    subprocess.run(cmd, shell=True)

    cmd = f"subscraper -r {tool_output_file_path}" + "/subscraper_out3.txt " + f"{domain_name}" + " > /dev/null && cat " + f"{tool_output_file_path}" + "/subscraper_out3.txt " + ">> " + f"{output_file_path}"
    subprocess.run(cmd, shell=True)

    cmd = f"subscraper -r {tool_output_file_path}" + "/subscraper_out4.txt " + f"{domain_name}" + " > /dev/null && cat " + f"{tool_output_file_path}" + "/subscraper_out4.txt " + ">> " + f"{output_file_path}"
    subprocess.run(cmd, shell=True)

    cmd = f"subscraper -r {tool_output_file_path}" + "/subscraper_out5.txt " + f"{domain_name}" + " > /dev/null && cat " + f"{tool_output_file_path}" + "/subscraper_out5.txt " + ">> " + f"{output_file_path}"
    subprocess.run(cmd, shell=True)

def subfinder_runner(tool_output_file_path, domain_name, output_file_path):
    print("[+] Running subfinder")
    cmd = f"subfinder -d {domain_name}" + " > /dev/null 2>&1 > " + f"{tool_output_file_path}" + "/subfinder_out1.txt && cat " + f"{tool_output_file_path}" + "/subfinder_out1.txt >> " + f"{output_file_path}"
    subprocess.run(cmd, shell=True)

    cmd = f"subfinder -d {domain_name}" + " > /dev/null 2>&1 > " + f"{tool_output_file_path}" + "/subfinder_out2.txt && cat " + f"{tool_output_file_path}" + "/subfinder_out2.txt >> " + f"{output_file_path}"
    subprocess.run(cmd, shell=True)

    cmd = f"subfinder -d {domain_name}" + " > /dev/null 2>&1 > " + f"{tool_output_file_path}" + "/subfinder_out3.txt && cat " + f"{tool_output_file_path}" + "/subfinder_out3.txt >> " + f"{output_file_path}"
    subprocess.run(cmd, shell=True)

    cmd = f"subfinder -d {domain_name}" + " > /dev/null 2>&1 > " + f"{tool_output_file_path}" + "/subfinder_out4.txt && cat " + f"{tool_output_file_path}" + "/subfinder_out4.txt >> " + f"{output_file_path}"
    subprocess.run(cmd, shell=True)

    cmd = f"subfinder -d {domain_name}" + " > /dev/null 2>&1 > " + f"{tool_output_file_path}" + "/subfinder_out5.txt && cat " + f"{tool_output_file_path}" + "/subfinder_out5.txt >> " + f"{output_file_path}"
    subprocess.run(cmd, shell=True)

def assetfinder_runner(tool_output_file_path, domain_name, output_file_path):
    print("[+] Running assetfinder")

    cmd = "assetfinder " + f"{domain_name}" + " | grep " + f"{domain_name}" + " > " f"{tool_output_file_path}" + "/assetfinder_out5.txt && cat " + f"{tool_output_file_path}" + "/assetfinder_out5.txt" + " >> " + f"{output_file_path}"
    subprocess.run(cmd, shell=True)

def sorter(output_file_path, current_path, domain_name):
    cmd = "cat " + f"{output_file_path}" + " | sort | sort -u > " + f"{current_path}" + "/" + f"{domain_name}" + "/2_sorted.txt"
    subprocess.run(cmd, shell=True)

    filename = f"{current_path}" + "/" + f"{domain_name}" + "/2_sorted.txt"

    with open(filename, "r") as file:
        lines = file.readlines()

    num_lines = len(lines)
    print("[+] Unique subdomains found:", num_lines)

def find_alive(current_path, domain_name):
    sorted_file = f"{current_path}" + "/" + f"{domain_name}" + "/2_sorted.txt"
    output_file_path_alive = f"{current_path}" + "/" + f"{domain_name}" + "/3_alive.txt"
    
    # update this cmd so that it check all diff ports:
    # this can be called a port scan 
    # cat all.txt| httpx -silent -ports 80,443,3000,8080,8000,8081,8008,8888,8443,9000,9001,9090 | tee -a alive.txt
    # source: https://infosecwriteups.com/story-of-my-first-valid-critical-bug-22029115f8d7

    cmd = f"cat {sorted_file} | httpx > {output_file_path_alive}"
    subprocess.run(cmd, shell=True)

    filename = f"{current_path}" + "/" + f"{domain_name}" + "/3_alive.txt"

    with open(filename, "r") as file:
        lines = file.readlines()

    num_lines = len(lines)
    print("[+] Alive subdomains found:", num_lines)

    return filename

def main(target):
    current_path = os.getcwd()
    if not os.path.exists(target):
        os.makedirs(target)

    current_path = os.getcwd()
    if not os.path.exists(target + "/tool_output"):
        os.makedirs(target + "/tool_output")

    domain_name = target
    output_file_path = f"{current_path}" + "/" + f"{domain_name}" + "/1_found.txt"
    tool_output_file_path = f"{current_path}" + "/" + f"{domain_name}" + "/tool_output"

    subscrapper_runner(tool_output_file_path, domain_name, output_file_path)
    subfinder_runner(tool_output_file_path, domain_name, output_file_path)
    assetfinder_runner(tool_output_file_path, domain_name, output_file_path)
    sorter(output_file_path, current_path, domain_name)
    filename = find_alive(current_path, domain_name)

    return filename
