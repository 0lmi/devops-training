#!/bin/bash

#In start my script need to make sure that you have instaled tools in linux
command=/usr/bin/nmap
if [ -f $command ]
then
	echo "Great, your pc is configured to run Host-Scanning-Script"
		sleep 2
			clear
else
choose_fun() {
	echo "Bad news script cannot be completed, you want to install nmap command?"
	read -p "Yes/No:" answer
		if [ $answer = "No" ]; then
		echo "This script will be closed"
		exit
		elif [ $answer = "Yes" ]; then
		echo "I'm installing nmap now."
		sudo apt install -y nmap
		clear
		echo "Congratulation nmap command is installed"
		sleep 3
		clear
fi
}
choose_fun
fi

#Variable which taking ip-address and net_mask
ipnmask=$(ip addr | sed '1,7d' | grep -w 'inet' |  awk '{print $2}')

#Function which scanning your local network for avaible hosts, and returning clear output with ip-addres and latency
host_find() {
        nmap -sn -v $ipnmask | sed 's/[()]//g' | grep -v down | awk '/Nmap scan report/ {ip=$NF} /Host is up/ {latency=$(NF-1); print ip, latency}'
}

host_find
