=========
Buildroot
=========

Buildroot is a simple, efficient and easy-to-use tool to generate embedded Linux systems through cross-compilation.

* Linux Kernel: bzImage
* Rootfs: rootfs.ext2

.. code-block:: 

    make menuconfig
    make busybox-menuconfig 
    make linux-menuconfig

BusyBox
=======

BusyBox **combines tiny versions of many common UNIX utilities into a single small executable**. It provides replacements for most of the utilities you usually find in GNU fileutils, shellutils, etc. 

The utilities in BusyBox generally have fewer options than their full-featured GNU cousins; however, the options that are included provide the expected functionality and behave very much like their GNU counterparts.

BusyBox provides a fairly complete environment for any small or embedded system.

.. code-block:: 

    make menuconfig
    make

Buildroot using QEMU
====================

.. code-block:: bash

    qemu-system-x86_64 \
        -M pc \
        -kernel ./output/images/bzImage \
        -drive file=./output/images/rootfs.ext2,if=virtio,format=raw \
        -append "root=/dev/vda console=ttyS0" \
        -net nic,model=virtio -net user \
        -nographic

    qemu-system-i386 \
        -M pc \
        -kernel ./output/images/bzImage \
        -drive file=./output/images/rootfs.ext2,if=virtio,format=raw \
        -append "root=/dev/vda console=ttyS0" \
        -net nic,model=virtio -net user \
        -nographic
