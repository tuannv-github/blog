===
Git
===

Configurations
==============

User global git configuration file :file:`~/.gitconfig`.

List configurations

.. code-block:: 

    git config --list

Global Username and Email
-------------------------

.. code-block:: 

    git config --global user.name "tuannv"
    git config --global user.email "tuannv.email@gmail.com"

Fetch
=====

* Fetch branches and/or tags (collectively, "refs") from one or more other repositories, along with the objects necessary to complete their histories.
* When no remote is specified, by default the **origin** remote will be used, unless there’s an upstream branch configured for the current branch.


.. code-block::

    git fetch [<options>] [<repository> [<refspec>…​]]

.. list-table:: 
    
    * - Options
      - Description
    * - :code:`<refspec>`
      - Specifies which refs to fetch and which local refs to update. When no <refspec>s appear on the command line, the refs to fetch are read from remote.<repository>.fetch variables instead 
  
Fetch master branch from remote named origin

.. code-block::

    git fetch origin master

Merge
=====

Pull
====