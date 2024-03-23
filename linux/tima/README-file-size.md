# file-size task

#### Task:
How many bytes on the disk does a text file of 5000 letters take up(OS: Linux, filesystem: ext4, encoding: utf-8)

---
#### Important note
To determine the disk space required for a text file, you need to consider not only the number of characters, but also other factors such as encoding and file system block size. For instance in utf-8, 1 russian symbol uses 2 bytes, when english uses 1 byte. Therefore, estimated values are used that give a general idea of the size of the files on the disk. And I use only Russian and English symbols for comparison.
---
### UTF-8
5000 letters in Russian (utf-8 encoding):

- Average size of Russian letter in utf-8 is approx. 2 bytes
- 5000 letters * 2 bytes = 10 000 bytes

So approx. size of file in Russian with utf-8 encoding takes arounf 10 000 bytes on disk.

5000 letter in English (utf-8 encoding):

- Average size of English letter in utf-8 is approx. 1 byte
- 5000 letters * 1 byte = 5000 bytes

Approx. size of file in English with utf-8 encoding takes around 5000 bytes on disk.

### OS: Linux and filesystem: etx4

In general a file size in same language and using same encodings, will take up approxuimately the same amount of disk space regardless of system, as long as the same file system is used. However, there may be difference in file system implementations or optimizations for individial systems that could affect the exact size on disk.

So, if you create a file with the same text on Linux with an ext4 file system adn then copy that file to another system with the same file system, the file size on disk will likely be similar. 
