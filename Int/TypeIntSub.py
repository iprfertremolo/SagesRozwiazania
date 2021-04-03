"""
* Assignment: Type Int Sub
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. One Kelvin is equal to 1 Celsius degree (1K = 1°C)
    2. Zero Kelvin (absolute) is equal to -273.15 Celsius degrees
    3. For calculation use round number -273 (0K = -273°C)
    4. How many Celsius degrees has average temperatures at surface [1]:
        a. Lunar day: 453 K
        b. Lunar night: 93 K
    5. Compare result with "Tests" section (see below)

Polish:
    1. Jeden Kelwin to jeden stopień Celsiusza (1K = 1°C)
    2. Zero Kelwina (bezwzględne) to -273.15 stopni Celsiusza
    3. W zadaniu przyjmij równe -273°C (0K = -273°C)
    4. Ile stopni Celsiusza wynoszą średnie temperatury powierzchni [1]:
        a. Księżyca w dzień: 453 K
        b. Księżyca w nocy: 93 K
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

References:
    [1] Centro de Astrobiología (CSIC-INTA).
        Rover Environmental Monitoring Station, Mars Science Laboratory (NASA).
        Year: 2019.
        Retrieved: 2019-08-06.
        URL: http://cab.inta-csic.es/rems/marsweather.html

Tests:
    >>> type(moon_day)
    <class 'int'>
    >>> type(moon_night)
    <class 'int'>
    >>> moon_day
    180
    >>> moon_night
    -180
"""

# Given
Celsius = 1
Kelvin = 273

moon_day = ...  # 453 Kelvins
moon_night = ...  # 93 Kelvins

moon_day = 453 - 273
moon_night = 93 - 273