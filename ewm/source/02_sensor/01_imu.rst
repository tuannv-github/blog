===
IMU
===

State vector
============

One define INS state vector :math:`x_I(t)` at time :math:`t` as:

.. math:: 
    x_I(t) = 
    \begin{bmatrix}
    {^I_G}\bar{q}(t)\\
    {^G}\mathbf{p}_I(t)\\
    {^G}\mathbf{v}_I(t)\\
    \mathbf{b}_g(t)\\
    \mathbf{b}_a(t)\\
    \end{bmatrix}

where

* :math:`{^I_G}\bar{q}(t)` is the unit  quaternion representing the rotation of global frame to IMU frame.
* :math:`{^G}\mathbf{p}_I(t)` is the position of IMU in global frame.
* :math:`{^G}\mathbf{v}_I(t)` is the velocity of IMU in global frame.
* :math:`\mathbf{b}_g(t)` is the gyroscope bias.
* :math:`\mathbf{b}_a(t)` is the accelerometer bias.

IMU Kinematics
==============

.. math:: 
    {^I_G}\dot{\bar{q}}(t) &= \frac{1}{2} 
    \begin{bmatrix}
    -\omega(t) & w(t) \\
    -\omega^T(t) & 0 
    \end{bmatrix} {^{I_t}_G}\bar{q}
    \\
    &= \frac{1}{2} \Omega(\omega(t)) {^{I_t}_G}\bar{q} \\
    {^G}\dot{\mathbf{p}}_I(t) &= {^G}\mathbf{v}_I(t) \\
    {^G}\dot{\mathbf{v}}_I(t) &= {^{I_t}_G}R^T \mathbf{a}(t) \\
    \dot{\mathbf{b}}_g(t) & = \mathbf{n}_{\omega g}\\
    \dot{\mathbf{b}}_a(t) & = \mathbf{n}_{\omega a}


Discrete-time IMU propagation
=============================

.. math:: 
    {^{I_{k+1}}_G}\hat{\bar{q}} &= \exp \left(\frac{1}{2}\Omega(\omega_{m,k}-\hat{\mathbf{b}}_{g,k})\Delta t\right) {^{I_k}_G}\hat{\bar{q}} \\
    {^G}\hat{\mathbf{v}}_{I_{k+1}} &= {^G}\hat{\mathbf{v}}_{I_k} + {^{I_k}_G}\hat{\mathbf{R}}^T(\mathbf{a}_{m,k} - \hat{\mathbf{b}}_{a,k})\Delta t - {^G}\mathbf{g}\Delta t \\
    {^G}\hat{\mathbf{p}}_{I_{k+1}} &= {^G}\hat{\mathbf{p}}_{I_{k}} + {^G}\hat{\mathbf{v}}_{I_{k}} \Delta t + \frac{1}{2}{^{I_k}_G}\hat{\mathbf{R}}^T(\mathbf{a}_{m,k} - \hat{\mathbf{b}}_{a,k})\Delta t ^2 - \frac{1}{2} {^G}\mathbf{g}\Delta t ^2 \\
    \hat{\mathbf{b}}_{g, k+1} &= \hat{\mathbf{b}}_{g, k}\\
    \hat{\mathbf{b}}_{a, k+1} &= \hat{\mathbf{b}}_{a, k}

Discrete-time Error-state propagation
=====================================

.. math:: 
    P_{k+1|k} = \Phi(t_{k+1}, t_k)P_{k|k}\Phi(t_{k+1}, t_k)^T + G_kQ_dG_k^T

where

.. math:: 
    \Phi(t_{k+1}, t_k) = 
    \begin{bmatrix}
    {^{I_{k+1}}_{I_k}}\hat{\mathbf{R}} & 0_3 & 0_3 & - {^{I_{k+1}}_{I_k}}\hat{\mathbf{R}}\mathbf{J}_r({^{I_{k+1}}_{I_k}}\hat{\theta}) \Delta t & 0_3 \\
    -\frac{1}{2} {^{I_k}_G}\hat{\mathbf{R}}^T \lfloor \hat{\mathbf{a}}_k\Delta t^2 \times \rfloor & \mathbf{I}_3 & \Delta t \mathbf{I}_3 & 0_3 & -\frac{1}{2} {^{I_k}_G} \hat{\mathbf{R}}^T \Delta t^2\\
    -{^{I_k}_G}\hat{\mathbf{R}}^T \lfloor \hat{\mathbf{a}}_k\Delta t \rfloor& 0_3 & \mathbf{I}_3 & 0_3 & {^{I_k}_G}\hat{\mathbf{R}}^T \Delta t^2\\
    0_3 & 0_3 & 0_3 & \mathbf{I}_3 & 0_3\\
    0_3 & 0_3 & 0_3 & 0_3 & \mathbf{I}_3
    \end{bmatrix}

.. math:: 
    \mathbf{G}_k = 
    \begin{bmatrix}
    - {^{I_{k+1}}_{I_k}}\hat{\mathbf{R}}\mathbf{J}_r({^{I_{k+1}}_{I_k}}\hat{\theta}) \Delta t & 0_3 & 0_3 & 0_3 \\
    0_3 & -\frac{1}{2} {^{I_k}_G}\hat{\mathbf{R}}^T \Delta t^2 & 0_3 & 0_3 \\
    0_3 & -{^{I_k}_G}\hat{\mathbf{R}}^T \Delta t & 0_3 & 0_3 \\
    0_3 & 0_3 & \mathbf{I}_3 & 0_3\\
    0_3 & 0_3 & 0_3 & \mathbf{I}_3\\
    \end{bmatrix}

Link: https://docs.openvins.com/propagation.html
