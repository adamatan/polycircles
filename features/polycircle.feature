Feature: A geometrically correct polycircle

Scenario Outline: A Polycircle whose vertices have the correct distance from the center

  Given A polycircle class with center in "<location>" at (<latitude>, <longitude>) with a radius of <radius> meters and <num_vertices> vertices
  When then class is initialized
  Then the distance (meters) of each vertex from the center is <radius>, up to 4 decimal places
  And each vertex is aligned in a correct azimuth (degrees), up to 5 decimal places

  Examples:
  | location                         | latitude     | longitude    | radius     | num_vertices  |
  | Azrieli Center, Tel Aviv, Israel | 32.074322    | 34.792081    | 100        | 36            |
  | Azrieli Center, Tel Aviv, Israel | 32.074322    | 34.792081    | 100        | 100           |
  | Azrieli Center, Tel Aviv, Israel | 32.074322    | 34.792081    | 1          | 100           |
  | Azrieli Center, Tel Aviv, Israel | 32.074322    | 34.792081    | 0.2        | 100           |
  | Azrieli Center, Tel Aviv, Israel | 32.074322    | 34.792081    | 0.2        | 1000          |
  | Azrieli Center, Tel Aviv, Israel | 32.074322    | 34.792081    | 0.2        | 3600          |
  | Longyearbyen, Svalbard, Norway   | 78.216667    | 15.55        | 0.1        | 36            |
  | Longyearbyen, Svalbard, Norway   | 78.216667    | 15.55        | 1          | 36            |
  | Longyearbyen, Svalbard, Norway   | 78.216667    | 15.55        | 10         | 36            |
  | Longyearbyen, Svalbard, Norway   | 78.216667    | 15.55        | 100        | 36            |
  | Longyearbyen, Svalbard, Norway   | 78.216667    | 15.55        | 200000     | 36            |
  | Longyearbyen, Svalbard, Norway   | 78.216667    | 15.55        | 100        | 360           |
  | Longyearbyen, Svalbard, Norway   | 78.216667    | 15.55        | 100        | 3600          |
  | Longyearbyen, Svalbard, Norway   | 78.216667    | 15.55        | 100        | 36            |
  | Longyearbyen, Svalbard, Norway   | 78.216667    | 15.55        | 200000     | 3600          |