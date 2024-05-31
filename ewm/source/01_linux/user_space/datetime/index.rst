=========
Date Time
=========

System Clock vs Hardware Clock
==============================

.. list-table:: 
    
    * - System Clock
      - Hardware Clock
    * - **Maintained:** by Operating System
      - **Maintained:** in BIOS
    * - **Source:** Query online time server whenever the computer is power on
      - **Source:** Continue to run when the computer is power off
    * - **Purpose:** Linux programs and services reply on the system clock
      - **Purpose:** Use to set the time for system clock upon installation if timer server is not avalable 

Hardware Clock
==============

* Get hardware clock

.. code-block::

    $ sudo hwclock
    2022-10-08 15:00:00.885214-0400

* System clock to Hardware clock

.. code-block::

    $ sudo hwclock --systohc

* Hardware clock to System clock

.. code-block::

    $ sudo hwclock --hctosys

System Clock
============

Command :code:`date` print or set the system date and time

* Get time in system timezone

.. code-block:: 

    $ date
    Sat Oct  8 15:00:09 +07 2022

* Get UTC time

.. code-block:: 

    $ date -u
    Fri Jun 30 09:27:51 AM UTC 2023

* Systemd command

.. code-block:: 

    $ timedatectl
                   Local time: Fri 2023-06-30 04:22:37 UTC
               Universal time: Fri 2023-06-30 04:22:37 UTC
                     RTC time: Fri 2023-06-30 04:22:37
                    Time zone: Etc/UTC (UTC, +0000)
    System clock synchronized: yes
                  NTP service: active
              RTC in local TZ: no

* Set system datetime

.. code-block:: 

    date -s "STRING"
    date --set="STRING"

    date -s "2 OCT 2006 18:00:00"
    date --set="2 OCT 2006 18:00:00"

Coordinated Universal Time
==========================

* Coordinated Universal Time or UTC is the primary time standard by which the world regulates clocks and time.
* A Standard, Not a Time Zone: UTC is the time standard commonly used across the world. The world's timing centers have agreed to keep their time scales closely synchronized - or coordinated - therefore the name Coordinated Universal Time.

Timezone
========

Timezone examples

.. code-block::

    Asia/Ho_Chi_Minh
    Asia/Hong_Kong
    US/Alaska
    US/Aleutian
    US/Arizona

Timezone files

.. code-block:: bash

    ls /usr/share/zoneinfo/

Get current timezone:

.. code-block:: bash

    cat /etc/localtime

Update timezone using soft link

.. code-block::

    sudo ln -sf /usr/share/zoneinfo/zoneinfo /etc/localtime

Update timezone using timedatectl

.. code-block:: bash

    timedatectl list-timezones
    timedatectl list-timezones | grep Ho_Chi_Minh
    sudo timedatectl set-timezone [timezone]
    timedatectl

Update timezone using the tzdata

.. code-block:: bash

    sudo dpkg-reconfigure tzdata
