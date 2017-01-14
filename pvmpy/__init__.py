"""
pvmpy: Partial Volume Morphology in Python
==========================================

This library exposes functions for partial volume morphology (PVM),
an extension to binary morphology enabling arbitrary precision [War17]_.

Dependencies
------------

* numpy
* scipy
* scikit-image

References
----------

.. [War17] Warner, J.D. *Partial volume morphology: eliminating precision
   loss in binary morphology.* Proceedings of SPIE Medical Imaging 2017:
   Biomedical Applications in Molecular, Structural, and Functional Imaging.
   2017. DOI:[in print]
"""

__all__ = ['erode_pvm',
           'dilate_pvm',
           'open_pvm',
           'close_pvm',
           # 'tophat_pvm',
           # 'bottomhat_pvm',
           'disk',
           ]

from .base_pvm import erode_pvm, dilate_pvm

from .extended_pvm import open_pvm, close_pvm  #, tophat_pvm, bottomhat_pvm

from .strel_pvm import disk