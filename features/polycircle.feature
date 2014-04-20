Feature: A geometrically correct polycircle

Scenario Outline: A Polycircle whose vertices have the correct distance from the center

  Given A polycircle class with center in "<location>" at (<latitude>, <longitude>) with a radius of <radius> meters and <num_vertices> vertices
  When then class is initialized
  Then the distance (meters) of each vertex from the center is <radius>, up to 4 decimal places
  And each vertex is aligned in a correct azimuth (degrees), up to 6 decimal places

  Examples:
  | location      | latitude     | longitude    | radius     | num_vertices  |
  | Nataf, Israel | 32.074322    | 34.792081    | 100        | 36            |
  | Nataf, Israel | 32.074322    | 34.792081    | 100        | 100           |
  | Nataf, Israel | 32.074322    | 34.792081    | 1          | 100           |
  | Nataf, Israel | 32.074322    | 34.792081    | 0.2        | 100           |