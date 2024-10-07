Task: Know, understand what NAT is, why it is needed, what is the principle of operation, where it is used
___

# NAT (Network Address Translation)
NAT - is a mechanism in TCP/IP networks that allows the IP address to be changed in the header of a packet passing through a traffic r
outing device.

## Problems solved by NAT

1. Allows you to save IP addresses (only when using NAT in PAT mode) by translating multiple internal IP addresses to one external public IP address (or multiple, but still fewer than internal).
2. Allows you to prevent or limit traffic from the outside to internal hosts, while allowing traffic from the inside to the outside. When a connection is initiated from within the network, a broadcast is created. Corresponding packets coming in from the outside match the created broadcast and are therefore passed through. If there is no corresponding broadcast for packets coming from the outside (and it can be created at connection initiation or static), they are not passed.
3. Allows you to hide individual internal services of internal hosts/servers. Basically, the same, above, translation to the specified port is performed, but you can replace the internal port of the officially registered service (for example, the 80th TCP port (HTTP server) with the external 54055). Thus, externally, on the external IP address, after broadcasting the address on the site (or forum), for familiar visitors, it will be possible to get to the address http://example.org:54055, but on the internal server, which is through NAT, it will work on the usual 80th port. Increasing security and preservation of "non-public" resources.

## NAT types
There are 3 basic concepts of address translation: static (**Static Network Address Translation**), dynamic (**Dynamic Address Translation**), overloaded (**NAPT, NAT Overload, PAT**).

**Static NAT** - Mapping an unregistered IP address to a registered IP address on a one-to-one basis. Especially useful when the device needs to be accessible outside the network.

**Dynamic NAT** - Maps an unregistered IP address to a registered address from a pool of registered IP addresses. Dynamic NAT also establishes a direct mapping between unregistered and registered addresses, but the mapping may change depending on which registered address is available in the address stack during communication.

**Overloaded NAT** (**NAPT, NAT Overload, PAT, masquerading**) is a form of dynamic NAT that converts multiple unregistered addresses into a single registered IP address using a variety of ports. Also known as PAT (**Port Address Translation**). During congestion, every computer on the private network broadcasts to the same address, but with a different port number.
___

### Useful links: ###
1. https://www.checkpoint.com/cyber-hub/network-security/what-is-network-address-translation-nat/
2. https://www.youtube.com/watch?v=L1JtmAiSaFQ&ab_channel=AndreySozykin
3. https://www.youtube.com/watch?v=B3LViQ_184Q&ab_channel=NajQazi
4. https://www.youtube.com/watch?v=hFGXq66mcqM&ab_channel=CloudLearners







