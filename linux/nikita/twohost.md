#How to Establish TCP connection between 2 Linux hosts and transfer data through it.
>In this task im created 2 virtual machines which is based on 2 different unix systems, ubuntu and kali.
---
## Step 1(Virtual box configuration)
- Open **Virtual Box** -> **Settings** -> **Network settings** -> **Enable (Adapter 2)**
>For adapter 1 (Enable Host-only Adapter), for adapter 2 (Enable Nat).
>It help for you to create other virtual network, to connect 2 differnt systems.
---
## Step 2(Virtuals machines configuration)

>**Note**
>The next step we will need to configure, both virtual machines to connect each other.
>The ways to do it is differnt for both machines, so im gonna separete this step for kali and ubuntu softwares.
### Kali linux
- ```service ssh start```
>Will start the OpenBSD Secure Shell server.
- ```serivce ssh status```
>Will check the status, if its Active then its ready to connect.
### Ubuntu
- ```service ssh status```
>If the server not install in your ubuntu system then use that command to install it ```sudo apt-get install openssh-server```
>Then after running this command it whill install it, and run it.
---
## Step 3(Connect both machines)
>**Note**
>This server is opening port 22, it will changing his status to **Listening**.
- Now i will connect kali linux, to ubuntu.
```ssh vboxuser@192.168.56.102```
>**Note**
>You need in this command type name of user in the system where you want to connect(For me its vboxuser)
>The ip addres of the system where you connecting(For me its 192.168.56.102)
>After that type the password of this user.
When you will see that your user and system changed, thats mean youre succesfully connected to other system.
```uname -a```
>Give you detailed overview of the system where you are.
---
## Step 4(Transfer data)
```scp [filename] [username@IPAddress:path]```
- There you need to writte file name which you want to trasnsfer. ```scp <nikita.txt>```
- There you need to overwritte where you want to transfer this file, ```<kolega@192.168.56.103:~/Downloads>```
- Done data is transfered with output, how many data is transfered.
>To exit of connection type ```exit```
---
Good job you know how to transfer data throw the ssh, with using TCP protocol.


![alt text](http://picsum.photos/200/200)

