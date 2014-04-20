Feature: A geometrically correct polycircle

Scenario Outline: A Polycircle whose vertices have the correct distance from the center

  Given A polycircle class with center at <latitude>, <longitude> with a radius of <radius> meters and <num_vertices> vertices
  When then class is initialized
  Then the distance from the center to each vertex is <radius>, up to 5 decimal digits

  Examples:
  | latitude     | longitude    | radius     | num_vertices  |
  | 32.074322    | 34.792081    | 100        | 36            |