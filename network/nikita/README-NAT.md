# NAT (Network Address Translation)
Task: Know, understand what NAT is, why it is needed, what is the principle of operation, where it is used

---

## Overview of NAT

To understand *NAT*, first we need to take in mind which problems caused to create this method of mapping.
For global data transfer throw network from machine **HOST 1** to machine **HOST 2**, both host should have IP address.
IPv4 gives total number of possible addresses 4,3 billion, this is large number but isn't enough to give uniq address for each machine.
This problem solution gives to seperate network to **LAN** and **WAN**.

**LAN (Local Area Network)**
Using private IP address 
A network that covers a small geographic area, such as a single building, home, or campus.
It's private and used for internal communication among devices.

**WAN (Wide Area Network)**
Using public IP address
A network that spans a large geographic area, often connecting multiple LANs across cities, countries, or even continents.
The internet is the largest example of a WAN, as it connects millions of smaller networks worldwide.

## In summary

NAT is a technicque used in networking to translate private IP address into a public IP address, thats allowing multiple devices in LAN to access the internet using one public IP.
Information with source Ip address and destination IP address is located in package, this package travels to router for NAT translation.
NAT is usually implemented in router or firewall.

Best practice to configure NAT on linux operation system is using `iptables` command, used to set up, maintain, and inspect the tables of IP packet filter rules in the Linux kernel.

---

## Types of NAT

### Static NAT

Static NAT maps network traffic from a static external IP address to an internal IP address or network.
It creates a static translation of real addresses to mapped addresses.
Static NAT provides internet connectivity to networking devices through a private LAN with an unregistered private IP address. 

### Dynamic NAT

Dynamic NAT avoids IP address conflicts by maintaining a state table that records five values (source address, source port, destination address, destination port, and protocol) for each TCP or UDP connection.

## Overview of PAT

PAT (Port Address Translation) - allows many devices on the LAN to share only 1 public IP address (or few, with dynamic PAT), by translating the private IP address and port number.
Being sure that all packets are routed correctly.

- PAT distinguishes between different internal devices by mapping each device's private IP address to a unique port number.

- When packet was sent to WAN, PAT translate **Private IP address** and **Port** to public IP address and a new unic PORT.
For example when Host trying to reach remote server by HTTP protocol:
196.168.6.4:42441 -> 10.0.4.5:80

- When the internal device initiates outgoing connections to the internet or external services, 
Static PAT can map these connections to the correct external ports (like 443, 80, or 1443)

### Static PAT

- Is permantly mapped to a single Public IP and olny retranslate the Port number.
 
### Dynamic PAT

- In dynamic PAT, the network can have multiple public IP addresses available.

- Every of outgoing connection can be retranslated to different public IP and Port number.

---

## Benefits of NAT

- Cost saving
- Network security 
- Load balanced

## Useful service from AWS

*NAT gateways* - A NAT gateway is a Network Address Translation (NAT) service.
You can use a NAT gateway so that instances in a private subnet can connect to services outside your VPC but external services cannot initiate a connection with those instances.

When creating a NAT gateway you can specify the connection type **Public** or **Private**

*Public* - (Default) Instances in private subnets can connect to the internet through a public NAT gateway, but cannot receive unsolicited inbound connections from the internet.

*Private* - Instances in private subnets can connect to other VPCs or your on-premises network through a private NAT gateway.
You can route traffic from the NAT gateway through a transit gateway or a virtual private gateway.

# Conclusion

Nat is really powerful technicue of translating Ip addresses and Port, taking huge role in global network traffic.
