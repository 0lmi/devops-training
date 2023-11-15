#!/bin/bash
#Correct script

ipnmask=$(ip addr | sed '1,7d' | grep -w 'inet' |  awk '{print $2}')

host_find() {
	nmap -sn -v $ipnmask | sed 's/[()]//g' | grep -v down | awk '/Nmap scan report/ {ip=$NF} /Host is up/ {latency=$(NF-1); print ip, latency}'
}

host_find



