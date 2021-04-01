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
