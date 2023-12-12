# folder-size task

#### Task: ####
Can the folder size be larger than the empty folder size? What does it depend on?
---
As we have seen in [Directory-size task](README-directory-size.md), the normal size of directory is 4096 bytes, because it aligns with the block size of file system. So basically this 4096 bytes contain meta-informain.

#### Directory's Meta information  ####
Directory's meta data innehold information about it's name, permissions, owner, catalog etc.

But what if I make 100 000 empty files inside of it.

```
for (( i=1; i<133700; i++ )); do touch long_long_looong_man_sakeru_$i ; done

```

Size of our folder is already 8.376.320 bytes which use 8M on the disk.

#### And that's why: ####

- Catalog entry size
Every file in folder has a corresponding entry in catalog(name of the file, inode, type of the file)
The size of this entry depends on the file system, but it's typically a few bytes. If you have many files, each has it's own entry, the total size of catalog entries can become significant
- File system block alignment
File systems typically align data into blocks. If the file system block size smaller then catalog entry size, even empty files can occupy an entire block.
- Using Indexes and File System Data Structure
As the number of files increases, the file system can use indexes and other data structures to efficently locate and manage files. These additional structures can also increase the overall folfer size.

### Answe ###
Yes, folder size of non-empty folder can be larger than the empty folder's size, and it depends on amount of files folder innehold and the name of these files. 
