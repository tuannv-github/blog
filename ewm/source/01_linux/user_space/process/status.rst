==============
Process status
==============

Process capabilities
--------------------

.. code-block:: 

  cat /proc/<PID>/status | grep Cap

  CapInh: 00000000a80425fb (Inherited capabilities)
  CapPrm: 0000000000000000 (Permitted capabilities)
  CapEff: 0000000000000000 (Effective capabilities)
  CapBnd: 00000000a80425fb (Bounding set)
  CapAmb: 000000000000000  (Ambient capabilities set)


.. code-block:: 

  capsh --decode=00000000a80425fb

  0x00000000a80425fb=cap_chown,cap_dac_override,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,cap_setpcap,cap_net_bind_service,cap_net_raw,cap_sys_chroot,cap_mknod,cap_audit_write,cap_setfcap

.. list-table:: 

  * - Key
    - Descriptions
  * - CapInh
    - Inherited capabilities
  * - CapPrm
    - Permitted capabilities
  * - CapEff
    - Effective capabilities
  * - CapBnd
    - Bounding set
  * - CapAmb
    - Ambient capabilities set
