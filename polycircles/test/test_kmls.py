import unittest
from polycircles import polycircles
import simplekml

class TestKMLs(unittest.TestCase):
    """Tests the KML representation of the Polycircles using the simplekml
    package."""

    def test_kml_polygon_1(self):
        """Asserts that the KML output is valid for the simplekml package."""
        polycircle = polycircles.Polycircle(latitude=32.074523,
                                            longitude=34.791469,
                                            radius=20,
                                            number_of_vertices=36)
        kml = simplekml.Kml()
        pol = kml.newpolygon(name="Azrieli towers",
                             outerboundaryis=polycircle.to_kml())
        pol.style.polystyle.color = \
            simplekml.Color.changealphaint(200, simplekml.Color.green)
        kml.save("test_kml_polygon_1.kml")

    def test_kml_polygon_2(self):
        """Creates a bagel-shaped polygon."""
        outer_polycircle = polycircles.Polycircle(latitude=32.074523,
                                                  longitude=34.792,
                                                  radius=20,
                                                  number_of_vertices=36)
        inner_polycircle = polycircles.Polycircle(latitude=32.074523,
                                                  longitude=34.792,
                                                  radius=16,
                                                  number_of_vertices=36)

        kml = simplekml.Kml()
        pol = kml.newpolygon(name="Azrieli towers",
                             outerboundaryis=outer_polycircle.to_kml(),
                             innerboundaryis=inner_polycircle.to_kml())
        pol.style.polystyle.color = \
            simplekml.Color.changealphaint(200, simplekml.Color.red)
        kml.save("test_kml_polygon_2.kml")

    def test_kml_polygon_3_manhattan(self):
        """Asserts that the KML output is valid for the simplekml package."""
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

    def test_olympic_bagels2(self):
        """Creates bagel-shaped polygons in Rio (just for fun).."""
        circles = ((-22.971499, -43.183030, simplekml.Color.blue),
                    (-22.971498, -43.182737, simplekml.Color.black),
                    (-22.971498, -43.182444, simplekml.Color.red),
                    (-22.971666, -43.182892, simplekml.Color.yellow),
                    (-22.971665, -43.182599, simplekml.Color.green)
        )

        kml = simplekml.Kml()

        for circle in circles:
            outer_polycircle = polycircles.Polycircle(circle[0], circle[1],
                                                      radius=20)
            inner_polycircle = polycircles.Polycircle(circle[0], circle[1],
                                                      radius=16)
            pol = kml.newpolygon(outerboundaryis=outer_polycircle.to_kml(),
                                 innerboundaryis=inner_polycircle.to_kml())
            pol.style.polystyle.color = \
                simplekml.Color.changealphaint(150, circle[2])

        kml.save("test_olympic_bagels_2.kml")

if __name__ == '__main__':
    unittest.main()