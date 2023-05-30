======
netcat
======

TCP server
==========

Server

.. code-block:: 

    nc -l 0.0.0.0 8989

Always-On Server

.. code-block:: 

    while true; do nc -l 0.0.0.0 8989; done

.. list-table::
   :header-rows: 1

   * - Option
     - Name
     - Description
   * - :code:`-l`
     - 
     - Used to specify that nc should listen for an incoming connection rather than initiate a connection to a remote host.

Client

.. code-block:: 

    nc localhost 8989

UDP server
==========

Server

.. code-block:: 

    nc -luw 0 0.0.0.0 8989

Always-On Server

.. code-block:: 

    while true; do nc -luw 0 0.0.0.0 8989; done

.. list-table::
   :header-rows: 1

   * - Option
     - Name
     - Description
   * - :code:`-u`
     - 
     - Use UDP instead of the default option of TCP.
   * - :code:`-w`
     - timeout
     - If a connection and stdin are idle for more than timeout seconds, then the connection is silently closed.

Client

.. code-block:: 

    nc -u localhost 8989