Physical Memory
===============

x86_64 Machine
--------------

.. code-block:: bash

    # sudo cat /proc/iomem                    
    [sudo] password for tuannv: 
    00000000-00000fff : Reserved
    00001000-0009ffff : System RAM
    000a0000-000fffff : Reserved
    00000000-00000000 : PCI Bus 0000:00
    000a0000-000dffff : PCI Bus 0000:00
    000f0000-000fffff : System ROM
    00100000-09bfefff : System RAM
    09bff000-0a000fff : Reserved
    0a001000-0a1fffff : System RAM
    0a200000-0a20efff : ACPI Non-volatile Storage
    0a20f000-c3221017 : System RAM
    c3221018-c322e857 : System RAM
    c322e858-c4a36fff : System RAM
    c4a37000-c4b2afff : Reserved
    c4b2b000-c70a3fff : System RAM
    c70a4000-c70a4fff : Reserved
    c70a5000-c8912fff : System RAM
    c8913000-c9e31fff : Reserved
    c9e12000-c9e15fff : MSFT0101:00
        c9e12000-c9e15fff : MSFT0101:00
    c9e16000-c9e19fff : MSFT0101:00
        c9e16000-c9e19fff : MSFT0101:00
    c9e32000-c9e91fff : ACPI Tables
    c9e92000-cb589fff : ACPI Non-volatile Storage
    cb58a000-cd1fefff : Reserved
    cd1ff000-cdffffff : System RAM
    ce000000-cfffffff : Reserved
    d0000000-fec01fff : Reserved
    d0000000-febfffff : PCI Bus 0000:00
        d0000000-e01fffff : PCI Bus 0000:04
        d0000000-dfffffff : 0000:04:00.0
        e0000000-e01fffff : 0000:04:00.0
        e0300000-e04fffff : PCI Bus 0000:01
        e0300000-e03fffff : 0000:01:00.0
            e0300000-e03fffff : 0000:01:00.0
        e0400000-e0403fff : 0000:01:00.0
        e0404000-e0404fff : 0000:01:00.0
        e0500000-e06fffff : PCI Bus 0000:01
        e0700000-e08fffff : PCI Bus 0000:02
        f0000000-f7ffffff : PCI MMCONFIG 0000 [bus 00-7f]
        f0000000-f7ffffff : Reserved
            f0000000-f7ffffff : pnp 00:00
        fca00000-fcdfffff : PCI Bus 0000:04
        fca00000-fcafffff : 0000:04:00.4
            fca00000-fcafffff : xhci-hcd
        fcb00000-fcbfffff : 0000:04:00.3
            fcb00000-fcbfffff : xhci-hcd
        fcc00000-fccfffff : 0000:04:00.2
            fcc00000-fccfffff : ccp
        fcd00000-fcd7ffff : 0000:04:00.0
        fcd80000-fcdbffff : 0000:04:00.5
            fcd80000-fcdbffff : AMD ACP3x audio
            fcd80000-fcd90200 : acp_pdm_iomem
        fcdc0000-fcdc7fff : 0000:04:00.6
            fcdc0000-fcdc7fff : ICH HD audio
        fcdc8000-fcdcbfff : 0000:04:00.1
            fcdc8000-fcdcbfff : ICH HD audio
        fcdcc000-fcdcdfff : 0000:04:00.2
            fcdcc000-fcdcdfff : ccp
        fce00000-fcefffff : PCI Bus 0000:03
        fce00000-fce03fff : 0000:03:00.0
            fce00000-fce03fff : nvme
        fcf00000-fcffffff : PCI Bus 0000:02
        fcf00000-fcf00fff : 0000:02:00.0
            fcf00000-fcf00fff : rtsx_pci
        fd000000-fdffffff : Reserved
        fd210510-fd21053f : MSFT0101:00
        fd300000-fd37ffff : amd_iommu
    fec00000-fec003ff : IOAPIC 0
    fec01000-fec013ff : IOAPIC 1
    fec10000-fec10fff : Reserved
    fec10000-fec10fff : pnp 00:04
    fed00000-fed00fff : Reserved
    fed00000-fed003ff : HPET 0
        fed00000-fed003ff : PNP0103:00
    fed40000-fed44fff : Reserved
    fed80000-fed8ffff : Reserved
    fed81200-fed812ff : AMDI0030:00
    fed81500-fed818ff : AMDI0030:00
    fedc0000-fedc0fff : pnp 00:04
    fedc4000-fedc9fff : Reserved
    fedc5000-fedc5fff : AMDI0010:03
        fedc5000-fedc5fff : AMDI0010:03 AMDI0010:03
    fedcc000-fedcefff : Reserved
    fedd5000-fedd5fff : Reserved
    fee00000-ffffffff : PCI Bus 0000:00
    fee00000-fee00fff : Local APIC
        fee00000-fee00fff : pnp 00:04
    ff000000-ffffffff : Reserved
        ff000000-ffffffff : pnp 00:04
    100000000-40e2fffff : System RAM
    2f0a00000-2f1a02607 : Kernel code
    2f1c00000-2f2695fff : Kernel rodata
    2f2800000-2f2c48a3f : Kernel data
    2f2fb5000-2f41fffff : Kernel bss
    40e300000-42fffffff : Reserved
    3fffe0000000-3fffffffffff : 0000:04:00.0

x86
---

.. code-block:: bash

    # cat /proc/iomem 
    00000000-00000fff : Reserved
    00001000-0009fbff : System RAM
    0009fc00-0009ffff : Reserved
    000a0000-000bffff : PCI Bus 0000:00
    000a0000-000bffff : Video RAM area
    000c0000-000c99ff : Video ROM
    000ca000-000cadff : Adapter ROM
    000cb000-000cb5ff : Adapter ROM
    000f0000-000fffff : Reserved
    000f0000-000fffff : System ROM
    00100000-07fdcfff : System RAM
    05400000-06160c1a : Kernel code
    06161000-065defff : Kernel rodata
    065df000-067d487f : Kernel data
    068c4000-06950fff : Kernel bss
    07fdd000-07ffffff : Reserved
    08000000-febfffff : PCI Bus 0000:00
    fd000000-fdffffff : 0000:00:02.0
    fe000000-fe003fff : 0000:00:03.0
        fe000000-fe003fff : virtio-pci-modern
    fe004000-fe007fff : 0000:00:04.0
        fe004000-fe007fff : virtio-pci-modern
    feb00000-feb7ffff : 0000:00:03.0
    feb90000-feb90fff : 0000:00:02.0
    feb91000-feb91fff : 0000:00:03.0
    feb92000-feb92fff : 0000:00:04.0
    fec00000-fec003ff : IOAPIC 0
    fed00000-fed003ff : PNP0103:00
    fee00000-fee00fff : Local APIC
    fffc0000-ffffffff : Reserved