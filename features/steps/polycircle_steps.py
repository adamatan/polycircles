from polycircles import polycircles
from nose.tools import assert_almost_equal
from geographiclib import geodesic
from geopy.distance import distance as geodesic_distance

@given('A polycircle class with center in "{location}" at ({latitude}, {longitude}) with a radius of {radius} meters and {num_vertices} vertices')
def step_impl(context, location, latitude, longitude, radius, num_vertices):
    context.latitude = float(latitude)
    context.longitude = float(longitude)
    context.radius = float(radius)
    context.num_vertices = int(num_vertices)

@when('then class is initialized')
def step_impl(context):
    context.polycircle = \
        polycircles.Polycircle(float(context.latitude),
                               float(context.longitude),
                               float(context.radius),
                               int(context.num_vertices))

@then('each vertex is aligned in a correct azimuth (degrees), up to {places} decimal places')
def step_impl(context, places):
    vertices = context.polycircle.to_lat_lon()
    for vertex in vertices:
        vertex_number = vertices.index(vertex)
        expected_azimuth = 360.0/(len(vertices) - 1) * vertex_number
        actual_azimuth = (geodesic.Geodesic.WGS84.Inverse(
            context.latitude, context.longitude, vertex[0], vertex[1]))['azi1']

        if actual_azimuth < 0:
            actual_azimuth = 360.0 + actual_azimuth

        assert_almost_equal(expected_azimuth, actual_azimuth, places=int(places))

@then('the distance (meters) of each vertex from the center is {distance}, up to {places} decimal places')
def step_imp(context, distance, places):
    vertices = context.polycircle.to_lat_lon()
    for vertex in vertices:
        actual_distance = geodesic_distance((context.latitude, context.longitude),
                                   (vertex[0], vertex[1])).meters
        assert_almost_equal(actual_distance, float(distance), int(places))