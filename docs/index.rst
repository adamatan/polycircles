.. _index:

Welcome to Polycircles documentation!
=====================================

Generates accurate polygonal approximation of circles, for KMLs and general usage.

.. toctree::
   :maxdepth: 2

   installing
   kmls
   accuracy
   development

Installing
----------

.. code:: bash

	pip install polycircles

KML circle
----------

Generates a circle approximation readable by `simpleKML`_.

.. _simpleKML : https://code.google.com/p/simplekml/

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

Note that a polygon with 36 vertices looks pretty much like a circle:

.. image:: _static/kml_manhattan.png
   :height: 300 px
   :alt: Polygon circle in Google Earth. Image Credit: Google
   :align: center

Sequence of lat-lon points
--------------------------

``polycircles`` can simply generate a tuple of lat-lon tuples:

.. code:: python

	import pprint
	from polycircles import polycircles
	polycircle = polycircles.Polycircle(latitude=32.074523,
	                                    longitude=34.791469,
	                                    radius=20,
	                                    number_of_vertices=12)
	pprint.pprint(polycircle.to_lat_lon())
	((32.07470336197859, 34.791469),
	 (32.074679198011374, 34.7915749137218),
     ...
	 (32.074613180857156, 34.79128555218445),
	 (32.074679198011374, 34.791363086278196))
