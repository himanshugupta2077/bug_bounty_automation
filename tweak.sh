#!/bin/bash

# status indicators
blueinfo='\e[0;34m[i]\e[0m'
greenplus='\e[1;32m[+]\e[0m'
yellowinfo='\e[1;33m[i]\e[0m'
yellowplus='\e[1;33m[+]\e[0m'
yellowminus='\e[1;33m[-]\e[0m'
redminus='\e[1;31m[-]\e[0m'
redexclaim='\e[1;31m[!]\e[0m'
redstar='\e[1;31m[*]\e[0m'

# current location
CURRENT_LOCATION=$(pwd)

# current user
CURRENT_USER=$(logname)

# package folder to download packages to install
PACKAGE_FOLDER="/home/$CURRENT_USER/Downloads/"

check_for_root() {
    if [ "$EUID" -ne 0 ]; then 
        echo -e "\n$redexclaim script must be run with root"
        echo -e "$redexclaim exiting"
        exit
    fi
    }

line() {
    echo -e "\n---------------------------------------------------------------------------------------------"
    }

show_system_info() {
    echo -e "\n$blueinfo system info \n"
    echo user: $CURRENT_USER
    echo working directory: $CURRENT_LOCATION
    sleep 0.5
    line
    }

apt_update() {
    echo -e "\n$greenplus running: sudo apt update \n"
    eval sudo apt -y update -o Dpkg::Progress-Fancy="1"
    }

apt_upgrade() {
    echo -e "\n$greenplus running: sudo apt upgrade \n"
    eval sudo apt -y upgrade -o Dpkg::Progress-Fancy="1"
    }

apt_autoremove() {
    echo -e "\n$greenplus running: sudo apt autoremove \n"
    eval sudo apt -y autoremove -o Dpkg::Progress-Fancy="1"
    line
    }

ask_for_adding_new_user() {
    echo ""
    read -r -p $'\e[1;33m[++]\e[0m Do you want to add a new user? [Y/n]: ' response

    # Use default answer 'Y' if no input provided
    if [ -z "$response" ]; then
      response="Y"
    fi

    # Convert response to lowercase for comparison
    response=${response,,}

    # Check user's response
    if [ "$response" != "y" ]; then
        echo -e "\n$blueinfo Skipping user creation "
        line
        sleep 0.5
    else add_new_user
    fi
    }
    
add_new_user() {

    echo -e "\n$greenplus adding new user \n"
    
    read -p "Enter the username (press Enter for default 'tester'): " username

    # Use default username if no input provided
    if [ -z "$username" ]; then
      username="tester"
    fi

    # Add the new user
    echo -e "\n$greenplus running: sudo adduser "$username" \n"

    sudo adduser "$username"

    echo -e "\n$blueinfo new user '$username' has been created"

    line
    sleep 0.5

    echo -e "\n$greenplus granting sudo privileges to $username "

    echo -e "\n$greenplus running: sudo usermod -aG sudo $username "

    sudo usermod -aG sudo "$username"

    echo -e "\n$blueinfo new user $username has been added to sudo group"

    line
    sleep 0.5

    echo -e "\n$greenplus adding $username to vboxsf group\n"

    findgroup=$(groups $username | grep -i -c "vboxsf")

    if [ $findgroup = 1 ]
        then
        echo -e "$yellowinfo $username is already a member of vboxsf group"
    else
        eval sudo adduser $username vboxsf
        echo -e "\n$blueinfo new user $username has been added to vboxsf group"
    fi

    line
    sleep 0.5

    echo -e "\n$blueinfo log in with new user "    
    echo -e "\n$blueinfo bye!"
    exit

    }

change_keyboard_shortcuts() {
    # create copy of original file
    echo -e "\n$greenplus changing keyboard shortcuts \n"
    cp /home/$CURRENT_USER/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml /home/$CURRENT_USER/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts-backup.xml
    exit_status1=$?

    # replace original file by configured one
    cp $CURRENT_LOCATION/config-files/configured-xfce4-keyboard-shortcuts.xml /home/$CURRENT_USER/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml
    exit_status2=$?

    if [ $exit_status1 -eq 0 ] && [ $exit_status2 -eq 0 ]; then
        echo -e "replaced /home/$CURRENT_USER/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml with $CURRENT_LOCATION/config-files/configured-xfce4-keyboard-shortcuts.xml"
        echo -e "\n$blueinfo restart the machine for the keyboard shortcuts to work"
        echo -e "\n$blueinfo to restore the original file, run: \n\ncp /home/$CURRENT_USER/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts-backup.xml /home/$CURRENT_USER/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml"
    fi

    line
    sleep 0.5

    }

