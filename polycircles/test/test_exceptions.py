import unittest
from polycircles import polycircles
from nose.tools import raises

class TestExceptions(unittest.TestCase):
    """Tests that the right exceptions are raised for erroneous inputs."""

    @raises(ValueError)
    def test_less_than_3_vertices_no_1(self):
        polycircle = polycircles.Polycircle(latitude=30,
                                           longitude=30,
                                           radius=100,
                                           number_of_vertices=2)

    @raises(ValueError)
    def test_less_than_3_vertices_no_2(self):
        polycircle = polycircles.Polycircle(latitude=30,
                                           longitude=30,
                                           radius=100,
                                           number_of_vertices=-3)

    @raises(ValueError)
    def test_less_than_3_vertices_no_3(self):
        polycircle = polycircles.Polycircle(latitude=30,
                                           longitude=30,
                                           radius=100,
                                           number_of_vertices=0)

    @raises(ValueError)
    def test_erroneous_latitude_1(self):
        polycircle = polycircles.Polycircle(latitude=-100,
                                            longitude=30,
                                            radius=100)

    @raises(ValueError)
    def test_erroneous_latitude_2(self):
        polycircle = polycircles.Polycircle(latitude=100,
                                            longitude=30,
                                            radius=100)

    @raises(ValueError)
    def test_erroneous_latitude_3(self):
        polycircle = polycircles.Polycircle(latitude=200,
                                            longitude=30,
                                            radius=100)
    @raises(ValueError)
    def test_erroneous_longitude_1(self):
        polycircle = polycircles.Polycircle(latitude=30,
                                            longitude=-200,
                                            radius=100)

    @raises(ValueError)
    def test_erroneous_longitude_2(self):
        polycircle = polycircles.Polycircle(latitude=30,
                                            longitude=200,
                                            radius=100)

if __name__ == '__main__':
    unittest.main(verbose=2)