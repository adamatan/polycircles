import os
import simplekml
from polycircles.polycircles import Polycircle


polycircle = Polycircle(latitude=31.611878, longitude=34.505351, radius=100)
kml = simplekml.Kml()

pol = kml.newpolygon(name=f"Polycircle", outerboundaryis=polycircle.to_kml())
kml.save('02.kml')