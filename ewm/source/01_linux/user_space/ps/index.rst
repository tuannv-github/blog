===
ps
===

report a snapshot of the current processes.

.. list-table:: 

    * - Options
      - Description
    * - :code:`-e`
      - Select all processes
    * - :code:`-f`
      - Do full-format listing
    * - :code:`-F`
      - Extra full format.
    * - :code:`-u` *userlist*
      - Select by effective user ID (EUID) or name
    * - :code:`-o` *format*
      - User-defined format
    * - :code:`f`
      - ASCII art process hierarchy (forest)
    * - :code:`u`
      - Display user-oriented format.

.. code-block:: 

    ps -e
    ps -ef
    ps -ef f
    ps -eF
    ps -ely
