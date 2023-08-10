#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <domain>"
    exit 1
fi

domain="$1"

echo "Pinging $domain:"
ping -c 4 "$domain"

echo "Digging $domain:"
dig +short "$domain"

echo "Traceroute to $domain:"
traceroute "$domain"

echo "Nslookup for $domain:"
nslookup "$domain"

echo "Whois information for $domain:"
whois "$domain"
