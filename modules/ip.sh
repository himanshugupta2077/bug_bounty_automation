#!/bin/bash

domain=$1

ping -c 4 domain

dig domain

traceroute domain

nslookup domain

whois domain