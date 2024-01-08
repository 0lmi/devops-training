#!/bin/bash

command=/usr/bin/nmap
ipnmask=$(ip addr | sed '1,7d' | grep -w 'inet' |  awk '{print $2}')

choose_fun() {
    echo "Bad news script cannot be completed, you want to install nmap command?"
    read -p "Yes/No:" answer
    if [ $answer = "No" ]; then
        echo "This script will be closed"
        exit
    elif [ $answer = "Yes" ]; then
        echo "I'm installing nmap now"
        version_fun
        echo "Congratulation nmap command is installed"
        host_find_fun
    fi
}

host_find_fun() {
    nmap -sn -v $ipnmask | sed 's/[()]//g' | grep -v down | \
        awk '/Nmap scan report/ {ip=$NF} /Host is up/ {latency=$(NF-1); print ip, latency}'
}

version_fun() {
    sudo apt install -y nmap > /dev/null 2>/dev/null
    if [ $? == 1 ]; then
        echo "Unexpected problem your based version is not suppost to download nmap command, please do it manually"
        exit
    fi
}

if [ -f $command ]; then
    host_find_fun
else
    choose_fun
fi

