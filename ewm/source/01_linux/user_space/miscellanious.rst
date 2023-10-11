=====================
Miscellanious Command
=====================

.. code-block:: 

    ip address add [ip]/[mask-digits] dev [nic]

    ip address

    ip address add 192.168.99.37/24 dev eth0

.. code-block:: 


    nmcli dev wifi list

    sudo nmcli dev wifi connect network-ssid password "network-password"

.. code-block:: 
    
    ssh -D 9999 -q -C -N user@raspberrypi.local

* :code:`-D 9999`: open a SOCKS proxy on local port 9999
* :code:`-C`: compress data in the tunnel, save bandwidth
* :code:`-q`: quiet mode, don’t output anything locally
* :code:`-N`: do not execute remote commands, useful for just forwarding ports
* :code:`user@raspberrypi.local`: the remote SSH server you have access to
