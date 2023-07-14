=======
Rsyslog
=======

RSYSLOG is the rocket-fast system for log processing.
It offers high-performance, great security features and a modular design.

Rsyslog Configurations
======================

Restart service

.. code-block::

    sudo systemctl start rsyslog

Edit configurations

.. code-block:: bash

    sudo vim /etc/rsyslog.conf


UDP server

.. code-block:: 

    $ModLoad imudp
    $UDPServerRun 514

TCP server

.. code-block:: 

    $ModLoad imtcp
    $InputTCPServerRun 514


Rule sets

.. code-block::

    <facility>.<severity_level>	<destination>
    <facility>.<severity_level>;<facility>.<severity_level>	<destination>

.. list-table::

    * - 
      - Description
    * - facility
      - Type of process/application generating message, they include auth, cron, daemon, kernel, local0..local7. Using * means all facilities.
    * - severity_level
      - Type of log message: emerg-0, alert-1, crit-2, err-3, warn-4, notice-5, info-6, debug-7. Using * means all severity levels and none implies no severity level.
    * - destination
      - Either local file or remote rsyslog server (defined in the form IP:port).

Example

.. code-block:: 

    $template RemoteLogs,"/var/log/%HOSTNAME%/%PROGRAMNAME%.log"
    *.* ?RemoteLogs 
    & ~


Rsyslog Test
============

Check listening socket
----------------------

.. code-block:: 

    sudo ss -tulp | grep "rsyslog"

Simple server
-------------

.. code-block:: 

  mkfifo /tmp/test_rsyslog
  echo "local0.* /tmp/test_rsyslog" > /etc/rsyslog.d/test_rsyslog.conf
  echo "local1.* /tmp/test_rsyslog" >> /etc/rsyslog.d/test_rsyslog.conf
  service rsyslog restart
  cat /tmp/test_rsyslog
  rm /etc/rssyslog.conf.d/test_rsyslog.conf
  service rsyslog restart

Simple client
-------------

.. code-block::

    logger "message"
    logger -p local0.notice -t "Backup script" "The database backups successfully to FreeBSD NAS server."
    logger -p local1.notice -t "Backup script" "The database backups successfully to FreeBSD NAS server."

Rsyslog Facility
================

The facility argument is used to specify what type of program is logging the message.  This lets the configuration file specify that messages from different facilities will be handled differently.

.. list-table::
   
    * - Facility
      - Description
    * - LOG_AUTH
      - security/authorization messages
    * - LOG_AUTHPRIV
      - security/authorization messages (private)
    * - LOG_CRON
      - clock daemon (cron and at)
    * - LOG_DAEMON
      - system daemons without separate facility value
    * - LOG_FTP
      - ftp daemon
    * - LOG_KERN
      - kernel messages (these can't be generated from user processes)
    * - LOG_LOCAL0 through LOG_LOCAL7
      - reserved for local use

Rsyslog Level
=============

.. list-table::
   
    * - Code
      - Level
      - Description
      - General Description
    * - 0
      - emerg, panic
      - Emergency: system is unusable
      - A "panic" condition usually affecting multiple apps/servers/sites. At this level it would usually notify all tech staff on call.
    * - 1
      - alert
      - Alert: action must be taken immediately
      - Should be corrected immediately, therefore notify staff who can fix the problem. An example would be the loss of a primary ISP connection.
    * - 2
      - crit
      - Critical: critical conditions
      - Should be corrected immediately, but indicates failure in a primary system, an example is a loss of a backup ISP connection.
    * - 3
      - err, error
      - Error: error conditions
      - Non-urgent failures, these should be relayed to developers or admins; each item must be resolved within a given time.
    * - 4
      - warning, warn
      - Warning: warning conditions
      - Warning messages, not an error, but indication that an error will occur if action is not taken, e.g. file system 85% full - each item must be resolved within a given time.
    * - 5
      - notice
      - Notice: normal but significant condition
      - Events that are unusual but not error conditions - might be summarized in an email to developers or admins to spot potential problems - no immediate action required.
    * - 6
      - info
      - Informational: informational messages
      - Normal operational messages - may be harvested for reporting, measuring throughput, etc. - no action required.
    * - 7
      - debug
      - Debug: debug-level messages
      - Info useful to developers for debugging the application, not useful during operations.

Rsyslog C Examples
==================

.. code-block:: C
  
  #include <syslog.h>

  void openlog(const char *ident, int option, int facility);
  void syslog(int priority, const char *format, ...);
  void closelog(void);

  void vsyslog(int priority, const char *format, va_list ap);

Single facility
---------------

.. code-block:: C

  #include <syslog.h>

  int main()
  {
    setlogmask (LOG_UPTO (LOG_NOTICE));

    openlog ("exampleprog", LOG_CONS | LOG_PID | LOG_NDELAY, LOG_LOCAL1);

    syslog (LOG_NOTICE, "Program started by User %d", getuid ());
    syslog (LOG_INFO, "A tree falls in a forest");

    closelog ();

    return 0;
  }

Multiple facilities
-------------------

.. code-block:: C

  #include <syslog.h>

  int main()
  {
    setlogmask (LOG_UPTO (LOG_NOTICE));

    openlog ("exampleprog", LOG_CONS | LOG_PID | LOG_NDELAY, LOG_LOCAL0 | LOG_LOCAL1);

    syslog (LOG_NOTICE, "Program started by User %d", getuid ());
    syslog (LOG_INFO, "A tree falls in a forest");

    syslog(LOG_NOTICE|LOG_LOCAL0, "message for local0");
    syslog(LOG_NOTICE|LOG_LOCAL1, "message for local1");

    closelog ();

    return 0;
  }

Rsyslog Rotate (logrotate)
==========================

**logrotate** is designed to ease administration of systems that generate large numbers of log files.  It allows automatic rotation, compression, removal, and mailing of log files. Each log file may be handled daily, weekly, monthly, or when it grows too large.

Normally, **logrotate** is run as a daily cron job.  It will not modify a log more than once in one day unless the criterion for that log is **based on the log's size** and logrotate is being run **more than once each day**, or unless the :code:`-f` or :code:`--force` option is used.

.. code-block:: bash

  logrotate [--force] [--debug] [--state file] [--skip-state-lock]
       [--wait-for-state-lock] [--verbose] [--log file] [--mail command]
       config_file [config_file2 ...]