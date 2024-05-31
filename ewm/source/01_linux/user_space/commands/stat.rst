====
stat
====

* **atime** access time
* **mtime** modify time
* **ctime** change time

atime
=====
When was the last time the file was accessed?

**Accessing** means using cat, vim, less, or some other tool to read or display the content of the file.

mtime
=====
When was the last time the file was modified?

**Modifying** means the contents of a file were changed by editing the file.

ctime
=====
When was the last time the property and metadata of the file were changed?

The **metadata** includes file permissions, ownership, name, and location of the file.

.. code-block:: bash

    $ stat TEST 
    File: TEST
    Size: 27              Blocks: 8          IO Block: 4096   regular file
    Device: 812h/2066d      Inode: 9831860     Links: 1
    Access: (0664/-rw-rw-r--)  Uid: ( 1002/tuannv109)   Gid: ( 1002/tuannv109)
    Access: 2023-08-02 01:26:42.237577846 +0000
    Modify: 2023-07-26 04:28:19.767628499 +0000
    Change: 2023-07-26 04:28:19.767628499 +0000
    Birth: 2023-07-26 04:27:56.643769003 +0000
