#!/bin/bash

ipnmask=$(ip addr | grep -w inet | awk '/brd/{print $2}')
nmap -sn $ipnmask | sed 's/[()]//g' | awk '/Nmap scan report/{host=$NF} /Host is up/{time=$(NF-1)} END{print host, time}'
