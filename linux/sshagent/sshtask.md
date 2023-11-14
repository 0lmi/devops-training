# This is how i confirm the task with the ssh keys, and ssh-agent

### 1. Create the ssh key, give for this key passprashe( ssh-keygen -t ed25519 -C "nikita@linux.eu" ) 
#### 1.1 Open public key in .ssh directory
#### 1.2 Add the public key in web site github, setting->add ssh key

### 2. Enable ssh agent
Use root to do it
#### 2.1 Use the eval "$(ssh-agen -s)"
#### 2.2 ssh-add ~/.ssh/id_ed25519
#### 2.3 Enter passphrase

### 3. Cheack the ssh-agen status

#### 3.1 Script for it

```
  GNU nano 6.2                                                                                      agent.sh                                                                                                
if [ $(ps ax | grep [s]sh-agent | wc -l) -gt 0 ] ; then
    echo "ssh-agent is already running"
else
    eval $(ssh-agent -s)
    if [ "$(ssh-add -l)" == "The agent has no identities." ] ; then
        ssh-add ~/.ssh/id_rsa
    fi
    # Don't leave extra agents around: kill it on exit. You may not want this part.
    trap "ssh-agent -k" exit
fi
```

### 4. git clone "Your needable repository"

All steps will provide to save the ssh-key in ssh-agent and not ask for passphraze.
