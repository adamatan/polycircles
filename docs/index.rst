Welcome to Polycircles documentation!
=====================================

Generates accurate polygonal approximation of circles, for KMLs and general usage.

.. toctree::
   :maxdepth: 2

Basic usage
-----------

Generates lat-lon pairs of a polygonal approximation for a circle.

.. code:: python

	>>> import pprint
	>>> from polycircles import polycircles
	>>> polycircle = polycircles.Polycircle(latitude=32.074523,
	                                        longitude=34.791469,
	                                        radius=20,
	                                        number_of_vertices=12)
	>>> pprint.pprint(polycircle.to_lat_lon())
	((32.07470336197859, 34.791469),
	 (32.074679198011374, 34.7915749137218),
	 (32.074613180857156, 34.79165244781555),
	 (32.07452299982296, 34.791680827083454),
	 (32.074432818876005, 34.79165244745541),
	 (32.07436680189626, 34.79157491336165),
	 (32.07434263801628, 34.791469),
	 (32.07436680189626, 34.79136308663835),
	 (32.074432818876005, 34.791285552544586),
	 (32.07452299982296, 34.791257172916545),
	 (32.074613180857156, 34.79128555218445),
	 (32.074679198011374, 34.791363086278196))

KML circles
-----------

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

Adjusting the number of vertices
--------------------------------

Raising the number of vertices makes the polygon illusion more compelling.
On the other side, too many vertices make the KML file larger and Google Earth slower.

In my opinion, 36 edges are the right balance between appearances and file size.

.. image:: _static/kml_namibia.png
   :alt: Polygon circle in Google Earth. Image Credit: Google
   :align: center

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

