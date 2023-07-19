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

line() {
    echo -e "\n---------------------------------------------------------------------------------------------"
    }

# echo -e "\n$greenplus checking database status "
# check...
# if not started 

echo -e "\n$greenplus starting database "
sudo service mongodb start
echo -e "\n$greenplus installing pymongo "
python -m pip install pymongo

# echo -e "\n$greenplus creating database user 'ronin' "

# echo -e "\n$greenplus creating database 'ronindb' "


# node server/server.js &
# cd client
# npm run start