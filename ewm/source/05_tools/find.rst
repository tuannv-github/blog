====
Find
====

.. code-block:: 

    find [-H] [-L] [-P] [-D debugopts] [-Olevel] [starting-point...] [expression]

Ignore permission denied
------------------------

.. code-block:: 

    find / -name a.txt 2> /dev/null
