=============
Linear system
=============

Deterministic linear system can be described by the equations

.. math:: 
    :label: linear_system_equations

    \dot{x} &= Ax + Bu \\
    y &= Cx

where:

* :math:`x` is state vector
* :math:`u` is control vector
* :math:`y` is output vector
* :math:`A` is system matrix
* :math:`B` is input matrix
* :math:`C` is output matrix

If :math:`A`, :math:`B` and :math:`C` are constant, the the solution to Equation
:eq:`linear_system_equations` is given by

.. math:: 
    :label: solution_to_linear_system_equations

    x(t) &= e^{A(t-t_0)}x(t_0) + \int_{t_0}^t e^{A(t-\tau)} B u(\tau) d\tau\\
    y(t) &= Cx(t)

where

* :math:`t_0` is the initial time of the system and is often taken to be 0


Example
-------

.. math::

    \begin{bmatrix}
        \dot{\theta} \\
        \dot{\omega}
    \end{bmatrix}
    &=
    \begin{bmatrix}
        0 & 1 \\
        0 & 0
    \end{bmatrix}
    \begin{bmatrix}
        \theta \\
        \omega
    \end{bmatrix}
    +
    \begin{bmatrix}
        0 \\
        1
    \end{bmatrix}
    u \\
    y &=
    \begin{bmatrix}
        1 & 0
    \end{bmatrix}
    x

where

* :math:`x` is a :math:`2 \times 1` matrix containing the scalars :math:`\theta` and :math:`\omega`