import os
import simplekml
from polycircles.polycircles import Polycircle

polycircle = Polycircle(latitude=31.611878, longitude=34.505351, radius=1500)
print(polycircle.to_lat_lon())
kml = simplekml.Kml()

for i, vertex in enumerate(polycircle):
    if i == len(polycircle.to_lat_lon())-1:
        break
    print(i, vertex)
    current_polygon = Polycircle(latitude=vertex['lat'], longitude=vertex['lon'], radius=100, number_of_vertices=i+3)
    pol = kml.newpolygon(name=f"polygon-{i}", outerboundaryis=current_polygon.to_kml())
    pol.style.polystyle.color = simplekml.Color.changealphaint(200, simplekml.Color.green)
kml.save(os.path.join('.', "test_kml_polygon_1.kml"))
