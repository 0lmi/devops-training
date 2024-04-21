# Make an empty directory and check it’s size, explain why does empty directory has size and why is it exactly like this.

## Describe:

An ext4 file system is split into a series of block groups.
Block size can be edited manually, for needable requirments of stored data.
By default 1 block size to hold data inside of it 4096 bytes(4KB).
In block space include indoes - index data, needable to store metadata(Permissions, file type, size).

## Practice:

Command to create an empty directory is `mkdir`.
After entering the directory `ls -ld`, it shows empty folder size in bytes(4096 bytes = 4KB).

## Answer:

The size 4096 bytes is the starting storage, which are needable to store metadata of the files inside of currect directory(Including filenames).
The starting store is equal the blocks size.
