from polycircles import polycircles

@given('A polycircle class with center at {latitude}, {longitude} with a radius of {radius} meters and {num_vertices} vertices')
def step_impl(context, latitude, longitude, radius, num_vertices):
    context.latitude = latitude
    context.longitude = longitude
    context.radius = radius
    context.num_vertices = num_vertices

@when('then class is initialized')
def step_impl(context):
    context.polycircle = \
        polycircles.Polycircle(float(context.latitude),
                               float(context.longitude),
                               float(context.radius),
                               int(context.num_vertices))

@then('the distance from the center to each vertex is 100, up to 5 decimal digits')
def step_impl(context):
    for vertex in context.polycircle.to_lat_lon():
        print(vertex)
        assert False
