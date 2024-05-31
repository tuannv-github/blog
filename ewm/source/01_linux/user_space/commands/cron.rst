====
Cron
====

**cron** comes from chron, the Greek prefix for 'time'. Cron is a daemon which runs at the times of system boot.

**crontab** (CRON TABle) is a file which contains the schedule of cron entries to be run and at specified times. File location varies by operating systems.

**cron job** or **cron schedule**: is a specific set of execution instructions specifying day, time and command to execute. crontab can have multiple execution statements.

Crontab file location
=====================

.. code-block:: 

    /var/spool/cron/crontabs/<user>

System crontab
==============

.. code-block:: 

    # For details see man 4 crontabs

    # Example of job definition:
    .---------------- minute (0 - 59)
    |  .------------- hour (0 - 23)
    |  |  .---------- day of month (1 - 31)
    |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
    |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
    |  |  |  |  |
    *  *  *  *  * user-name  command to be executed
