=====
Alias
=====

Aliases don't take arguments. With an alias like :code:`alias foo='echo $1'`, the :code:`$1` will be expanded by the shell to the shell's first argument (which is likely nothing) when the alias is run.

.. code-block:: 

    ~/blog/ewm$ alias foo="echo $0"
    ~/blog/ewm$ foo
    /bin/bash
    ~/blog/ewm$ alias foo="echo $1"
    ~/blog/ewm$ foo

    ~/blog/ewm$
    ~/blog/ewm$ unalias foo
    ~/blog/ewm$ foo
        Command 'foo' not found, did you mean:
        command 'roo' from snap roo (2.0.3)
        command 'fox' from deb objcryst-fox (1.9.6.0-2.2)
        command 'goo' from deb goo (0.155+ds-4)
        command 'foot' from deb foot (1.11.0-2)
        command 'fop' from deb fop (1:2.6-2)
        command 'fio' from deb fio (3.28-1)
        See 'snap info <snapname>' for additional versions.
    ~/blog/ewm$ unalias -a