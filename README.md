This repository contains code for work done on the Prescribed Ricci Curvature problem in the field of Riemannian Geometry. The write-up is pending, but a link to the ArXiv will be provided when available. My only request if you wish to use this code or use it as a starting place for your own use is that a reference to my work is provided.

There are multiple files in Python that are provided, all of which use Sympy for importing functions and symbols. There are 6 files in Python that are intended to be viewed in order. 
The first file (so17orthonormalbasis.py) finds a basis for so(1,7) and the second file (so17orthocheck.py) runs check to ensure that the basis has the desired structures.
The third file (IntertwiningMap.py) finds intertwining maps between irreducible ad_{g_2} representations in so(1,7) and the fourth file (Intertwinecheck.py) runs checks to ensure that the map found is indeed an intertwining map.
The fifth file (so17Ricci.py) finds the Ricci curvature interms of an arbitary ad_{g_2} invariant inner product and the sixth file (so17RicciCheck.py) runs check to ensure that the Ricci curvature has the properties we expect to be true.


In addition to Python, there is a file from Mathematica. The file from Mathematica (Mathematica for Prescribed Ricci Curvature of SO17_G2.nb) was used to do computations using the Ricci curvature expressions found in the Python code. There, one can find the inputs and outputs that were essential for solving the Prescribed Ricci Curvature problem for SO(1,7)/G_2.
