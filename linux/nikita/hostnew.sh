#!/bin/bash

ip=$(ip addr | grep -w inet | awk '/brd/{print $2}')
nmap -sn $ip | awk '/Nmap scan report/{host=$NF} /Host is up/{time=$(NF-1)} END{print host, time}' 
