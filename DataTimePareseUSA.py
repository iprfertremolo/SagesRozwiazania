"""
* Assignment: Datetime Parse US
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Given `DATA` is in long US date and time format
    3. Define `a: datetime` with converted `DATA` to `datetime` object
    4. Define `b: str` with converted `a` to `1961-04-12 06:07` format
    4. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Dana `DATA` jest w długim formacie amerykańskim
    3. Zdefiniuj `a: datetime` z przekonwertowaną `DATA` do obiektu `datetime`
    4. Zdefiniuj `b: str` z przekonwertowaną `a` do formatu `1961-04-12 06:07`
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> assert type(a) is datetime, \
    'Variable `a` has invalid type, must be a datetime'

    >>> assert type(b) is str, \
    'Variable `b` has invalid type, must be a str'

    >>> a
    datetime.datetime(1961, 4, 12, 6, 7)

    >>> b
    '1961-04-12 06:07'
"""


# Given
from datetime import datetime


DATA = 'April 12, 1961 6:07 local time'

a = ...  # datetime: representing DATA
b = ...  # str: `a` formatted as '1961-04-12 06:07'

a = datetime(1961, 4, 12, 6, 7)
b = a.strftime('%Y-%m-%d %H:%M')