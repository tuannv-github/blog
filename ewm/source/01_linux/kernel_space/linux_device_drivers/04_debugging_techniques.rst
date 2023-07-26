====================
Debugging Techniques
====================

Code kernel có thể coi là phức tạp hơn code application vì:

* Không thể chạy bằng debugger dễ  dàng
* Không thể trace code dễ dàng 
* Các tính năng đa phần là API để process gọi, phải làm test
* Có thể khó tái hiện lỗi 
* Khi xảy ra lỗi thì có thể  "bring down" toàn hệ thống, làm mất thông tin để debug

Debugging Support in the Kernel
-------------------------------

Debugging by Printing - printk
------------------------------

Debugging by Querying 
------------------------------

/proc/
~~~~~~

ioctl
~~~~~


Debugging by Watching
---------------------

strace
~~~~~~

Debugging System Faults
-----------------------

Oops Messages
~~~~~~~~~~~~~

System Hangs
~~~~~~~~~~~~

Debuggers and Related Tools 
---------------------------

Using gdb
~~~~~~~~~

The kdb Kernel Debugger
~~~~~~~~~~~~~~~~~~~~~~~

The kgdb Patches:
~~~~~~~~~~~~~~~~~

The User-Mode Linux Port
~~~~~~~~~~~~~~~~~~~~~~~~

The Linux Trace Toolkit
~~~~~~~~~~~~~~~~~~~~~~~

Dynamic Probes
~~~~~~~~~~~~~~
