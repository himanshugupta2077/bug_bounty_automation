#!/bin/bash

# Install pdtm
echo "Installing pdtm..."
go install -v github.com/projectdiscovery/pdtm/cmd/pdtm@latest

# Check if pdtm is installed successfully
if command -v pdtm &> /dev/null; then
    echo "pdtm is installed successfully."
    
    # Run pdtm -install-all
    echo "Running pdtm -install-all..."
    pdtm -install-all
    
    echo "pdtm -install-all completed."
else
    echo "pdtm installation failed."
fi

echo ''
echo "source ~/.zshrc"
