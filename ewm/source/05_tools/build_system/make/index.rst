========
Makefile
========

Link: https://www.gnu.org/software/make/manual/make.html

Makefile Variables
==================

A variable is a name defined in a makefile to represent a string of text, called the variable's value.

Either :code:`$(foo)` or :code:`${foo}` is a valid reference to the variable :code:`foo`.

.. code-block:: Makefile

    objects = program.o foo.o utils.o
    program : $(objects)
            cc -o program $(objects)

    $(objects) : defs.h

The two flavors of variables
----------------------------

* Recursively expanded variable

.. code-block:: Makefile

    foo = $(bar)
    bar = $(ugh)
    ugh = Huh?

    all:;echo $(foo)

* Simply expanded variables 

.. code-block:: Makefile

    x := foo
    y := $(x) bar
    x := later

is equivalent to

.. code-block:: Makefile

    y := foo bar
    x := later


Automatic Variables
-------------------

.. list-table:: 

    * - Variables
      - Description
    * - :code:`$@`
      - The file name of the target of the rule.
    * - :code:`$%`
      - The target member name, when the target is an archive member.
    * - :code:`$<`
      - The name of the first prerequisite.
    * - :code:`$?`
      - The names of all the prerequisites that are newer than the target, with spaces between them.
    * - :code:`$^`
      - The names of all the prerequisites, with spaces between them.

Built-in variable
-----------------

:code:`$(CURDIR)`
    It provides the full absolute pathname of the directory where the Makefile is located.

    .. code-block:: Makefile

        current_directory:
            @echo "The current directory is: $(CURDIR)"

Instead of Executing Recipes
============================

| :code:`-n` 
| :code:`--just-print`
| :code:`--dry-run`
| :code:`--recon`

“No-op”. Caes make to print the recipes that are needed to make the targets up to date, but not actually execute them.

:code:`make -n`

Print database
==============

:code:`--print-data-base`

Print the data base (rules and variable values) that results from reading the makefiles;

To print the data base without trying to remake any files, use :code:`make -qp`.

:code:`make -pq`

Exclude the implicit rules

.. code-block:: sh

    make -p | awk -F: '/^[a-zA-Z0-9_-]+:/ && !/^\./ {print}'


Verbosity
=========

.. code-block:: Makefile

    # Define a variable for verbosity (default is empty, i.e., not verbose)
    VERBOSE =

    # Define a target that prints the current target being built
    print_target:
        @echo "Building target: $@"

    # Define your main targets and their dependencies
    all: print_target target1 target2

    target1:
        $(VERBOSE) @echo "Building target: $@"
        # Add your build commands for target1 here

    target2:
        $(VERBOSE) @echo "Building target: $@"
        # Add your build commands for target2 here

Inclusion
=========

.. code-block:: Makefile

    # Include an external file named "common.mk"
    include common.mk

    # Define additional variables and rules specific to your project
    CC = gcc
    CFLAGS = -Wall -O2
    SRC_DIR = src
    OUT_DIR = build

    all: $(OUT_DIR)/myapp

    $(OUT_DIR)/myapp: $(OUT_DIR)/main.o $(OUT_DIR)/other.o
        $(CC) $(CFLAGS) -I$(INC_DIR) $^ -o $@

    $(OUT_DIR)/main.o: $(SRC_DIR)/main.c
        $(CC) $(CFLAGS) -c $< -o $@

    $(OUT_DIR)/other.o: $(SRC_DIR)/other.c
        $(CC) $(CFLAGS) -c $< -o $@

    clean:
        rm -rf $(OUT_DIR)/*.o $(OUT_DIR)/myapp

    .PHONY: all clean

.. code-block:: Makefile

    # common.mk

    INC_DIR = include
    LIB_DIR = lib

    # Shared compiler and flags
    CC = gcc
    CFLAGS = -Wall -O2

Recursive Use of make
=====================

.. code-block:: Makefile

    subsystem:
        cd subdir && $(MAKE)

or, equivalently:

.. code-block:: Makefile

    subsystem:
            $(MAKE) -C subdir
