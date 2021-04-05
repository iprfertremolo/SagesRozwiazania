"""
* Assignment: Type Bool Simple
* Complexity: easy
* Lines of code: 9 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. What you need to put in expressions to get the expected outcome?
    3. In place of ellipsis (`...`) insert only `True` or `False`
    4. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Co należy podstawić w wyrażeniach aby otrzymać wartość oczekiwaną?
    3. W miejsce trzech kropek (`...`) wstawiaj tylko `True` lub `False`
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> bool(a)
    True
    >>> bool(b)
    True
    >>> bool(c)
    False
    >>> bool(d)
    True
    >>> bool(e)
    True
    >>> bool(f)
    False
    >>> bool(g)
    True
    >>> bool(h)
    True
    >>> bool(i)
    False
"""

# Given
a = True == True  # True
b = True != False  # True
c = not True  # False
d = bool(True) == True  # True
e = bool(False) == False  # True
f = False or False  # False
g = True and True  # True
h = bool(bool(True) == False) or True  # True
i = bool(False) is not bool(False)  # False