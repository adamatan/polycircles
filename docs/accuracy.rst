.. _accuracy:

Accuracy
========

Distance accuracy
-----------------

Polycircle uses Python's `geographiclib`_ for distance calculations.

+------------------------+--------------------+
| Method                 | Accuracy           |
+========================+====================+
| Simple trigonometry    | Dozens of meters   |
+------------------------+--------------------+
| `geographiclib`_       | 10^-4 meters       |
+------------------------+--------------------+

The distance was measured by `geopy`_.

.. _geographiclib : https://pypi.python.org/pypi/geographiclib
.. _geopy : http://geopy.readthedocs.org/en/latest/


How many vertices?
------------------

Raising the number of vertices makes the polygon illusion more compelling.
On the other side, too many vertices make the KML file larger and Google Earth slower.

In my opinion, 36 edges are the right balance between appearances and file size.

.. figure:: _static/kml_namibia.png
   :width: 600 px
   :alt: A Polycircle above The Namibian desert, Namibia. Image: Google Earth, Credit: `Google`_
   :align: center

   A Polycircle above The Namibian desert, Namibia.

   Image: Google Earth, Credit: `Google`_

   .. _Google : http://www.google.com/permissions/geoguidelines/attr-guide.html



