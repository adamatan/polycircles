from polycircles import polycircles
from nose.tools import assert_almost_equal
from geographiclib import geodesic

@given('A polycircle class with center at {latitude}, {longitude} with a radius of {radius} meters and {num_vertices} vertices')
def step_impl(context, latitude, longitude, radius, num_vertices):
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

@then('the distance from the center to each vertex is 100, up to 5 decimal digits')
def step_impl(context):
    #for vertex in context.polycircle.to_lat_lon():
    #    print(vertex)
    #    assert False
    vertices = context.polycircle.to_lat_lon()
    for vertex in vertices:
        vertex_number = vertices.index(vertex)
        expected_azimuth = 360.0/len(vertices) * vertex_number
        actual_azimuth = (geodesic.Geodesic.WGS84.Inverse(
            context.latitude, context.longitude, vertex[0], vertex[1]))['azi1']

        if actual_azimuth < 0:
            actual_azimuth = 360.0 + actual_azimuth

        assert_almost_equal(expected_azimuth, actual_azimuth, places=5)
