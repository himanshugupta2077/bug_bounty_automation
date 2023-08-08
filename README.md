# Automating Bug Bounty
This GitHub repository contains a python script that automates the bug bounty process. With the help of this tool, you can quickly set up your Kali environment, install the required tools, and perform security assessments efficiently.

## Workflow

1. **Open Fresh Kali**: Ensure you have a clean and updated Kali Linux environment.

2. **Run main.py**: Execute the main Python script to initiate the automated bug bounty process.

- **Updating System**: The script will start by updating the system to ensure you have the latest packages and security patches.

- **Installing Tools**: Necessary tools will be installed automatically. This may include MongoDB, which is used to store and manage the findings.

- **Check MongoDB Status**: The script will check if MongoDB is already running:
	- If MongoDB is up and running, the process will continue without any issues.
	- If MongoDB is not running, the script will start the MongoDB service.

- **Create Ronin User**: The script will verify the existence of a "ronin" user:
	- If the "ronin" user is already created, this step will be skipped.
	- If the "ronin" user does not exist, the script will create one for you.

- **Run Tool**: A tool will be executed and the output generated will be saved in a formatted text file for future reference and analysis by MongoDB.

- **Copy Output to MongoDB**: The script will automatically copy the findings from the text file to MongoDB for easier data management and analysis.

- **Repeat Loop**: The above process will be repeated for all the different tools used during the bug bounty process. This ensures that each tool's output is analyzed and stored in MongoDB for further comparison and study.

## Usage

To use this tool, make sure you have the following prerequisites:

- Kali Linux (or any compatible Linux distribution)
- Python 3.x

Clone this repository to your local machine using the following command:

```
git clone https://github.com/within-cells-interlink-ed/bug_bounty_automation.git
```
cd into the directory
```
cd bug_bounty_automation
```
Give the script permission to execute
```
chmod +x main.py
```
Run the script with
```
./main.py 
```
or
```
python3 main.py
```

## Contribution

Contributions to this project are welcome! If you encounter any issues or have ideas for improvements, please feel free to create an issue or submit a pull request.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute the code as per the terms of the license.

We hope this tool proves to be beneficial in automating your bug bounty process. If you have any questions or need assistance, don't hesitate to reach out.

## Happy hunting! 🐛🔍
