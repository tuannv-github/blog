Buildroot
=========

* Linux Kernel: bzImage
* Rootfs: rootfs.ext2

.. code-block:: 

    make menuconfig
    make linux-menuconfig

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
