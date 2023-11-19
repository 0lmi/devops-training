# directory size task

#### Task:
To make a new directory and check it's size. Explain why does empty directory has a size.

---

After making an empty directory we noticed that it's size is 4096 bytes.    
The 4096 bytes size for directories is often chosen, because it aligns with the block size of the file system. File systems are typically divided into fixed-size blocks, and the directory structure is designed to be efficient in terms of block allocation.
This means that even if directory contains only few entries, it still occupies en entire block, which is usually 4096 bytes in size. This simplifies file system managment and reduce fragmentation.
If you want to find the real storage of directory, you can use command `du` which stands for 'disk usage'

### To sum up:
That's the size of space on the disk that is used to store the meta-information[^1] for the directory, not what it contains.

[For more info you can check this](https://linuxize.com/post/how-get-size-of-fle-directory-linux/)
 
[^1]:Metainformation is a data that provides information about other data.  
