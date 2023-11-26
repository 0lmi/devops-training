#Make an empty directory and check it’s size, explain why does empty directory has size and why is it exactly like this
I will try to overview for you all the needable tools and information, for better understanding about linux directory.
---

### 1. Directory

A directory, also known as a folder, is a container used to organize files on a computer's file system.
Also usable thinks when you making directory.
- Navigation - Simply allows you to find needable files.
- Group - Sorting the files by groups/categorys.
- Path - Finding the folder with the uniq **path**, like `/usr/bin/bash`
>Its only most populars parts of the folder but its enough for now to understand why did empty directory have size
To make the empty directory you can use simple command
```
mkdir your_directory_example
```
---

### 2. Empty space which still have size

Firs i will show for you needable commands to check directory sizes.
| Check disk space usage | List the directory content | Ckeck directory path |
| --- | --- | ---|
| `du -sh` | `ls -la` | `pwd` |

When you creating an empty directory it size will be **4096 bytes**
> In other different file systems empty folder size is different.
After creating a new directory it still using a disk space, in mostly its a little space.
As it mainly includes metadata such as the directory entry itself and information about the names and numbers of the files.
The actual file data is not stored in the directory itself but in the inodes associated with the files.
>Now i will show you example which indformation cost the space for the disk.(Ubuntu)
1. (Check disk space usage) it show that folder still have the size 4K, thats mean 4000 bytes `linux not showing the decimal, hundredths, thousandths parts`. 
2. (List the directory content) There you can see 2 dots **. ..**, it the links of the files. It shows for use that directory is really not that empty, it still have link for it self.
3. (Check directory path) And the path for the file where directory is located.

---

Thank you for reading my empty folder overview.
![alt text](http://picsum.photos/200/200)
