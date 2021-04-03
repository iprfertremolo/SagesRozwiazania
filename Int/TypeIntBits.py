"""
* Assignment: Type Int Bits
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Calculate altitude in kilometers:
        a. Kármán Line Earth: 100_000 m
        b. Kármán Line Mars: 80_000 m
        c. Kármán Line Venus: 250_000 m
    2. In Calculations use floordiv (`//`)
    3. Compare result with "Tests" section (see below)

Polish:
    1. Oblicz wysokości w kilometrach:
        a. Linia Kármána Ziemia: 100_000 m
        b. Linia Kármána Mars: 80_000 m
        c. Linia Kármána Wenus: 250_000 m
    2. W obliczeniach użyj floordiv (`//`)
    3. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * 1 km = 1000 m

Tests:
    >>> type(karman_line_earth)
    <class 'int'>
    >>> type(karman_line_mars)
    <class 'int'>
    >>> type(karman_line_venus)
    <class 'int'>
    >>> karman_line_earth
    100
    >>> karman_line_mars
    80
    >>> karman_line_venus
    250
"""

# Given
m = 1
km = 1000 * m

karman_line_earth = ...  # 100_000 meters in km
karman_line_mars = ...  # 80_000 meters in km
karman_line_venus = ...  # 250_000 meters in km

karman_line_earth = int(100_000 / km)
karman_line_mars = int(80_000 / km)
karman_line_venus = int(250_000 / km)