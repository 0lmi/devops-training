# Establish TCP connection between 2 Linux hosts and transfer data through it.

---

## Step 1. Creating arbitrage socket.

Sockets are Linux file descriptors that serve as the communication end-points for processes running on that device.
Each Linux socket consists of the device's **IP address** and a selected **port number**.
```sudo nc -l <port numer>```

For me its ```sudo nc -l <555>```

---

## Step 2. Establish connection between 2 hosts.
 
Other host need to be connected with the host name.
```hostname```

For the data transfer we need to connect both hosts.
```sudo nc [your host name] [your created port]```

For me its ```sudo nc ubuntu20 555```

---

## Step 3. Data transfer

Choose which host will be reciever and sender.

**Host Reciever**
Select the file path where you want to recieve file, use ```pwd```
```sudo nc -l [port] > [file to recieve]```

For me its ```sudo nc -l 555 > test.txt```

**Host Sender**
Select the folder path, where is your file located.
```sudo nc [your host name] [port] < [file to send]```

For me its ```sudo nc ubuntu20 555 < test.txt```

