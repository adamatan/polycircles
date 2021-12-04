from geographiclib import geodesic

DEFAULT_NUMBER_OF_VERTICES = 36


class Shape(object):
    """Common operations for shapes"""

    def to_lat_lon(self):
        """Returns a tuple of (lat, lon) tuples of the polygon."""
        return self.vertices

    def to_kml(self):
        """Returns a tuple of (lon, lat) tuples suitable for a KML polygon."""
        return self.to_lon_lat()

    def to_wkt(self):
        """Returns a WKT (Well Known Text) representation of the polygon. Note
           that WKT tuples are (lon, lat), not (lat, lon)."""
        vertices = ", ".join(["%f %f" % v for v in self.to_lon_lat()])
        return "POLYGON ((%s))" % vertices

    def to_lon_lat(self):
        """Returns a tuple of (lon, lat) tuples of the polygon.
           The (lon, lat) notation is used in KMLs and WKTs."""
        return tuple(v[::-1] for v in self.vertices)

    def __iter__(self):
        return iter([{'lat': p[0], 'lon': p[1], 'index': self.vertices.index(p)} for p in self.vertices])

    def __str__(self):
        return self.to_wkt()


class Polycircle(Shape):
    """A polygonial approximation of a circle in WGS84 coordinates.

    >>> import polycircles
    >>> number_of_vertices = 20
    >>> polycircle = polycircles.Polycircle(latitude=31.611878, longitude=34.505351, radius=100, number_of_vertices=number_of_vertices)
    >>> len(polycircle.to_lat_lon()) == number_of_vertices + 1
    True
    """

    def __init__(self, latitude, longitude, radius, number_of_vertices=DEFAULT_NUMBER_OF_VERTICES):
        """
        Arguments:
        latitude -- WGS84 latitude, between -90.0 and 90.0.
        longitude -- WGS84 longitude, between -180.0 and 180.0.
        radius -- Circle radius in meters.
        number_of_vertices -- Number of vertices for the approximation
        polygon.
        """
        # Value assertions
        assert number_of_vertices >= 3, "The minimal number of vertices in a polygon is 3."
        assert radius > 0, "Radius can only have positive values."
        assert -180 <= longitude <= 180, "Longitude must be between -180 and 180 degrees."
        assert -90 <= latitude <= 90, "Latitude must be between -90 and 90 degrees."

        self.latitude = latitude
        self.longitude = longitude
        self.radius = radius
        self.number_of_vertices = number_of_vertices

        vertices = []
        for i in range(self.number_of_vertices):
            bearing = 360.0 / self.number_of_vertices * i # turn around center point

            # allow longitude unroll: longitudes will extend beyond +-180 if necessary
            # (for circles that cross the antimeridian)
            #
            # concerning polar latitudes/circles that overlap poles:
            # Google Earth has known issues with polygons that contain poles, linestring are ok
            vertex = geodesic.Geodesic.WGS84.Direct(self.latitude, self.longitude, bearing, self.radius,
                                                    geodesic.GeodesicCapability.STANDARD | geodesic.GeodesicCapability.LONG_UNROLL)
            lat = vertex['lat2']
            lon = vertex['lon2']
            vertices.append((lat, lon))
        vertices.append(vertices[0]) # its a closed figure
        self.vertices = tuple(vertices)
