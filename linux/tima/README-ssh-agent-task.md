# ssh-key task

#### Task:
To make an SSH key with a passphrase and launch ssh-agent, add a key to ssh-
agent. Clone private repository by using ssh-agent[^1]
--- 
#### Step 1:
We have to start with making an ssh-key   
```
ssh-keygen -t ed25519[^2] -C "[your email addresse]"
```
Then we have to copy **public** key from `~/.shh/id_ed25519.pub`[^2] and add i
t to your git user in settings by going to git   
```
Settings >> SSH and GPS keys >> New SSH key
```

---

#### Step 2:
The next step after we got a key and saved it in our git, is to launch a ssh-agnet   
```
eval $(ssh-agent)
```
Now we launched ssh-agent and it returned us a PID[^3], we can check if the process take place    
```
ps aux | grep [PID we got]
```
Afterwards, if the ssh-agent is working, we have to add our **private** key in there   
```
ssh-add ~/.ssh/[name of file for private key]
```
Then we pass our passphrase to ssh-agent.

---

#### Step 3:
Now it's time to clone repository from git, we copy the link to the repository and use git clone      
```
git clone git@github.com:user/repository.git
```
	 
[^1]: Meant to use ssh-agent instead of entering passphrase
[^2]: I used ed25519 because this key is more secure and shorter that rsa
[^3]: Process ID
