#!/bin/bash

# Change to the Downloads directory
cd ~/Downloads

# Download Go
wget https://go.dev/dl/go1.21.0.linux-amd64.tar.gz

# Extract the downloaded tarball
tar -xvf go1.21.0.linux-amd64.tar.gz

# Move back to the home directory
cd ..

# Copy the extracted Go directory to /usr/local/
sudo cp -r Downloads/go/ /usr/local/

# Add Go paths to the user's profile
echo '' >> ~/.profile
echo 'PATH="$PATH:/home/kali/go"' >> ~/.profile
echo 'PATH="$PATH:/usr/local/go/bin"' >> ~/.profile
echo 'PATH="$PATH:/home/kali/go/bin"' >> ~/.profile

# Inform the user
echo ''
echo "run the following:"
echo "source ~/.profile"
