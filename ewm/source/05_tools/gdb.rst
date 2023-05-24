===
GDB
===

Coredump
--------

Generate coredump file when application crash.

.. list-table::
   :header-rows: 1

   * - Options
     - Explain
     - Example
   * - :code:`-c`
     - The maximum size of core files created. 
     - :code:`ulimit -c unlimited`

.. code-block::

  ulimit -c unlimited
  echo coredump-%e-%t-%p-%i > /proc/sys/kernel/core_pattern 

GDB options
-----------

.. list-table::
   :header-rows: 1

   * - Options
     - Explain
     - Example
   * - <executable_file>
     - Debug an executable file
     - :code:`gdb ./a.out`
   * - <executable_file>  <core_dump_file>
     - Open core dump file
     - :code:`gdb ./a.out ./coredump_a`
   * - :code:`-p` <PID>
     - Attach debugger to a running process
     - :code:`gdb -p`

GDB commands
------------

.. list-table::
   :header-rows: 1

   * - Command
     - Explain
     - Example
   * - :code:`run` | :code:`r`
     - Restart current process
     - :code:`r`
   * - :code:`kill` | :code:`k`
     - Kill current process
     - :code:`k`
   * - :code:`next` | :code:`n`
     - Go to the next line
     - :code:`n`
   * - :code:`step` | :code:`s`
     - Step into a function
     - :code:`s`
   * - :code:`finish` | :code:`fin`
     - Execute until current function exit
     - :code:`fin`
   * - :code:`p`
     - Print in decimal format
     - :code:`p/x hello`
   * - :code:`p/x`
     - Print in hexadecimal format
     - :code:`p/x hello`
   * - :code:`p/t`
     - Print in binary format
     - :code:`p/t hello`
   * - :code:`watch <address>`
     - Stop wen watched variable change
     - :code:`watch (struct student *)peter`
   * - :code:`call <function()>`
     - Call a function with gdb
     - :code:`call lookup_student(student_id)`
   * - :code:`set <variable>=<value>`
     - Change variable value using gdb
     - :code:`set age=20`
