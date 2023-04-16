Direct Cosine Matrix
====================

2D Rotatin Matrix
-----------------
.. math::

   \begin{bmatrix}
   \cos(\theta) && \sin(\theta)\\
   -\sin(\theta) && \cos(\theta)
   \end{bmatrix}
   = 
   \begin{bmatrix}
   \cos(\pi/4) && \sin(\pi/4)\\
   -\sin(\pi/4) && \cos(\pi/4)
   \end{bmatrix}
   = 
   \begin{bmatrix}
   \sqrt{2}/2 && \sqrt{2}/2\\
   -\sqrt{2}/2 && \sqrt{2}/2
   \end{bmatrix}

.. math:: 
   \begin{bmatrix}
    x\\
    y
    \end{bmatrix}
   = R    \begin{bmatrix}
    1\\
    1
    \end{bmatrix}
   =     \begin{bmatrix}
    \sqrt{2}/2 && \sqrt{2}/2\\
    -\sqrt{2}/2 && \sqrt{2}/2
    \end{bmatrix}
    \begin{bmatrix}
        1\\
        1
        \end{bmatrix}
   =
        \begin{bmatrix}
            \sqrt{2}\\
            0
            \end{bmatrix}

3D Rotation Matrix
------------------

.. math:: 

   R &= R_z(\gamma) R_y(\beta) R_x(\alpha) \\
   &=
   \begin{bmatrix}
      \cos(\gamma) && -\sin(\gamma) && 0\\
      \sin(\gamma) && \cos(\gamma) && 0\\
      0 && 0 && 1
   \end{bmatrix}
   \begin{bmatrix}
      \cos(\beta) && 0 && \sin(\beta) \\
      0 && 1 && 0\\
      -\sin(\beta) && 0 && \cos(\beta)
   \end{bmatrix}
   \begin{bmatrix}
      1 && 0 && 0 \\
      0 && \cos(\alpha) && -\sin(\alpha) \\
      0 && \sin(\alpha) && \cos(\alpha)
   \end{bmatrix}

Gimbal Lock
-----------

.. math:: 
   R &= R_z(\alpha) R_y(\beta) R_x(\gamma) \\
   &=
   \begin{bmatrix}
      \cos(\alpha) && -\sin(\alpha) && 0\\
      \sin(\alpha) && \cos(\alpha) && 0\\
      0 && 0 && 1
   \end{bmatrix}
   \begin{bmatrix}
      \cos(\beta) && 0 && \sin(\beta) \\
      0 && 1 && 0\\
      -\sin(\beta) && 0 && \cos(\beta)
   \end{bmatrix}
   \begin{bmatrix}
      1 && 0 && 0 \\
      0 && \cos(\gamma) && -\sin(\gamma) \\
      0 && \sin(\gamma) && \cos(\gamma)
   \end{bmatrix}\\
   &=
   \begin{bmatrix}
      \cos(\alpha) && -\sin(\alpha) && 0\\
      \sin(\alpha) && \cos(\alpha) && 0\\
      0 && 0 && 1
   \end{bmatrix}
   \begin{bmatrix}
      0 && 0 && 1 \\
      0 && 1 && 0\\
      -1 && 0 && 0
   \end{bmatrix}
   \begin{bmatrix}
      1 && 0 && 0 \\
      0 && \cos(\gamma) && -\sin(\gamma) \\
      0 && \sin(\gamma) && \cos(\gamma)
   \end{bmatrix}\\
   &=
   =
   \begin{bmatrix}
      0 && 0 && 1 \\
      \sin(\alpha+\gamma) && \cos(\alpha+\gamma) && 0\\
      -\cos(\alpha+\gamma) && \sin(\alpha+\gamma) && 1
   \end{bmatrix}