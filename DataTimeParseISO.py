"""
* Assignment: Datetime Parse ISO
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Given `DATA` is in ISO format
    3. Define `a: datetime` with converted `DATA` to `datetime` object
    4. Define `b: str` with converted `a` to to ISO format
    4. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Dana `DATA` jest w formacie ISO
    3. Zdefiniuj `a: datetime` z przekonwertowaną `DATA` do obiektu `datetime`
    4. Zdefiniuj `b: str` z przekonwertowaną `a` do formatu ISO
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> assert type(a) is datetime, \
    'Variable `a` has invalid type, must be a datetime'

    >>> assert type(b) is str, \
    'Variable `b` has invalid type, must be a str'

    >>> a
    datetime.datetime(1969, 7, 21, 2, 56, 15, 123000)

    >>> b
    '1969-07-21T02:56:15.123000'
"""


# Given
from datetime import datetime


DATA = '1969-07-21T02:56:15.123'

a = ...  # datetime: representing DATA
b = ...  # str: `a` formatted as '1969-07-21T02:56:15.123000'

a = datetime(1969, 7, 21, 2, 56, 15, 123000)
b = a.strftime('%Y-%m-%dT%H:%M:%S.%f')