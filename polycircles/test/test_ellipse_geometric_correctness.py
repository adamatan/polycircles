'''
Created on Apr 30, 2021

@author: John Klapp
'''


import unittest
from polycircles import polycircles
from nose.tools import assert_equal, assert_almost_equal, assert_greater_equal
from geopy.distance import vincenty
from geographiclib import geodesic

class TestGeometry(unittest.TestCase):

    def setUp(self):
        self.latitude = 32.074322
        self.longitude = 34.792081
        self.semi_major = 1000
        self.semi_minor = 100
        self.orientation = 0
        self.number_of_vertices = 36
        polycircle = polycircles.Polyellipse(latitude=self.latitude,
                                           longitude=self.longitude,
                                           semimajor=self.semi_major,
                                           semiminor=self.semi_minor,
                                           orientation=self.orientation,
                                           number_of_vertices=self.number_of_vertices)

        self.vertices = polycircle.to_lat_lon()

    def test_number_of_vertices(self):
        """Does the number of vertices in the circle match the input+1?
        The +1 is because the first vertex should be appended to the internal
        list of vertices to properly "close" a polygon in KML.
        Asserts that the number of vertices in the approximation polygon
        matches the input."""
        assert_equal(len(self.vertices), self.number_of_vertices+1)

    def test_vertices_distance_from_center(self):
        """Does the distance of the vertices equals the input radius?
        Asserts that the distance from each vertex to the center of the
        circle equals the radius, in 5 decimal digits accuracy."""
        for vertex in self.vertices:
            actual_distance = vincenty((self.latitude, self.longitude), (vertex[0], vertex[1])).meters
            assert_greater_equal(actual_distance, self.semi_minor)
            assert_greater_equal(self.semi_major, actual_distance)

    def test_azimuth_of_vertices(self):
        """Is the azimuth (bearing) to each vertex correct?
        Asserts that for n vertices, the bearing to vertex number 0 <= i <= n
        is 360/n*i."""
        relative_azimuth = [geodesic.Geodesic.WGS84.Inverse(self.latitude, self.longitude, vertex[0], vertex[1])-self.orientation for vertex in self.vertices]
        for i in range(1,len(self.vertices)):
            assert_greater_equal(relative_azimuth[i], relative_azimuth[i-1])

if __name__ == '__main__':
    unittest.main(verbose=2)