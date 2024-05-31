==========
Dockerfile
==========

A Dockerfile is a text document that contains all the **commands** a user could call on the command line to **assemble an image**.

Build docker image
==================

To build docker image using dockerfile:

.. code-block:: 

    docker build .

Options
-------

.. list-table::
   :header-rows: 1

   * - Name,shorthand
     - Default
     - Description
   * - :code:`--file`, :code:`-f`
     - PATH/Dockerfile
     - Name of the Dockerfile


Example
-------

.. code-block:: 

    docker build -f blog

Docker file contents
====================

.. list-table::
   :header-rows: 1

   * - Command
     - Example
   * - :code:`FROM` ImageName
     - :code:`FROM ubuntu:22.04`
