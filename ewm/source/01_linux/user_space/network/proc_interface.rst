===============
/proc interface
===============

The core socket networking parameters can be accessed via files in the directory **/proc/sys/net/core/**.

.. list-table:: 

    * - Parameters
      - Description
    * - **rmem_default**
      - contains the default setting in bytes of the socket receive buffer.
    * - **rmem_max**
      - contains the maximum socket receive buffer size in bytes which a user may set by using the SO_RCVBUF socket option.
    * - **wmem_default**
      - contains the default setting in bytes of the socket send buffer.
    * - **wmem_max**
      - contains the maximum socket send buffer size in bytes which a user may set by using the SO_SNDBUF socket option.
    * - **message_cost** and **message_burst**
      - configure the token bucket filter used to load limit warning messages caused by external network events.
    * - **netdev_max_backlog**
      - Maximum number of packets in the global input queue.
    * - **optmem_max**
      - Maximum length of ancillary data and user control data like the iovecs per socket.
