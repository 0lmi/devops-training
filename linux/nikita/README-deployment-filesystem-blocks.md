# Characters space usage in text file
The task is how many bytes of disk space took file which contain 5000 characters.
(OS: Linux, filesystem: ext4, encoding: UTF8).

---

# UTF-8 Describe
UTF-8 is a any line of characters encoding system, which can encode any characters of different languages.
UTF-8 is based on 8 bit code unit, where each character is 1-4 bytes(1-2 bytes most usable).

---

### System
1. File system : *ext4*
2. OS : *Linux*
3. Encoding : *UTF-8*

### Characters
1. *5000 Characters*
2. *English language*

Usually used english characters - *1byte*
Thats mean file with 5000 characters will be - *5000bytes*

---

# Explanation:
In ext4 filesystem data is storing by blocks, 1 block is equal 4096 bytes.
Block already sepperated by units, 1 unit equal 1024 bytes, 4 units equal 1 block.
Two different files cannot store the data in the same block.
 
---

### Answer:

File which contain 5000 characters of UTF-8 encoding on ext4 filesystem, gonna took 5000 bytes of disk size.
We need 2 blocks for lacate our file, 8192 bytes of disk space will took this file.
