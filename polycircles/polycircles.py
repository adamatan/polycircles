from geographiclib import geodesic

def circle(latitude, longitude, radius, number_of_vertices):

    # Value assertions
    if number_of_vertices < 3:
        raise ValueError("The minimal number of vertices in a polygon is 3.")
    if radius <= 0:
        raise ValueError("Radius can only have positive values.")
    if not (-180 <= longitude <= 180):
        raise ValueError("Longitude must be between -180 and 180 degrees.")
    if not (-90 <= latitude <= 90):
        raise ValueError("Latitude must be between -90 and 90 degrees.")

    # Vertices calculation
    vertices = []
    for i in range(number_of_vertices):
        degree = 360.0/number_of_vertices*i
        vertex = geodesic.Geodesic.WGS84.Direct(latitude, longitude,
                                                degree, radius)
        vertices.append((vertex['lat2'], vertex['lon2']))
    return vertices
