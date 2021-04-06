# polycircles

WGS84 Circle approximations using polygons for KMLs.

[![Build Status](https://github.com/adamatan/polycircles/actions/workflows/test.yaml/badge.svg)](https://github.com/adamatan/polycircles/actions)
[![Latest Version](https://pypip.in/version/polycircles/badge.png)](https://pypi.python.org/pypi/polycircles/)
[![License](https://pypip.in/license/polycircles/badge.png)](https://pypi.python.org/pypi/polycircles/)
[![Downloads](https://pypip.in/download/polycircles/badge.png)](https://pypi.python.org/pypi/polycircles/)


## Installing

```bash
pip install polycircles
```
## Create a polygon

```python
import os
from polycircles.polycircles import Polycircle

polycircle = Polycircle(latitude=31.611878, longitude=34.505351, radius=1500)
print(polycircle)
```

Should print its [WKT](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) representation:

```bash
POLYGON ((34.505351 31.625406, 34.508096 31.625201, 34.510758 31.624590...
```

## A KML circle

Generates a circle and use [simpleKML](https://pypi.org/project/simplekml/) to generate a KML file.

```python
import simplekml
from polycircles.polycircles import Polycircle

polycircle = Polycircle(latitude=40.768085,
                        longitude=-73.981885,
                        radius=200,
                        number_of_vertices=36)
kml = simplekml.Kml()
pol = kml.newpolygon(name="Columbus Circle, Manhattan", outerboundaryis=polycircle.to_kml())
pol.style.polystyle.color = simplekml.Color.changealphaint(200, simplekml.Color.green)

kml.save("02.kml")
```

![Manhattan example](https://raw.githubusercontent.com/adamatan/polycircles/master/docs/_static/kml_manhattan.png)
