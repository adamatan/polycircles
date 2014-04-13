import unittest
from polycircles import polycircles

import geopy

class TestPolycircles(unittest.TestCase):

    def test_number_of_vertices(self):
        vertices = polycircles.circle(latitude=32.074322, longitude=34.792081,
                     radius=100, number_of_vertices=36)
        print(dir(geopy))
        print(geopy.__path__)
        #unittest.ass

if __name__ == '__main__':
    unittest.main()