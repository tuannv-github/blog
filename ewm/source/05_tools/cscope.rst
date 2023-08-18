======
CScope
======

.. code-block:: 

    rm cscope.files ; git ls-files | grep '\.c$\|\.h$' > cscope.files
    cscope -b -i cscope.files
    CSCOPE_DB=cscope.out; export CSCOPE_DB 

.. list-table:: 
    
    * - Option
      - Description
    * - :code:`-R`
      - Recurse subdirectories for source files.
    * - :code:`-b`
      - Build the cross-reference only.
    * - :code:`-d`
      - Do not update the cross-reference.
    * - :code:`-i namefile`
      - Browse through all source files whose names are listed in namefile (file names separated by spaces, tabs, or new-lines) instead of the default (cscope.files).

Build database:

.. code-block:: 
    
    cscope -R -b

Open Cscope without rebuilding database:

.. code-block::

    cscope -d
