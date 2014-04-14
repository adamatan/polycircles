import unittest
from polycircles import polycircles
from nose.tools import assert_equal, assert_almost_equal
from geopy.distance import vincenty
from geographiclib import geodesic

class TestPolycircles(unittest.TestCase):

    def setUp(self):
        self.latitude = 32.074322
        self.longitude = 34.792081
        self.radius_meters = 100
        self.number_of_vertices = 36
        self.vertices = polycircles.circle(latitude=self.latitude,
                                           longitude=self.longitude,
                                           radius=self.radius_meters,
                                           number_of_vertices=self.number_of_vertices)

    def test_number_of_vertices(self):
        """Does the number of vertices in the circle match the input?
        Asserts that the number of vertices in the approximation polygon
        matches the input."""
        assert_equal(len(self.vertices), self.number_of_vertices)

    def test_vertices_distance_from_center(self):
        """Does the distance of the vertices equals the input radius?
        Asserts that the distance from each vertex to the center of the
        circle equals the radius, in 5 decimal digits accuracy."""
        for vertex in self.vertices:
            actual_distance = vincenty((self.latitude, self.longitude), (vertex[0], vertex[1])).meters
            assert_almost_equal(actual_distance, self.radius_meters, 5)

    def test_azimuth_of_vertices(self):
        """Is the azimuth (bearing) to each vertex correct?
        Asserts that for n vertices, the bearing to vertex number 0 <= i <= n
        is 360/n*i."""
        for vertex in self.vertices:
            vertex_number = self.vertices.index(vertex)
            expected_azimuth = 360.0/len(self.vertices) * vertex_number
            actual_azimuth = (geodesic.Geodesic.WGS84.Inverse(
                self.latitude, self.longitude, vertex[0], vertex[1]))['azi1']

            if actual_azimuth < 0:
                actual_azimuth = 360.0 + actual_azimuth

            assert_almost_equal(expected_azimuth, actual_azimuth, places=5)

if __name__ == '__main__':
    unittest.main()