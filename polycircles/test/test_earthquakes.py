import os, csv
from nose.tools import assert_equal
from polycircles import polycircles
import simplekml
import unittest


class TestLastPointInPolygonEqualsTheFirstOne(unittest.TestCase):
    """
    Courtesy Carlos H. Grohmann (https://github.com/CarlosGrohmann) who
    reported Issue #1 (https://github.com/adamatan/polycircles/issues/1).

    In KML, the first point of the polygon should be equal to the last point
    of the polygon in order to properly create a closed polygon, without
    a missing vertex.

    Therefore, a Polycircle called with number_of_vertices=N
    will have N+1 vertices, where vertices[0] == vertices[N].

    BTW, This is cool - this project is used to map earthquakes!
    """

    def setUp(self):
        csvfile = 'polycircles/test/sismos_continente2.csv'
        output_dir = 'kmls'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        with open(csvfile) as f:
            datafile = csv.reader(f, delimiter=',')
            quakelist = list(datafile)
        kml = simplekml.Kml()
        alpha = 100
        self.polycircles = []
        self.number_of_vertices = 36

        for quake in quakelist[1:]:
            lng = float(quake[0]) # X
            lat = float(quake[1]) # Y
            yyyy = quake[2] # Ano
            magw = quake[25] # mag_03

            polycircle = polycircles.Polycircle(
                latitude=lat,
                longitude=lng,
                radius=40000,
                number_of_vertices=self.number_of_vertices)
            self.polycircles.append(polycircle)
            pol = kml.newpolygon(name=yyyy, outerboundaryis=polycircle.to_kml())

            if float(magw) < 3.0:
                pol.style.polystyle.color = simplekml.Color.changealphaint(alpha, simplekml.Color.lightyellow)
                pol.style.linestyle.color = simplekml.Color.lightyellow
            elif 3.0 < float(magw) < 3.5:
                pol.style.polystyle.color = simplekml.Color.changealphaint(alpha, simplekml.Color.yellow)
                pol.style.linestyle.color = simplekml.Color.yellow
            elif 3.5 < float(magw) < 4.0:
                pol.style.polystyle.color = simplekml.Color.changealphaint(alpha, simplekml.Color.orangered)
                pol.style.linestyle.color = simplekml.Color.orangered
            else:
                pol.style.polystyle.color = simplekml.Color.changealphaint(alpha, simplekml.Color.red)
                pol.style.linestyle.color = simplekml.Color.red

        kml.save(os.path.join(output_dir, 'sismos.kml'))

    def test_number_of_vertices(self):
        """The number of vertices in the Polycircle should equal (number_of_vertices+1).
        This test verifies that all the points representations (wkt, kml, lat-lon, lon-lat)
        have the same number of points, equal to number_of_vertices+1."""
        for polycircle in self.polycircles:
            lat_lons = polycircle.to_lat_lon()
            lon_lats = polycircle.to_lon_lat()
            points = [p for p in polycircle]
            wkt = polycircle.to_wkt().split(',')
            kml = polycircle.to_kml()

            assert_equal(len(lat_lons), self.number_of_vertices + 1)
            assert_equal(len(lon_lats), self.number_of_vertices + 1)
            assert_equal(len(points), self.number_of_vertices + 1)
            assert_equal(len(wkt), self.number_of_vertices + 1)
            assert_equal(len(kml), self.number_of_vertices + 1)

