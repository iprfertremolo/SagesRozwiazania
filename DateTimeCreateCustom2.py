"""
* Assignment: Datetime Create Current
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Create `date` object with current date
    2. Create `datetime` object with current date and time
    3. Create `time` object with current time
    4. Date and time must be from system, not hardcoded in code

Polish:
    1. Stwórz obiekt `date` z obecną datą
    2. Stwórz obiekt `datetime` z obecną datą i czasem
    3. Stwórz obiekt `time` z obecnym czasem
    4. Data i czas ma być pobierana z systemu, nie zapisana w kodzie

Tests:
    >>> assert type(dt) is datetime, \
    'Variable `dt` has invalid type, must be a datetime'

    >>> assert type(d) is date, \
    'Variable `dt` has invalid type, must be a date'

    >>> assert type(t) is time, \
    'Variable `t` has invalid type, must be a time'
"""


# Given
from datetime import datetime, date, time


dt = ...  # datetime: representing current moment
d = ...  # date: representing current moment
t = ...  # time: representing current moment

dt = datetime.now()
d = date.today()
t = time()