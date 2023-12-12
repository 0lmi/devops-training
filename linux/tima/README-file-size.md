# File-size task #

#### Task: ####
How many bytes on the disk does a text file of 5000 letters take up(OS: Linux, filesystem: ext4, encoding: utf-8)

---

#### Note: ####
We are going to check two files, one with 5000 of Russian symbols and another with English for comparison. With some another languages or use of special symbols can lead to different totals, as well as using another filesystem(different block size, metadata overhead, allocations, fragmentation, etc) or OS(vary filesystem implementation, filesystem configuration, matadata handling, etc.)

---

##### Russian symbols #####i

5000 Russian letters in etf-8:
- Size of Russian letter in utf-8 is 2 bytes
- 5000 * 2 = 10 000 bytes

We can check apparent size with `du --apparent-size`
```
du --apparent-size --block-size=1 your_file.txt
```
The output is approx 10 000 bytes, I got 9985 bytes(may be different due to metadata overhead, block allocation, or others filesystem related factors)

Then, we can check size on the disk using
```
du -h your_file.txt
```
Som when you observe a text file with 5000 Russian symbols, it's size on the disk is 12KB which is 12 228 bytes. Where 9985 bytes are actual size and 2243 bytes are and Overhead[^1].

##### English symbols  #####

5000 English symbols in utf-8:
- an English symbol in utf-8 takes 1 byte
- 5000 * 1 = 5000 bytes

By checking it's apparent size, it shows 5000 bytes
By checking it's size on the disk, output is 8KB

8KB is 8192 bytes, where 5000 bytes are the actual file content, and 3192 bytes are taken for Overhead.

---

In general a file size in same language and using same encodings, will take up approxuimately the same amount of disk space regardless of system, as long as the same file system is used. However, there may be difference in file system implementations or optimizations for individial systems that could affect the exact size on disk.

---
[^1]: The ext4 filesystem allocate space in blocks. Even if your file is smaller than the block size, it will occupy a full block. The ramaining space in that block that is not used by the actual file content contributes to the overhead.
