# This is how i confirm the task with the ssh keys, and ssh-agent
All of this steps are provided to make in UNIX based system
And not able to work with MAC and WINDOWS os

### 1. Create the ssh key, give for this key ** passprashe **
```
ssh-keygen -t ed25519 -C "example@linux.eu"
```
- Open public key in .ssh directory
```
cd /home/your_username/.ssh/
```
> id_ed25519.pub > copy the text inside

- Add the public key in web site github.
[Git hub link where to paste the ssh-key](https://github.com/settings/keys)

### 2. Enable ssh agent
** Use root to do it **
- You need to start the ssh-agent on the background
```
** Note **
The ssh-agent will save in your ram memory, thats mean when you restart your PC should to do this step again
```
```
eval "$(ssh-agent -s")
```
- After that insert your *ssh-key* in *ssh-agent*
```
ssh-add ~/.ssh/id_ed25519
```
- In the last step it will ask for you to create a *passphrase*, for your own security make it ** strong ** not ~~ simple ~~
```
** NOTE **
Better to not save the passphrase in any of the .txt files or the paper list. Form it on other device like usb-flash. That provide to you full security of your data.  
```

### 3. Cheack if the ssh-agent running correctly 
- This step i will mark with *. By running this script you can check the ssh-agent activity and if you made everythink completly it will show that ssh-agent is running.
```
!#/bin/bash

if [ $(ps ax | grep [s]sh-agent | wc -l) -gt 0 ] ; then
    echo "ssh-agent is already running"
else
    eval $(ssh-agent -s)
    if [ "$(ssh-add -l)" == "The agent has no identities." ] ; then
        ssh-add ~/.ssh/id_rsa
    fi
    # Don't leave extra agents around: kill it on exit. You may not want this part.
    trap "ssh-agent -k" exit.
fi
```

# Good job ssh-key is saved in your ssh-agent
Now your development work such be a little easier
![alt text](http://picsum.photos/200/200)
