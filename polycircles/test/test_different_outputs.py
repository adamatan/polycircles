import unittest
from polycircles import polycircles
from nose.tools import assert_equal, assert_almost_equal
import re

class TestGeometry(unittest.TestCase):
    """Tests the various output methods: KML style, WKT, lat-lon and lon-lat."""

    def setUp(self):
        self.latitude = 32.074322
        self.longitude = 34.792081
        self.radius_meters = 100
        self.number_of_vertices = 36
        self.polycircle = \
            polycircles.Polycircle(latitude=self.latitude,
                                   longitude=self.longitude,
                                   radius=self.radius_meters,
                                   number_of_vertices=self.number_of_vertices)

    def test_lat_lon_output(self):
        """Asserts that the vertices in the lat-lon output are in the
        right order (lat before long)."""
        for vertex in self.polycircle.to_lat_lon():
            assert_almost_equal(vertex[0], self.latitude, places=2)
            assert_almost_equal(vertex[1], self.longitude, places=2)

    def test_lon_lat_output(self):
        """Asserts that the vertices in the lat-lon output are in the
        right order (lat before long)."""
        for vertex in self.polycircle.to_lon_lat():
            assert_almost_equal(vertex[0], self.longitude, places=2)
            assert_almost_equal(vertex[1], self.latitude, places=2)

    def test_vertices_equals_lat_lon(self):
        """Asserts that the "vertices" property is identical to the return
        value of to_lat_lon()."""
        assert_equal(self.polycircle.vertices, self.polycircle.to_lat_lon())

    def test_kml_equals_lon_lat(self):
        """Asserts that the return value of to_kml() property is identical to
        the return value of to_lon_lat()."""
        assert_equal(self.polycircle.to_kml(), self.polycircle.to_lon_lat())

    def test_wkt_form(self):
        """Asserts that the to_wkt() return value complies with the WKT
        form."""
        assert_equal(self.polycircle.to_kml(), self.polycircle.to_lon_lat())


if __name__ == '__main__':
    unittest.main(verbose=2)