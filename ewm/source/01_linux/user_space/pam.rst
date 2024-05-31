================================
Pluggable Authentication Modules
================================

**Linux-PAM** is a system of libraries that handle the authentication tasks of applications (services) on the system.

A PAM-Aware Application
=======================

.. code-block:: C

    #include <pwd.h>
    #include <stdio.h>
    #include <sys/types.h>
    
    #include <security/pam_appl.h>
    #include <security/pam_misc.h>

    #define MY_CONFIG "custom_application"
    static struct pam_conv conv = { misc_conv, NULL };

    main( )
    {
        pam_handle_t *pamh;
        int result;
        struct passwd *pw;
        if ((pw = getpwuid(getuid( ))) == NULL)
            perror("getpwuid");
        else if ((result = pam_start(MY_CONFIG, pw->pw_name, &conv, &pamh)) != PAM_SUCCESS)
            fprintf(stderr, "start failed: %d\n", result);
        else if ((result = pam_authenticate(pamh, 0)) != PAM_SUCCESS)
            fprintf(stderr, "authenticate failed: %d\n", result);
        else if ((result = pam_acct_mgmt(pamh, 0)) != PAM_SUCCESS)
            fprintf(stderr, "acct_mgmt failed: %d\n", result);
        else if ((result = pam_end(pamh, result)) != PAM_SUCCESS)
            fprintf(stderr, "end failed: %d\n", result);
        else
            Run_My_Big_Application( );            /* Run your application code */
    }

.. code-block:: 

    gcc myprogram.c -lpam -lpam_misc

PAM Configurations
==================

An important feature of PAM, is that a number of rules may be stacked to combine the services of a number of PAMs for a given authentication task.

Syntax
------

.. code-block:: 

    type  control  module-path  module-arguments

/etc/pam.d/custom_application
-----------------------------

The service is typically the familiar name of the corresponding application.

.. code-block:: 

    auth            required    pam_permit.so
    account         required    pam_permit.so
    password        required    pam_permit.so
    session         required    pam_permit.so
