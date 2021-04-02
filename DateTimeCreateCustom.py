"""
* Assignment: Datetime Create Custom
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. First human (Yuri Gagarin) flown to space on
       April 12th, 1961 at 6:07 a.m. from Bajkonur Cosmodrome in Kazahstan
    2. Create `date` object representing date of the launch
    3. Create `time` object representing time of the launch
    4. Combine date and time into `datetime` object representing
       exact moment of the launch

Polish:
    1. Pierwszy czÅ‚owiek (Juri Gagarin) poleciaÅ‚ w kosmos
       12 kwietnia 1961 roku o 6:07 rano z kosmodromu Bajkonur w Kazachstanie
    1. StwÃ³rz obiekt `date` reprezentujÄ…cy datÄ™ startu
    2. StwÃ³rz obiekt `time` reprezentujÄ…cy czas startu
    3. PoÅ‚Ä…Ä‡Å¼ datÄ™ i czas w obiekt `datetime` reprezentujÄ…cy
       dokÅ‚adny moment startu

Tests:
    >>> assert type(dt) is datetime, \
    'Variable `dt` has invalid type, must be a datetime'

    >>> assert type(d) is date, \
    'Variable `dt` has invalid type, must be a date'

    >>> assert type(t) is time, \
    'Variable `t` has invalid type, must be a time'

    >>> str(d)
    '1961-04-12'
    >>> str(t)
    '06:07:00'
    >>> str(dt)
    '1961-04-12 06:07:00'
"""


# Given
from datetime import datetime, date, time


d = ...  # date: representing April 12th, 1961 6:07 a.m.
t = ...  # time: representing April 12th, 1961 6:07 a.m.
dt = ...  # datetime: representing April 12th, 1961 6:07 a.m.


# Solution
d = date(1961, 4, 12)
t = time(6, 7, 0)
dt = datetime(1961, 4, 12, 6, 7, 0)