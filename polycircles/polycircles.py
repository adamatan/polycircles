from geographiclib import geodesic


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

    Usage example:

    >>> c=polycircles.Polycircle(latitude=31.830039, longitude=35.071912, radius=100)
    >>> c.to_lat_lon()
    ((31.83094084460926, 35.071912), (31.830910114707777, 35.07218540190941), (31.830820019253167, 35.07244017141744), (31.83067669825975, 35.07265894602757), (31.830489919032214, 35.07282681647418), (31.83027241048205, 35.07293234280127), (31.830038995615485, 35.07296833393961), (31.82980558132776, 35.07293233766568), (31.829588074359023, 35.07282680757908), (31.829401297291742, 35.07265893575638), (31.82925797845859, 35.07244016252233), (31.829167884585402, 35.07218539677381), (31.829137155262753, 35.071912), (31.829167884585402, 35.071638603226184), (31.82925797845859, 35.07138383747767), (31.829401297291742, 35.071165064243615), (31.829588074359023, 35.07099719242092), (31.82980558132776, 35.07089166233432), (31.830038995615485, 35.07085566606038), (31.83027241048205, 35.07089165719872), (31.830489919032214, 35.07099718352581), (31.83067669825975, 35.07116505397242), (31.830820019253167, 35.071383828582555), (31.830910114707777, 35.07163859809059))
    >>> c.to_wkt()
    'POLYGON ((35.071912 31.830941, 35.072185 31.830910, 35.072440 31.830820, 35.072659 31.830677, 35.072827 31.830490, 35.072932 31.830272, 35.072968 31.830039, 35.072932 31.829806, 35.072827 31.829588, 35.072659 31.829401, 35.072440 31.829258, 35.072185 31.829168, 35.071912 31.829137, 35.071639 31.829168, 35.071384 31.829258, 35.071165 31.829401, 35.070997 31.829588, 35.070892 31.829806, 35.070856 31.830039, 35.070892 31.830272, 35.070997 31.830490, 35.071165 31.830677, 35.071384 31.830820, 35.071639 31.830910))'
    >>> c.to_kml()
    ((35.071912, 31.83094084460926), (35.07218540190941, 31.830910114707777), (35.07244017141744, 31.830820019253167), (35.07265894602757, 31.83067669825975), (35.07282681647418, 31.830489919032214), (35.07293234280127, 31.83027241048205), (35.07296833393961, 31.830038995615485), (35.07293233766568, 31.82980558132776), (35.07282680757908, 31.829588074359023), (35.07265893575638, 31.829401297291742), (35.07244016252233, 31.82925797845859), (35.07218539677381, 31.829167884585402), (35.071912, 31.829137155262753), (35.071638603226184, 31.829167884585402), (35.07138383747767, 31.82925797845859), (35.071165064243615, 31.829401297291742), (35.07099719242092, 31.829588074359023), (35.07089166233432, 31.82980558132776), (35.07085566606038, 31.830038995615485), (35.07089165719872, 31.83027241048205), (35.07099718352581, 31.830489919032214), (35.07116505397242, 31.83067669825975), (35.071383828582555, 31.830820019253167), (35.07163859809059, 31.830910114707777))
    """

    def __init__(self, latitude, longitude, radius, number_of_vertices=36):
        """
        Arguments:
        latitude -- WGS84 latitude, between -90.0 and 90.0.
        longitude -- WGS84 longitude, between -180.0 and 180.0.
        radius -- Circle radius in meters.
        number_of_vertices -- Number of vertices for the approximation
        polygon.
        """
        # Value assertions
        if number_of_vertices < 3:
            raise ValueError("The minimal number of vertices in a "
                             "polygon is 3.")
        if radius <= 0:
            raise ValueError("Radius can only have positive values.")
        if not (-180 <= longitude <= 180):
            raise ValueError("Longitude must be between -180 and 180 degrees.")
        if not (-90 <= latitude <= 90):
            raise ValueError("Latitude must be between -90 and 90 degrees.")

        self.latitude = latitude
        self.longitude = longitude
        self.radius = radius
        self.number_of_vertices = number_of_vertices

        vertices = []
        for i in range(number_of_vertices):
            degree = 360.0/number_of_vertices*i
            vertex = geodesic.Geodesic.WGS84.Direct(latitude, longitude,
                                                    degree, radius)
            vertices.append((vertex['lat2'], vertex['lon2']))
        vertices.append(vertices[0])
        self.vertices = tuple(vertices)

