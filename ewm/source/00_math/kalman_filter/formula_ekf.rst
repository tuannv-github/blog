==============================
Extended Kalman Filter Formula
==============================

1. The system and measurement equations are given as follows:

.. math:: 
    x_k &= f_{k-1}(x_{k-1}, u_{k-1}, w{k-1}) \\
    y_k &= h_k(x_k, v_k) \\
    w_k &\sim (0, Q_k) \\
    v_k &\sim (0, R_k)

2. Initialize the filter as follows:

.. math:: 
    \hat{x}_0^+ = E(x_0) \\
    P_0^+ = E[(x_0 - \hat{x}_0^+)(x_0 - \hat{x}_0^+)^T]

3. For k = 1,2,..., perform the following

a. Compute the following partial derivative matrices:

.. math:: 
    F_{k-1} &= \left.\frac{\partial f_{k-1}}{\partial x}\right|_{x_{k-1}^+} \\
    L_{k-1} &= \left.\frac{\partial f_{k-1}}{\partial w}\right|_{x_{k-1}^+} \\

b. Perform the time update of the state estimate and estimation-error covariance as follows:

.. math:: 
    \hat{x}_{k}^- &= f_{k-1}(x_{k-1}^+, u_{k-1}, 0) \\
    P_k^- &= F_{k-1}P_{k-1}^+F_{k-1}^T + L_{k-1}Q_{k-1}L_{k-1}^T

c. Compute to following partial derivative matrices:

.. math:: 
    H_k &= \left. \frac{\partial h_k}{\partial x} \right|_{\hat{x}_{k}^-}\\
    M_k &= \left. \frac{\partial h_k}{\partial v} \right|_{\hat{x}_{k}^-}

d. Perform the measurement update of the state estimate and estimation-error covariance as follows:

.. math:: 
    K_k &= P_k^-H_k^T (H_kP_k^-H_k^T + M_kR_kM_k^T)^{-1}\\
    \hat{x}_k^+ &= \hat{x}_k^- + K_k[y_k-h_k(\hat{x}_k^-,0)]\\
    P_k^+ &= (I-K_kH_k)P_k^-
