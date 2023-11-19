# tcp connection task

### Task:
To establish TCP connection between two computers in local network and send a file through it.

---

In order to create a TCP connection between two computers in local network and send a file, one of them is going to have a role of client, and another is going to have a role of server.

---

##### Client
First of all we have to create a socket, I use **netcat** utility
```
sudo nc -l [port] > [file we are expecting to get]
```
For port you can basically use any number you want
---

##### Server
As a server tou have to connect to this soccet by using the same **netcat** utility
```
sudo nc [hostname] [port you created] < [file they're expecting to get]
```
You have to write your hostname in order to connect to created soccet, use command `hostname` to check your hostname

---

[You can check this video for better understanding](www.youtube.com/watch?v=L_WkKRaUudY)
