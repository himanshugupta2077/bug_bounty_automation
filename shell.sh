#!/bin/bash

# unicorn puke:
red=$'\e[1;31m'
green=$'\e[1;32m'
blue=$'\e[1;34m'
magenta=$'\e[1;35m'
cyan=$'\e[1;36m'
yellow=$'\e[1;93m'
white=$'\e[0m'
bold=$'\e[1m'
norm=$'\e[21m'
reset=$'\e[0m'
color_nocolor='\e[0m'
color_black='\e[0;30m'
color_grey='\e[1;30m'
color_red='\e[0;31m'
color_light_red='\e[1;31m'
color_green='\e[0;32m'
color_light_green='\e[1;32m'
color_brown='\e[0;33m'
color_yellow='\e[1;33m'
color_blue='\e[0;34m'
color_light_blue='\e[1;34m'
color_purple='\e[0;35m'
color_light_purple='\e[1;35m'
color_cyan='\e[0;36m'
color_light_cyan='\e[1;36m'
color_light_grey='\e[0;37m'
color_white='\e[1;37m'

# nuke impacket function launch_code generator
launch_codes_alpha=$(echo $((1 + RANDOM % 9999)))
launch_codes_beta=$(echo $((1 + RANDOM % 9999)))
launch_codes_charlie=$(echo $((1 + RANDOM % 9999)))

# status indicators
blueplus='\e[0;34m[++]\e[0m'
greenplus='\e[1;32m[++]\e[0m'
greenminus='\e[1;33m[--]\e[0m'
redminus='\e[1;31m[--]\e[0m'
redexclaim='\e[1;31m[!!]\e[0m'
redstar='\e[1;31m[**]\e[0m'
blinkexclaim='\e[1;31m[\e[5;31m!!\e[0m\e[1;31m]\e[0m'
fourblinkexclaim='\e[1;31m[\e[5;31m!!!!\e[0m\e[1;31m]\e[0m'

# current location
CURRENT_LOCATION=$(pwd)

# current user
CURRENT_USER=$(logname)

# package folder to download packages to install
PACKAGE_FOLDER="/home/{$CURRENT_USER}/Downloads/"

# system architecture
archtype=$(uname -m)
if [ "$archtype" == "aarch64" ]; then
	SYSTEM_ARCH="arm64"
fi

if [ "$archtype" == "x86_64" ]; then
	SYSTEM_ARCH="amd64"
fi

check_for_root() {
    if [ "$EUID" -ne 0 ]; then 
    	echo -e "\n$redexclaim Script must be run with root"
        echo -e "$redexclaim exiting"
    	exit
    fi
    }

check_linux_distribution() {
    distro=$(uname -a | grep -i -c "kali") # distro check
    if [ $distro -ne 1 ]; then
        echo -e "\n $blinkexclaim Kali Linux Not Detected - WSL/WSL2/Anything else is unsupported $blinkexclaim \n"; exit 
    fi
    }

show_system_info() {
    echo -e "\n  $blueplus system info \n"
    echo user: $CURRENT_USER
    echo working directory: $CURRENT_LOCATION
    echo architecture: $SYSTEM_ARCH
    }

apt_update() {
    echo -e "\n  $greenplus running: sudo apt update \n"
    eval sudo apt -y update -o Dpkg::Progress-Fancy="1"
    }

apt_upgrade() {
    echo -e "\n  $greenplus running: sudo apt upgrade \n"
    eval sudo apt -y upgrade -o Dpkg::Progress-Fancy="1"
    }

apt_autoremove() {
    echo -e "\n  $greenplus running: sudo apt autoremove \n"
    eval sudo apt -y autoremove -o Dpkg::Progress-Fancy="1"
    }

change_keyboard_shortcuts() {
	# create copy of original file
    echo -e "\n  $greenplus changing keyboard shortcuts \n"
	cp /home/${CURRENT_USER}/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml ${CURRENT_LOCATION}/xfce4-keyboard-shortcuts-backup.xml
	exit_status1=$?
	echo "backed up /home/${CURRENT_USER}/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml to ${CURRENT_LOCATION}/xfce4-keyboard-shortcuts-backup.xml"

	# replace original file by configured one
	cp ${CURRENT_LOCATION}/configured-xfce4-keyboard-shortcuts.xml /home/${CURRENT_USER}/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml
	exit_status2=$?

	if [ $exit_status1 -eq 0 ] && [ $exit_status2 -eq 0 ]; then
        echo -e "replaced /home/${CURRENT_USER}/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml with ${CURRENT_LOCATION}/configured-xfce4-keyboard-shortcuts.xml"
        echo -e "\n  $blueplus log out and log in again for the keyboard shortcuts to work"
    fi
    }

add_user_to_vboxsf() {
    echo -e "\n  $greenplus adding user to vboxsf group\n"

    findgroup=$(groups $CURRENT_USER | grep -i -c "vboxsf")

    if [ $findgroup = 1 ]
        then
        echo -e "user is already a member of vboxsf group"
    else
        eval adduser $CURRENT_USER vboxsf
        echo -e "\n  $greenplus fix applied : virtualbox permission denied on shared folder"
        echo -e "user added to vboxsf group "
    fi
    }

install_sublime_text() {
    echo -e "\n  $greenplus installing sublime-text \n"
    if dpkg -s "sublime-text" >/dev/null 2>&1; then
        echo "sublime-text already installed"
    else
        echo "sublime-text is not installed"
        echo "installing sublime-text"

        if [ -e "/${PACKAGE_FOLDER}/sublime-text_build-4143_amd64.deb" ]; then
            eval sudo dpkg -i ${PACKAGE_FOLDER}/sublime-text_build-4143_amd64.deb    
        else
            eval wget -P ${PACKAGE_FOLDER} https://download.sublimetext.com/sublime-text_build-4143_amd64.deb    
            eval sudo dpkg -i ${PACKAGE_FOLDER}/sublime-text_build-4143_amd64.deb
        fi

        if dpkg -s "sublime-text" >/dev/null 2>&1; then
            echo "sublime-text installed"
        else 
            echo unable to install sublime-text
            exit
        fi
    fi
    }

install_terminator() {

    APPLICATION_NAME="terminator"

    echo -e "\n  $greenplus installing $APPLICATION_NAME \n"
    if dpkg -s "$APPLICATION_NAME" >/dev/null 2>&1; then
        echo "$APPLICATION_NAME already installed"
    else
        echo "$APPLICATION_NAME is not installed"
        echo "installing $APPLICATION_NAME\n"

        eval sudo apt install $APPLICATION_NAME -y

        if dpkg -s "$APPLICATION_NAME" >/dev/null 2>&1; then
            echo "\n$APPLICATION_NAME installed"
        else 
            echo unable to install $APPLICATION_NAME
            exit
        fi
    fi
    }

check_for_root
check_linux_distribution
show_system_info
sleep 1
# apt_update
# apt_upgrade
# apt_autoremove
change_keyboard_shortcuts
sleep 1
add_user_to_vboxsf
sleep 1
install_sublime_text
sleep 1
install_terminator
