===
GDB
===

Coredump
--------

Generate coredump file when application crash.

.. list-table::
   :header-rows: 1

   * - Options
     - Description
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
     - Description
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
     - Description
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

Debugging Forks
---------------

.. code-block:: 

  set follow-fork-mode <mode>

Set the debugger response to a program call of fork or vfork. A call to fork or vfork creates a new process. The mode argument can be:

* **parent** The original process is debugged after a fork. The child process runs unimpeded. This is the default.
* **child** The new process is debugged after a fork. The parent process runs unimpeded.

.. code-block:: 

  show follow-fork-mode

Display the current debugger response to a fork or vfork call.

.. code-block:: 

  set detach-on-fork <mode>

Tells gdb whether to detach one of the processes after a fork, or retain debugger control over them both.

* **on** The child process (or parent process, depending on the value of follow-fork-mode) will be detached and allowed to run independently. This is the default.

* **off** Both processes will be held under the control of GDB. One process (child or parent, depending on the value of follow-fork-mode) is debugged as usual, while the other is held suspended.

.. code-block::
  
  show detach-on-fork

Show whether detach-on-fork mode is on/off.

GDB with program arguments
==========================

On-start gdb:

.. code-block:: 

  gdb --args executablename arg1 arg2 arg3

After gdb has been started:

.. code-block:: 

  set args arg1 arg2 arg3
