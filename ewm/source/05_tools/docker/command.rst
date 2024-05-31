===============
Docker Commands
===============

Docker Image
============

Download
--------

.. code-block:: bash

  docker image pull ubuntu:latest

List
----
List all docker image installed

.. code-block:: bash

  docker images

Remove
------
.. code-block:: bash

  docker rmi [OPTIONS] IMAGE [IMAGE...]

Remove dangling images

.. code-block:: bash

  docker rmi -f $(docker images -f "dangling=true" -q)

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

List containers
===============

.. code-block:: 

    docker ps [OPTIONS]

.. list-table::
   :header-rows: 1

   * - Name,shorthand
     - Default
     - Description
   * - :code:`--all`, :code:`-a`
     - 
     - Show all containers (default shows just running)
   * - :code:`--no-trunc`
     - 
     - Donot truncate output

Exec container
==============

.. code-block:: 

    docker exec -it <container_name> <cmd>

.. list-table::
   :header-rows: 1

   * - Name,shorthand
     - Default
     - Description
   * - :code:`--interactive`, :code:`-i`
     - 
     - Keep STDIN open even if not attached
   * - :code:`--tty`, :code:`-t`
     - 
     - Allocate a pseudo-TTY

.. code-block:: 

  export DOCKER_BUILDKIT=0

Examples
========

