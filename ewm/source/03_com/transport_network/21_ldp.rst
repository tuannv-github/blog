===
LDP
===

.. image:: imgs/fib-lfib-cisco.png

.. image:: imgs/mpls-ldp-multicast-unicast.png

.. image:: imgs/ldp3.jpg

The two routers above will send multicast hello packets on their FastEthernet interfaces. Within this hello packet, they will advertise a **transport IP address**. This IP address is then used to establish the TCP connection between the two routers.

OSPF vs LDP Adjacency 
=====================

.. image:: imgs/ospf-two-neighbor-adjacencies.png

.. image:: imgs/ldp-single-neighbor-adjacency.png

.. image:: imgs/458.png

LDP Packets
===========

.. image:: imgs/mpls_headerlabel_01.gif

.. image:: imgs/mpls-ldp-hello-packet.png

.. image:: imgs/MPLS_Header_color.JPG
