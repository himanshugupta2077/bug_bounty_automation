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

# status indicators
blueplus='\e[0;34m[++]\e[0m'
greenplus='\e[1;32m[++]\e[0m'
yellowminus='\e[1;33m[--]\e[0m'
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
PACKAGE_FOLDER="/home/$CURRENT_USER/Downloads/"

check_for_root() {
    if [ "$EUID" -ne 0 ]; then 
        echo -e "\n  $redexclaim Script must be run with root"
        echo -e "  $redexclaim exiting"
        exit
    fi
    }

line() {
    echo -e "\n---------------------------------------------------------------------------------------------"
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
    cp /home/$CURRENT_USER/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml /home/$CURRENT_USER/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts-backup.xml
    exit_status1=$?

    # replace original file by configured one
    cp $CURRENT_LOCATION/config-files/configured-xfce4-keyboard-shortcuts.xml /home/$CURRENT_USER/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml
    exit_status2=$?

    if [ $exit_status1 -eq 0 ] && [ $exit_status2 -eq 0 ]; then
        echo -e "replaced /home/$CURRENT_USER/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml with $CURRENT_LOCATION/config-files/configured-xfce4-keyboard-shortcuts.xml"
        echo -e "\n  $blueplus restart the machine for the keyboard shortcuts to work"
        echo -e "\n  $blueplus to restore the original file, run: \n\ncp /home/$CURRENT_USER/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts-backup.xml /home/$CURRENT_USER/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml"
    fi
    }

add_user_to_vboxsf() {
    echo -e "\n  $greenplus adding user to vboxsf group\n"

    findgroup=$(groups $CURRENT_USER | grep -i -c "vboxsf")

    if [ $findgroup = 1 ]
        then
        echo -e "  $blueplus user is already a member of vboxsf group"
    else
        eval adduser $CURRENT_USER vboxsf
        echo -e "\n  $greenplus fix applied : virtualbox permission denied on shared folder"
        echo -e "user added to vboxsf group "
    fi
    }

install_sublime_text() {
    echo -e "\n  $greenplus looking for sublime-text \n"
    if subl -v >/dev/null 2>&1; then
        echo -e "  $blueplus sublime-text already installed"
    else
        echo -e "  $yellowminus sublime-text is not installed"
        echo -e "\n  $greenplus installing sublime-text \n"

        if [ -e "/$PACKAGE_FOLDER/sublime-text_build-4143_amd64.deb" ]; then
            eval sudo dpkg -i $PACKAGE_FOLDER/sublime-text_build-4143_amd64.deb    
        else
            eval wget -P $PACKAGE_FOLDER https://download.sublimetext.com/sublime-text_build-4143_amd64.deb    
            eval sudo dpkg -i $PACKAGE_FOLDER/sublime-text_build-4143_amd64.deb
        fi

        if dpkg -s "sublime-text" >/dev/null 2>&1; then
            echo -e "\n  $blueplus sublime-text installed"
        else 
            echo -e "  $redexclaim unable to install sublime-text"
            exit
        fi
    fi
    }

install_terminator() {

    APPLICATION_NAME="terminator"

    echo -e "\n  $greenplus looking for $APPLICATION_NAME \n"
    if terminator -v >/dev/null 2>&1; then
        echo -e "  $blueplus $APPLICATION_NAME already installed"
    else
        echo -e "  $yellowminus $APPLICATION_NAME is not installed \n"
        echo -e "  $greenplus installing $APPLICATION_NAME\n"

        eval sudo apt install $APPLICATION_NAME -y

        if terminator -v >/dev/null 2>&1; then
            echo -e "\n  $blueplus $APPLICATION_NAME installed"
        else 
            echo -e "  $redexclaim unable to install $APPLICATION_NAME"
            exit
        fi
    fi
    }

set_terminator_to_default() {
    # Check if Terminator is installed
    if ! command -v terminator &> /dev/null; then
        echo -e "terminator is not installed"
        exit 1
    fi

    echo -e "\n  $greenplus changing default terminal emulator to terminator"

    helpers_file="/home/$CURRENT_USER/.config/xfce4/helpers.rc"
    terminal_line="TerminalEmulator=terminator"

    # Check if helpers.rc file exists
    if [ -f "$helpers_file" ]; then
      # Check if the terminal line exists in the file
      if grep -q "$terminal_line" "$helpers_file"; then
        echo -e "\n  $blueplus terminator is already set to default terminal emulator"
      else
        # Check if any TerminalEmulator line exists
        if grep -q "TerminalEmulator=" "$helpers_file"; then
          # Replace the existing TerminalEmulator line with terminator
          sed -i "s/TerminalEmulator=.*/$terminal_line/" "$helpers_file"
          echo -e "\n  $blueplus default terminal emulator is set to terminator"
        else
          # Add the TerminalEmulator line at the end of the file
          echo -e "$terminal_line" >> "$helpers_file"
          echo -e "\n  $blueplus default terminal emulator is set to terminator"
        fi
      fi
    else
      # Create the helpers.rc file and add the TerminalEmulator line
      echo "$terminal_line" > "$helpers_file"
      echo -e "\n  $blueplus default terminal emulator is set to terminator"
    fi
    }

add_terminator_config() { 
    # Check if Terminator is installed
    if ! command -v terminator &> /dev/null; then
        echo -e "terminator is not installed"
        exit 1
    fi

    echo -e "\n  $greenplus adding terminator config file"

    if ! [ -d "/home/$CURRENT_USER/.config/terminator/" ]; then
        mkdir -p /home/$CURRENT_USER/.config/terminator/
    fi

    cp $CURRENT_LOCATION/config-files/terminator-config /home/$CURRENT_USER/.config/terminator/config
    chown -R kali /home/$CURRENT_USER/.config/terminator/
    echo -e "\n  $blueplus added terminator config file in /home/$CURRENT_USER/.config/terminator/config"
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
    echo -e "\n  $blueplus restart the machine for all the changes to take place"
    echo -e "\n  $blueplus bye!"
    }

check_for_root
show_system_info
line
sleep 1
echo -e "\n  $blueplus updating machine"
apt_update
apt_upgrade
apt_autoremove
line
change_keyboard_shortcuts
line
sleep 1
add_user_to_vboxsf
line
sleep 1
# install_sublime_text
# sleep 1
# line
install_terminator
line
sleep 1
set_terminator_to_default
line
sleep 1
add_terminator_config
line
sleep 1
install_mongodb
line
sleep 1
bye_bye
line
