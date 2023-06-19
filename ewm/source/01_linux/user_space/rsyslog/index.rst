=======
Rsyslog
=======

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


Ruleset

.. code-block::

    <facility>.<severity_level>	<destination>

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

Debug

.. code-block:: 

    sudo ss -tulp | grep "rsyslog"

.. code-block::

    logger "message"
    logger -p local0.notice -t "Backup script" "The database backups successfully to FreeBSD NAS server."

Facility
~~~~~~~~

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

Level
~~~~~

.. list-table::
   
    * - Facility
      - Description