#!/bin/bash

ipnmask=$(ip addr | grep enp0s | grep -w inet | awk '/inet/{print $2}')

host_find() {
	nmap -sn -v $ipnmask | sed 's/[()]//g' | grep -v down | awk '/Nmap scan report/ {ip=$NF} /Host is up/ {latency=$(NF-1); print ip, latency}'
}

host_find



