import os
import simplekml
from polycircles.polycircles import Polycircle


polycircle = Polycircle(latitude=36.46329, longitude=-116.880102, radius=500)
kml = simplekml.Kml()

pol = kml.newpolygon(name=f"Polycircle", outerboundaryis=polycircle.to_kml())
pol.style.polystyle.color = simplekml.Color.changealphaint(200, simplekml.Color.cyan)
kml.save('03.kml')