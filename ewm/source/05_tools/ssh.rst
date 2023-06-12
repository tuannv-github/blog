===
SSH
===

SSH login using private key
===========================
.. code-block:: 

    ssh -i ~/.ssh/mykey user@host

Instructions
============

* Create a pair of keys using :code:`ssh-keygen`
* Copy :code:`*.pub` public key to :code:`~/.ssh/authorized_keys` manually or ssh-copy-id

.. code-block::

    ssh-copy-id -i ~/.ssh/mykey.pub user@host

* SSH login using ssh private key.

Examples
========

VSCode

.. code-block:: 

    Host 192.168.0.10
        HostName 192.168.0.10
        User tuannv
        IdentityFile ~/.ssh/server_10
