#!/bin/bash

#
#Task: to make a script that can scan a local network with no adaptation 
#	and changing to different networks
#
#Bug:
#	1)Doesn't work if you have more than one network interface
#

function check_ip {
	ifconfig | grep "broadcast" | awk '{print $2}'
}

function check_netmask {
	ifconfig | grep "broadcast" | awk '{print $4}'
}

function netmask_prefix {
	local ip=$1
	local netmask=$2
	ipcalc -nb $ip $netmask | grep "Netmask" | awk '{print $4}'
}

function scan_network {
	local ip=$1
	local netmask_prefix=$2
	nmap -sn -n -v $ip/$netmask_prefix | grep -v "host down" | sed "1,4d" | grep -v "Nmap done" | awk '/Nmap scan report for/ { ip=$5 } /Host is up/ { latency=$4 ; print ip" " latency ")"}'
}

ip=$(check_ip)
netmask=$(check_netmask)
netmask_prefix=$(netmask_prefix $ip $netmask)

scan_network $ip $netmask_prefix
