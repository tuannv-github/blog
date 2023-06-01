==
ss
==

Options
=======

:code:`ss` is used to dump socket statistics.

* It allows showing information similar to netstat.
* It can display more TCP and state information than other tools.

.. list-table::
   :header-rows: 1

   * - Short
     - Long
     - Description
   * - :code:`-t`
     - :code:`--tcp`
     - Display TCP sockets.
   * - :code:`-u`
     - :code:`--udp`
     - Display UDP sockets.
   * - :code:`-x`
     - :code:`--unix`
     - Display Unix domain sockets (alias for -f unix).
   * - :code:`-l`
     - :code:`--listening`
     - Display only listening sockets (these are omitted by default).
   * - :code:`-a`
     - :code:`--all`
     - Display both listening and non-listening (for TCP this means established connections) sockets.
   * - :code:`-p`
     - :code:`--processes`
     - Show process using socket.

Output Description
==================

.. list-table::
   :header-rows: 1

   * - Column
     - Description
   * - Netid
     - Type of socket. Common types are tcp, ucp, u_str (Unix stream), u_dgr (Unix datagram)
   * - State 
     - State of the socket. Most commonly ESTAB (established), UNCONN (unconnected), LISTEN (listening).
   * - Recv-Q
     - Number of received packets in the queue.
   * - Send-Q
     - Number of sent packets in the queue.
   * - Local address:port
     - Address of local machine and port.
   * - Peer address:port
     - Address of remote machine and port.

Examples
========

List Unix domain socket with process info using such sockets.

.. code-block:: 

    ss -px

Show connected sockets from specific address

.. code-block:: 

    ss dst 192.168.1.139
