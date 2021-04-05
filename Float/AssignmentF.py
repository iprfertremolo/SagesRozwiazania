"""
* Assignment: Type Float Pressure
* Complexity: medium
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Operational pressure of EMU spacesuit: 4.3 PSI
    2. Operational pressure of ORLAN spacesuit: 40 kPa
    3. Calculate operational pressure in hPa for EMU
    4. Calculate operational pressure in hPa for Orlan
    5. Results round to one decimal place
    6. Compare result with "Tests" section (see below)

Polish:
    1. Ciśnienie operacyjne skafandra kosmicznego EMU (NASA): 4.3 PSI
    2. Ciśnienie operacyjne skafandra kosmicznego ORLAN (Roscosmos): 40 kPa
    3. Oblicz ciśnienie operacyjne skafandra EMU w hPa
    4. Oblicz ciśnienie operacyjne skafandra Orlan w hPa
    5. Wynik zaokrąglij do jednego miejsca po przecinku
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> type(emu)
    <class 'float'>
    >>> type(orlan)
    <class 'float'>"""
* Assignment: Type Float Percent
* Complexity: medium
* Lines of code: 2 lines
* Time: 3 min

English:
    1. International Standard Atmosphere (ISA) at sea level is 1 ata = 1013.25 hPa
    2. Calculate `pO2` - partial pressure of Oxygen at sea level in hPa
    3. Round result to one decimal place
    4. To calculate partial pressure use ratio (100% is 1013.25 hPa, 20.946% is how many hPa?)
    5. Compare result with "Tests" section (see below)

Polish:
    1. Międzynarodowa standardowa atmosfera (ISA) na poziomie morza wynosi 1 ata = 1013.25 hPa
    2. Oblicz `pO2` - ciśnienie parcjalne tlenu na poziomie morza w hPa
    3. Wynik zaokrąglij do jednego miejsca po przecinku
    4. Aby policzyć ciśnienie parcjalne skorzystaj z proporcji (100% to 1013.25 hPa, 20.946% to ile hPa?)
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * 1 hPa = 100 Pa
    * 1 kPa = 1000 Pa
    * 1 ata = 1013.25 hPa (ISA - International Standard Atmosphere)
    * Atmosphere gas composition:

        * Nitrogen 78.084%
        * Oxygen 20.946%
        * Argon 0.9340%
        * Carbon Dioxide 0.0407%
        * Others 0.001%

Tests:
    >>> type(pO2)
    <class 'float'>
    >>> pO2
    212.2
"""

# Given
PERCENT = 100
Pa = 1
hPa = 100 * Pa
kPa = 1000 * Pa

ata = ...  # Pressure at sea level: 1013.25 hectopascals
O2 = ...  # oxygen: 20.946%
pO2 = ...  # oxygen partial pressure: 20.946% of pressure at sea level

    >>> orlan
    400.0
    >>> emu
    296.5
"""

# Given
Pa = 1
hPa = 100 * Pa
kPa = 1000 * Pa
psi = 6894.757 * Pa

emu = ...  # 4.3 pounds per square inch in pascals
orlan = ...  # 40 kilopascals ins pascals

emu = round((4.3 * psi)/hPa, 1)
orlan = round((40 * hPa)/10, 1)