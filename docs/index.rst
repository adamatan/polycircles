.. Polycircles documentation master file, created by
   sphinx-quickstart on Mon Apr 21 13:22:59 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Polycircles's documentation!
=======================================

In short: Fake KML circles using accurate Polygons.

Basic example
-------------

.. code:: python

	from polycircles import polycircles

	polycircle = polycircles.Polycircle(latitude=40.768085,
	                                    longitude=-73.981885,
	                                    radius=200,
	                                    number_of_vertices=36)
	kml = simplekml.Kml()
	pol = kml.newpolygon(name="Columbus Circle, Manhattan",
						 outerboundaryis=polycircle.to_kml())
	pol.style.polystyle.color = \
		simplekml.Color.changealphaint(200, simplekml.Color.green)
	kml.save("test_kml_polygon_3_manhattan.kml")


.. image:: _static/kml_manhattan.png
   :height: 300 px
   :alt: Polygon circle in Google Earth. Image Credit: Google
   :align: center

Polycircles is a Pythonic tool for creating accurate Polygonic approximations of circles on a WGS-84 earth grid.

.. image:: _static/kml_manhattan.png
   :height: 300 px
   :alt: Polygon circle in Google Earth. Image Credit: Google
   :align: center

.. image:: _static/kml_namibia.png
   :alt: Polygon circle in Google Earth. Image Credit: Google
   :align: center

.. image:: _static/kml_rio.png
   :height: 300 px
   :alt: Polygon circle in Google Earth. Image Credit: Google
   :align: center
Contents:

.. toctree::
   :maxdepth: 2

Simple example
--------------




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