install_sublime_text() {
    echo -e "\n$greenplus looking for sublime-text \n"
    if subl -v >/dev/null 2>&1; then
        echo -e "$blueinfo sublime-text already installed"
    else
        echo -e "$yellowminus sublime-text is not installed"
        echo -e "\n$greenplus installing sublime-text \n"

        if [ -e "/$PACKAGE_FOLDER/sublime-text_build-4143_amd64.deb" ]; then
            eval sudo dpkg -i $PACKAGE_FOLDER/sublime-text_build-4143_amd64.deb    
        else
            eval wget -P $PACKAGE_FOLDER https://download.sublimetext.com/sublime-text_build-4143_amd64.deb    
            eval sudo dpkg -i $PACKAGE_FOLDER/sublime-text_build-4143_amd64.deb
        fi

        if dpkg -s "sublime-text" >/dev/null 2>&1; then
            echo -e "\n$blueinfo sublime-text installed"
        else 
            echo -e "$redexclaim unable to install sublime-text"
            exit
        fi
    fi
    
    line
    sleep 0.5
    }

install_terminator() {

    APPLICATION_NAME="terminator"

    echo -e "\n$greenplus looking for $APPLICATION_NAME \n"
    if terminator -v >/dev/null 2>&1; then
        echo -e "$blueinfo $APPLICATION_NAME already installed"
    else
        echo -e "$yellowminus $APPLICATION_NAME is not installed \n"
        echo -e "$greenplus installing $APPLICATION_NAME\n"

        eval sudo apt install $APPLICATION_NAME -y

        if terminator -v >/dev/null 2>&1; then
            echo -e "\n$blueinfo $APPLICATION_NAME installed"
        else 
            echo -e "$redexclaim unable to install $APPLICATION_NAME"
            exit
        fi
    fi

    line
    sleep 0.5
    }

set_terminator_to_default() {
    # Check if Terminator is installed
    if ! command -v terminator &> /dev/null; then
        echo -e "terminator is not installed"
        exit 1
    fi

    echo -e "\n$greenplus changing default terminal emulator to terminator"

    helpers_file="/home/$CURRENT_USER/.config/xfce4/helpers.rc"
    terminal_line="TerminalEmulator=terminator"

    # Check if helpers.rc file exists
    if [ -f "$helpers_file" ]; then
      # Check if the terminal line exists in the file
      if grep -q "$terminal_line" "$helpers_file"; then
        echo -e "\n$blueinfo terminator is already set to default terminal emulator"
      else
        # Check if any TerminalEmulator line exists
        if grep -q "TerminalEmulator=" "$helpers_file"; then
          # Replace the existing TerminalEmulator line with terminator
          sed -i "s/TerminalEmulator=.*/$terminal_line/" "$helpers_file"
          echo -e "\n$blueinfo default terminal emulator is set to terminator"
        else
          # Add the TerminalEmulator line at the end of the file
          echo -e "$terminal_line" >> "$helpers_file"
          echo -e "\n$blueinfo default terminal emulator is set to terminator"
        fi
      fi
    else
      # Create the helpers.rc file and add the TerminalEmulator line
      echo "$terminal_line" > "$helpers_file"
      echo -e "\n$blueinfo default terminal emulator is set to terminator"
    fi

    line
    sleep 0.5
    }

add_terminator_config() { 
    # Check if Terminator is installed
    if ! command -v terminator &> /dev/null; then
        echo -e "terminator is not installed"
        exit 1
    fi

    echo -e "\n$greenplus adding terminator config file"

    if ! [ -d "/home/$CURRENT_USER/.config/terminator/" ]; then
        mkdir -p /home/$CURRENT_USER/.config/terminator/
    fi

    cp $CURRENT_LOCATION/config-files/terminator-config /home/$CURRENT_USER/.config/terminator/config
    chown -R kali /home/$CURRENT_USER/.config/terminator/
    echo -e "\n$blueinfo added terminator config file in /home/$CURRENT_USER/.config/terminator/config"
    line
    sleep 0.5
    }

install_mongodb() {

    APPLICATION_NAME="mongodb"

    echo -e "\n  $greenplus looking for $APPLICATION_NAME \n"
    if mongod --version >/dev/null 2>&1; then
        echo -e "  $blueplus $APPLICATION_NAME already installed"
        echo -e "\n  $blueplus to start mongodb run: \n\nsudo systemctl enable mongodb\nsudo service mongodb start"
        echo -e "\n  $blueplus to check mongodb status run: \n\nsudo systemctl status mongodb"
    else
        echo -e "  $yellowminus $APPLICATION_NAME is not installed \n"
        echo -e "  $greenplus installing $APPLICATION_NAME\n"

        eval sudo apt install $APPLICATION_NAME -y

        if mongod --version >/dev/null 2>&1; then
            echo -e "\n  $blueplus $APPLICATION_NAME installed"
            echo -e "\n  $blueplus to start mongodb run: \n\nsudo service mongodb start\nsudo systemctl enable mongodb"
            echo -e "\n  $blueplus to check mongodb status run: \n\nsudo systemctl status mongodb"
        else 
            echo -e "  $redexclaim unable to install $APPLICATION_NAME"
            exit
        fi
    fi
    }

bye_bye() {
    echo -e "\n$blueinfo restart the machine for all the changes to take place"
    echo -e "\n$blueinfo bye!"

    line
    sleep 0.5
    }

check_for_root
show_system_info
# echo -e "\n$blueinfo updating machine"
# apt_update
# apt_upgrade
# apt_autoremove
ask_for_adding_new_user
# change_keyboard_shortcuts
# install_sublime_text
# install_terminator
# set_terminator_to_default
# add_terminator_config
install_mongodb
bye_bye
