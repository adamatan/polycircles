import unittest
from polycircles import polycircles
from nose.tools import assert_equal, assert_almost_equal, assert_is_not_none
import simplekml

class TestGeometry(unittest.TestCase):
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
        outer_polycircle = polycircles.Polycircle(latitude=32.0746,
                                                  longitude=34.791469,
                                                  radius=20,
                                                  number_of_vertices=36)
        inner_polycircle = polycircles.Polycircle(latitude=32.0746,
                                                  longitude=34.791469,
                                                  radius=16,
                                                  number_of_vertices=36)

        kml = simplekml.Kml()
        pol = kml.newpolygon(name="Azrieli towers",
                             outerboundaryis=outer_polycircle.to_kml(),
                             innerboundaryis=inner_polycircle.to_kml())
        pol.style.polystyle.color = \
            simplekml.Color.changealphaint(200, simplekml.Color.red)
        kml.save("test_kml_polygon_2.kml")


if __name__ == '__main__':
    unittest.main()