"""
* Assignment: Type Int Time
* Complexity: easy
* Lines of code: 12 lines
* Time: 8 min

English:
    1. Calculate how many seconds is one day (24 hours)
    2. Calculate how many minutes is one week (7 days)
    3. Calculate how many hours is in one month (31 days)
    4. Calculate how many seconds is work day (8 hours)
    5. Calculate how many minutes is work week (5 work days)
    6. Calculate how many hours is work month (22 work days)
    7. In Calculations use floordiv (`//`)
    8. Compare result with "Tests" section (see below)

Polish:
    1. Oblicz ile sekund to jedna doba (24 godziny)
    2. Oblicz ile minut to jeden tydzień (7 dni)
    3. Oblicz ile godzin to jeden miesiąc (31 dni)
    4. Oblicz ile sekund to dzień pracy (8 godzin)
    5. Oblicz ile minut to tydzień pracy (5 dni pracy)
    6. Oblicz ile godzin to miesiąc pracy (22 dni pracy)
    7. W obliczeniach użyj floordiv (`//`)
    8. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> type(day)
    <class 'int'>
    >>> type(week)
    <class 'int'>
    >>> type(month)
    <class 'int'>
    >>> type(workday)
    <class 'int'>
    >>> type(workweek)
    <class 'int'>
    >>> type(workmonth)
    <class 'int'>
    >>> day
    86400
    >>> week
    10080
    >>> month
    744
    >>> workday
    28800
    >>> workweek
    2400
    >>> workmonth
    176
"""

# Given
SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR

day = ...  # 1 day in seconds
week = ...  # 7 days in minutes
month = ...  # 31 days in hours
workday = ...  # 8 hours in seconds
workweek = ...  # 5 workdays in minutes
workmonth = ...  # 22 workdays in hours

day = DAY * SECOND
week = int((7 * DAY) / MINUTE)
month = int((31 * DAY) / HOUR)
workday = 8 * HOUR * SECOND
workweek = int((5 * workday) / MINUTE)
workmonth = int((22 * workday) / HOUR)