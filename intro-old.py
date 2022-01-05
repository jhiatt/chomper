import time
import pandas as pd

## SAHPES
border = ('|' * 100)

## CHARACTERS

# OPENING SET
eyes = """
    ()      ()"""

char_top = """
      _____
     /      \\"""

char_bottom = """
     \\      /
      _____
    """

# mouths only
char_op = """
     |   O  |   - - - - - - - - - - - - - - - - - - - - - - - - - - - - """

char_cl = """
     |   -  |  - - - - - - - - - - - - - - - - - - - - - - - - - - - - """

# MOVE UP
op = "     |   O  |"

cl = "     |   -  | "

top = "      _____\n     /      \\"

bottom = "     \\      /\n      _____"

eyes = "    ()      ()"

# Open and close mouth
for h in range (30):
    for i in range(100):
        print(border)

    print(eyes + char_top + (char_op if h%2 else char_cl) + char_bottom)

    for j in range(10):
        print(border)
    time.sleep(.1)

rg = range(15)
for h in rg:
    for i in range(100):
        print(border)

    # use the h index to alternate open and closed
    print("\n" + eyes + "       - - " + "\n" + top + "    - - " + "\n" + (op + " - - " if h%2 else cl) + "\n" + bottom + "\n")

    for j in range(9 + h):
        print(border)
    time.sleep(.1)