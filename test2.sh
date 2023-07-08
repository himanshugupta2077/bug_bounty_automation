#!/bin/bash

install_by_downloading_deb() {

	APPLICATION_NAME="tomato"
	INSTALLATION_FILE_NAME=""
	INSTALLATION_FILE_DOWNLOAD_LINK=""

    echo -e "\n  $greenplus installing $APPLICATION_NAME \n"
    if dpkg -s "$APPLICATION_NAME" >/dev/null 2>&1; then
        echo "$APPLICATION_NAME already installed"
    else
        echo "$APPLICATION_NAME is not installed"
        echo "installing $APPLICATION_NAME"

        if [ -e "$INSTALLATION_FILE_NAME" ]; then
            eval sudo dpkg -i $INSTALLATION_FILE_NAME    
        else
            eval wget $INSTALLATION_FILE_DOWNLOAD_LINK    
            eval sudo dpkg -i $INSTALLATION_FILE_NAME
        fi

        if dpkg -s "$APPLICATION_NAME" >/dev/null 2>&1; then
            echo "$APPLICATION_NAME installed"
        else 
            echo unable to install $APPLICATION_NAME
            exit
        fi
    fi
    }

install_with_apt() {

	APPLICATION_NAME="terminator"

    echo -e "\n  $greenplus installing $APPLICATION_NAME \n"
    if dpkg -s "$APPLICATION_NAME" >/dev/null 2>&1; then
        echo "$APPLICATION_NAME already installed"
    else
        echo "$APPLICATION_NAME is not installed"
        echo "installing $APPLICATION_NAME\n"

        eval apt install $APPLICATION_NAME -y

        if dpkg -s "$APPLICATION_NAME" >/dev/null 2>&1; then
            echo "\n$APPLICATION_NAME installed"
        else 
            echo unable to install $APPLICATION_NAME
            exit
        fi
    fi
    }

