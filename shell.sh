#!/bin/bash

# check if running as root or not
if [ "$EUID" -ne 0 ]
	then echo -e "\nScript must be run with root.\nrun: sudo ./pimpmylinux.sh"
	exit
fi

# current user
    finduser=$(logname)
    echo user: $finduser

# system architecture
    archtype=$(uname -m)
    if [ "$archtype" == "aarch64" ]; 
      then 
        arch="arm64"
		echo architecture: $arch
    fi

    if [ "$archtype" == "x86_64" ]; 
      then
        arch="amd64"
        echo architecture: $arch
    fi

# check linux distribution
distro=$(uname -a | grep -i -c "kali") # distro check
if [ $distro -ne 1 ]
	then echo -e "\n $blinkexclaim Kali Linux Not Detected - WSL/WSL2/Anything else is unsupported $blinkexclaim \n"; exit
else
	echo distribution: kali linux 
fi

# current destination
	current_destination=$(pwd)
	echo current destination: $current_destination

# change keyboard shortcuts
	# create copy of original file
	cp /home/${finduser}/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml ${current_destination}/keyboard-shortcuts-backup.xml
	exit_status1=$?
	# replace original file by configured one
	cp ${current_destination}/configured-xfce4-keyboard-shortcuts.xml /home/${finduser}/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml
	exit_status2=$?

	if [ $exit_status1 -eq 0 ] && [ $exit_status2 -eq 0 ]; then
		echo "original keyboard shortcut file replaced by the configured one."
	fi

# for vbox_fix_shared_folder_permission_denied
    # findgroup=$(groups $finduser | grep -i -c "vboxsf")

# Logging
    LOG_FILE=pimpmylinux.log
    exec > >(tee ${LOG_FILE}) 2>&1

# silent mode
    # silent=''                  # uncomment to see all output
    # # silent='>/dev/null 2>&1' # uncomment to hide all output10
    # export DEBIAN_FRONTEND=noninteractive
    # export PYTHONWARNINGS=ignore

