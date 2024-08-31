### What is NAT?

NAT(Network Address Translation) - is a technology that is used to change network addresses in data packets sent through a router.
The main function of NAT is to convert private IP addresses used in a local area network (LAN) into public IP addresses 
that can be used in a global network (Internet).

### Why do we need NAT?

1. IP Address Preservation:  NAT allows multiple devices to use the same public IP address to access the Internet. 
This significantly reduces the number of public IP addresses needed to service a large network.

2. Increased Security: NAT also acts as a kind of firewall. Since internal IP addresses are hidden from the outside world,
 it makes it difficult for unauthorized people to access devices on the private network.

3. Simplifying network management: NAT greatly simplifies the management of internal networks due to the fact that internal IP addressing and external public IP addresses can be independent of each other.

### How NAT works?

NAT works by replacing private IP addresses with public ones when passing packets through a router:

- Outgoing traffic: When a device on a local network (such as a computer) sends a data packet to the Internet, that packet has an internal (private) IP address and port.
A router with NAT replaces that IP address and port with a public IP address and a new, unique port. These changes are written to the NAT translation table.
When the packet reaches the destination server, the server sees it as coming from the public IP address.

- Incoming traffic: When the server sends a response packet back, it is directed to a public IP address with a specific port.
The router matches that port with an entry in the NAT translation table and forwards the packet to the corresponding internal IP address and port on the local network.

### Types of NAT

- Static NAT: One internal IP address is mapped to one external IP address. This is used when a permanent mapping is required, such as for a server that must be accessible from the Internet at a specific address.

- Dynamic NAT: allows multiple devices on a local network to use one or more public IP addresses from a pre-defined pool.
  1. Address assignment: When a device on the local network initiates a connection to the external network, NAT on the router selects one of the available public IP addresses from the pool and temporarily assigns it to the device's internal IP address.
  2. Translation Table: The router maintains a mapping between the internal IP address and its assigned external IP address in the NAT translation table.
  3. Address Release: Once a session is completed (e.g. the connection to a website is closed), the external IP address is released and returned to the pool for use by other devices. If all IP addresses in the pool are occupied, the new device will have to wait until one becomes available.

- PAT(Port Address Translation): This is a more advanced version of NAT that allows multiple devices on a local network to use a single public IP address at the same time. Instead of assigning each device a separate IP address, PAT uses unique ports for each connection, allowing multiple devices to share the same public IP address.
  1.  One public IP address: Unlike Dynamic NAT, which uses a pool of public IP addresses, PAT uses only one IP address for all devices on the network.
  2.  Using ports: When a device initiates a connection, the router changes not only the internal IP address, but also the port number (usually 1024 and up). For example, an internal device with an IP address of 192.168.1.10 might initiate a connection to port 56789.
     The router replaces the internal IP address with a public one and may change the port number to something else, say 1025. This new port is unique to the current connection.
  3. Translation Table: The router stores the mapping of the internal IP address and port to the public IP address and changed port in the translation table.
  4. Multiple Connections: Since port numbers can vary, the same device can establish multiple connections at the same time (such as opening multiple browser tabs), and each data stream will have its own unique port mapping.

### Where is NAT used?

- Home networks: NAT is widely used in home routers, where all devices in the house (computers, smartphones, TVs, etc.) connect to the Internet through one public IP address.
- Corporate Networks: In office networks, NAT allows multiple employees to use the Internet through one or more public IP addresses. This reduces the need to purchase additional public addresses.
- Cloud services and data centers: In virtualized environments, NAT is used to control access and distinguish between virtual machines and the outside world.
  1. Internal and external IP addresses: In cloud environments, each virtual machine receives a private IP address for communication within the virtual network (VPC - Virtual Private Cloud). When the virtual machine needs to communicate with the Internet or external networks, NAT translates its private IP address into a public one.
  2. NAT types in cloud services:
     - NAT Gateway: This is a managed cloud service that automatically performs address translation for large numbers of virtual machines, providing them with secure and scalable access to the Internet.
     - SNAT (Source NAT): This technology changes the source IP address of packets so that virtual machines can initiate connections to the Internet, hiding their internal IP addresses.
     - DNAT (Destination NAT): In this case, NAT changes the destination IP address of incoming packets, directing them to the desired virtual machines or services, which allows you to control access from the outside.
  3. Examples of use:
     - Public and private subnets: Cloud environments typically create public and private subnets. Virtual machines in private subnets can only access the Internet through a NAT Gateway, which ensures their security since they do not have a direct public IP address.
     - Web services: For example, web servers running on virtual machines can use NAT to restrict access to them only through certain ports (e.g. 80 for HTTP and 443 for HTTPS), providing security and access control.
     - Load Balancing: NAT is used in combination with load balancers to distribute incoming traffic across multiple virtual machines, improving service availability and fault tolerance.
- Mobile networks: In cellular networks, NAT is used to simplify the management of large numbers of mobile devices connected to the Internet through a limited number of public IP addresses.

### Conclusion

Thus, NAT is an important tool in modern network administration, providing IP address savings, security and flexibility when working with network resources.
