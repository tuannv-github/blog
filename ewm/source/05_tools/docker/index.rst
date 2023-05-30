======
Docker
======

Download image
==============

.. code-block:: bash

    docker image pull ubuntu:latest

List all docker image installed

.. code-block:: bash

    docker images


Create a container
==================

.. code-block:: bash

    docker run --name tuannv -d -i -t ubuntu:latest /bin/sh

.. list-table::
   :header-rows: 1

   * - Name,shorthand
     - Default
     - Description
   * - :code:`--name`
     - 
     - Assign a name to the container
   * - :code:`--detach`, :code:`-d`
     - 
     - Run container in background and print container ID
   * - :code:`--interactive`, :code:`-i`
     - 
     - Keep STDIN open even if not attached
   * - :code:`--tty`, :code:`-t`
     - 
     - Allocate a pseudo-TTY

Exec container
==============
