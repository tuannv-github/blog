====
User
====

List all groups
---------------

.. code-block:: 

    cat /etc/group

    sudo:x:27:ont,hoangtu1,tramtn,tuhn4,ducns3,phatkt

.. image:: imgs/etc_group.png

.. list-table:: 

    * - Index
      - Value
      - Description
    * - 1
      - Group name
      - Contains the name assigned to the group.
    * - 2
      - Password
      - Generally password is not used, hence it is empty/blank. It can store encrypted password. This is useful to implement privileged groups.
    * - 3
      - Group ID (GID)
      - Each user must be assigned a group ID.
    * - 4
      - Group List
      - It is a list of user names of users who are members of the group. The user names, must be separated by commas.

List all users
--------------

.. code-block:: 

    cat /etc/passwd

.. image:: imgs/etc_passwd.jpg

.. image:: imgs/etc_shadow.jpg

Who am I and What groups I belong to?
-------------------------------------

.. code-block:: 

  whoami
  groups

The id command is preferred command to list groups a user belongs to On Linux or Unix-like operating systems

.. code-block:: bash

    id -Gn userNameHere
