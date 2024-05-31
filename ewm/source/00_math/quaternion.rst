Quaternion
==========

Intro
=====

Number system - Hệ thống số
----------------------------

* Natural Number - Số tự nhiên
* Integer - Số Nguyên
* Decimal - Số thập phân
* Complex Number - Số phức
* Quaternion

.. math:: 
    \vec{u} &= (u_x, u_y, u_z) = u_x \mathbf{i} + u_y \mathbf{j} + u_z \mathbf{k}\\
    \mathbf{q} &= e^{\frac{\theta}{2}(u_x \mathbf{i} + u_y \mathbf{j} + u_z \mathbf{k})}
    = 
    \cos \frac{\theta}{2} + (u_x \mathbf{i} + u_y \mathbf{j} + u_z \mathbf{k}) \sin \frac{\theta}{2}\\
    \mathbf{p}' &=\mathbf{q}\mathbf{p}\mathbf{q}^{-1}

.. math:: 
    \mathbf{i}^2 &= \mathbf{j} ^ 2 = \mathbf{k}^2 = \mathbf{i} \mathbf{j} \mathbf{k} &= -1\\
    \mathbf{i}\mathbf{j} &= -\mathbf{j}\mathbf{i} = \mathbf{k}\\
    \mathbf{j}\mathbf{k} &= -\mathbf{k}\mathbf{j} = \mathbf{i}\\
    \mathbf{k}\mathbf{i} &= -\mathbf{i}\mathbf{k} = \mathbf{j}\\

Ví dụ
------

Cho điểm :math:`A(1,1)` trong hệ tọa độ :math:`Oxy`.

Hệ tọa độ :math:`Ox'y'` có được bằng cách xoay hệ tọa độ :math:`Oxy` một góc :math:`\frac
{-\pi}{4}`.

Tính tọa độ của :math:`A` trong :math:`Ox'y'`?

.. math:: 
    A' &= \left(\cos \frac{\pi}{8} + k \sin \frac{\pi}{8}\right)  (i+j) \left(\cos \frac{\pi}{8} + k \sin \frac{\pi}{8}\right)^{-1} \\
    &= (a + bk)  (i + j) (a - bk)\\
    &= (ai + aj + bki + bkj ) (a-bk)\\
    &= (ai + aj + bj - bi ) (a-bk)\\
    &= [(a-b)i + (a+b)j] (a-bk)\\
    &= a(a-b)i + a(a+b)j - b(a-b)ik - b(a+b)jk \\
    &= a(a-b)i + a(a+b)j + b(a-b)j - b(a+b)i \\
    &= (a^2-2ab-b^2)i + (a^2+2ab-b^2)j \\
    &= \left( \cos \frac{\pi}{4} - sin \frac{\pi}{4} \right) i + \left( \cos \frac{\pi}{4} + sin \frac{\pi}{4} \right) j \\
    &= \sqrt{2} j

Matlab:

.. code-block:: matlab

    q = quaternion(cos(pi/8),0,0,sin(pi/8));
    A = quaternion(0, 1, 1, 0);
    A_prime = q * A * quatinv(q);
    disp(A_prime);
    0 - 1.1102e-16i +     1.4142j +          0k

Link: https://danceswithcode.net/engineeringnotes/quaternions/quaternions.html

Quaternion operations
=====================

Quaternion and 3D Rotation
==========================

Quaternion-derived Rotation Matrix
==================================

A quaternion rotation :math:`\mathbf{p}' = \mathbf{q}\mathbf{p}\mathbf{q}^{-1}` with :math:`\mathbf{q} = q_r + q_i \mathbf{i} + q_j \mathbf{j} + q_k`