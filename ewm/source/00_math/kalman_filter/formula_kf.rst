=====================
Kalman Filter Formula
=====================

1. The dynamic system is given by the following equations:

.. math:: 

    x_k &= F_{k-1}x_{k-1} + G_{k-1}u_{k-1} + w_{k-1} \\
    y_k &= H_k x_k + v_k \\
    E(w_k w_j^T) &= Q_k \delta_{k-j} \\
    E(v_k v_j^T) &= R_k \delta_{k-j} \\
    E(w_k j_j^T) &= 0

where

* :math:`w_k` and :math:`v_k` are white, zero-mean, uncorrelated, and have known covariance matrix :math:`Q_k` and :math:`R_k`

2. The Kalman filter is initialized as follows:

.. math::

    \hat{x}_0^+ &= E(x_0) \\
    P_0^+ &= E[(x_0 - \hat{x}_0^+)(x_0 - \hat{x}_0^+)^T]

3. The Kalman filter is given by the following equations, which are computed for each time step k=1,2,...

.. math::

    \hat{x}_k^- &= F_{k-1}\hat{x}_{k-1}^+ + G_{k-1}u_{k-1}  &= \textnormal{a priori state estimate} \\
    P_k^- &= F_{k-1}P_{k-1}^+F_{k-1}^T + Q_{k-1}            & \\
    K_k &= P_k^-H_k^T(H_kP_k^-H_k^T + R_k)^{-1}             & \\
    \hat{x}_k^+ &= \hat{x}_k^- + K(y_k - H_k\hat{x}_k^-)    &= \textnormal{a posteriori state estimate} \\
    P_k^+ &= (I-K_k H_k)P_k^-(I-K_k H_k)^T + K_kR_kK_k^T    & \\
    &= [(P_k^-)^{-1} + H_kR_kH_k^T]^{-1}                    & \\
    &= (I - K_kH_k)P_k^-                                    &
