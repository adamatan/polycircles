import os
import unittest
from polycircles import polycircles
import simplekml
from geographiclib import geodesic

class TestKMLs(unittest.TestCase):
    """Tests the KML representation of the Polycircles using the simplekml
    package."""

    def setUp(self):
        self.output_dir = 'polycircles/test/kmls'
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)


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
        kml.save(os.path.join(self.output_dir, "test_kml_polygon_1.kml"))

    def test_kml_polygon_2(self):
        """Creates a torus-shaped polygon."""
        outer_polycircle = polycircles.Polycircle(latitude=40.768085,
                                                  longitude=-73.981885,
                                                  radius=200,
                                                  number_of_vertices=36)
        inner_polycircle = polycircles.Polycircle(latitude=40.768085,
                                                  longitude=-73.981885,
                                                  radius=180,
                                                  number_of_vertices=36)

        kml = simplekml.Kml()
        pol = kml.newpolygon(name="Torus around Columbus Circle, Manhattan",
                             outerboundaryis=outer_polycircle.to_kml(),
                             innerboundaryis=inner_polycircle.to_kml())
        pol.style.polystyle.color = \
            simplekml.Color.changealphaint(200, simplekml.Color.red)
        kml.save(os.path.join(self.output_dir, "test_kml_polygon_2_torus_manhattan.kml"))

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
        kml.save(os.path.join(self.output_dir, "test_kml_polygon_3_manhattan.kml"))

    def test_kml_polygons_4_multiple_vertices(self):
        """Creates polycircles with a varying amount of vertices."""
        start_lat = -24.336113
        start_lon = 14.976681

        direct = geodesic.Geodesic.WGS84.Direct
        kml = simplekml.Kml()

        for row in range(6):
            row_start = direct(start_lat, start_lon, 180, 100*row)
            row_start_lat, row_start_lon = row_start['lat2'], row_start['lon2']
            for column in range(6):
                circle_center = direct(row_start_lat, row_start_lon,
                                       90, 100*column)
                circle_center_lat = circle_center['lat2']
                circle_center_lon = circle_center['lon2']
                number_of_vertices = (row*6)+column+3
                polycircle = polycircles.Polycircle(circle_center_lat,
                                                    circle_center_lon,
                                                    40, number_of_vertices)
                pol = kml.newpolygon(name="%d vertices" % number_of_vertices,
                                     outerboundaryis=polycircle.to_kml())
                pol.style.polystyle.color = \
                    simplekml.Color.changealphaint(200,
                                                   simplekml.Color.aquamarine)
                kml.save(os.path.join(self.output_dir, "test_kml_multiple_vertices.kml"))


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

        kml.save(os.path.join(self.output_dir, "test_olympic_bagels_2.kml"))

if __name__ == '__main__':
    unittest.main()