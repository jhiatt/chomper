import time
import pandas as pd

## SAHPES
border = ('|' * 110)

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

cl = "     |   -  |"

top = "      _____\n     /      \\"

# breaking into two rows
top1 = "      _____"

top2 = "     /      \\"

bottom = "     \\      /\n      _____"

# breaking into two rows
bottom1 = "     \\      /"
bottom2 = "      _____"

eyes = "    ()      ()"

# expanding mouth
mt = "     |   ⁔  |"

mc = "     |  | | |"

mb = "     |   ‿  |"

# BIG THING
r1 = "__________________________"
r2 = "| _______________________ |"
rm = "||                       ||"

# BURP
burp = """
                  _______________
                 |               |
                 |  B U R P !!!  |
                 |_______________|
                ∠
"""

## FUNCTIONS
def top_border():
    for i in range(100):
        print(border)

# Open and close mouth
for h in range (30):
    top_border()

    print("\n" + eyes + "\n" + top + "\n" + (op if h%2 else cl) + " -" * (30 - h) + "\n" + bottom + "\n")

    for j in range(10):
        print(border)
    time.sleep(.1)

# move up
rg = range(15)
for h in rg:
    top_border()

    # use the h index to alternate open and closed
    print("\n" + eyes + "       - - " + "\n" + top + "    - - " + "\n" + (op + " - - " if h%2 else cl) + "\n" + bottom + "\n")

    for j in range(9 + h):
        print(border)
    time.sleep(.1)

# level off
for h in range (20):
    top_border()

    print("\n" + eyes + "\n" + top + "\n" + (op if h%2 else cl) + " -" * (20 - h) + "\n" + bottom + "\n")

    for j in range(len(rg)+10):
        print(border)
    time.sleep(.1)

# move down
rg_dwn = range(20)
for h in rg_dwn:
    top_border()

    print("\n" + eyes + "\n" + top + "\n" + (op if h%2 else cl) + " -" * 2 + "\n" + bottom + "       - -" +  "\n")

    for j in range(len(rg)+12 - h):
        print(border)
    time.sleep(.1)

# level off
for h in range (20):
    top_border()

    print("\n" + eyes + "\n" + top + "\n" + (op if h%2 else cl) + " -" * (19 - h) + "\n" + bottom + "\n")

    for j in range(len(rg)+ 9 - len(rg_dwn)):
        print(border)
    time.sleep(.1)

# BIG BITE
# intro
rg_big = range(70)
for h in rg_big:
    spacing = " " * (len(rg_big)-h + len(eyes)) # added length of eyes so there's no pause at the end
    top_border()

    # pause amount
    p = 30
    if (h<p):
        print(
            spacing + r1 + "\n" + spacing + r2 + "\n" + (spacing + rm + "\n") * (17) + 
            eyes + " " * (len(spacing) -len(eyes)) + rm + "\n" + 
            top1 + " " * (len(spacing) -len(top1)) + rm + "\n" + 
            top2 + " " * (len(spacing) -len(top2)) + rm + "\n" + 
            op + " " * (len(spacing) -len(op)) + rm + "\n" +
            bottom1 + " " * (len(spacing) -len(bottom1)) + r2 + "\n" +
            bottom2 + " " * (len(spacing) -len(bottom2)) + r1 + "\n"
            )

        # bottom border        
        for j in range(len(rg)+ 9 - len(rg_dwn)):
            print(border)

    # create the opening mouth
    elif (h<16+p):
        mouth_mid = ""
        for j in range(h-p):
            mouth_mid += mc + " " * (len(spacing) -len(mt)) + rm + "\n"
        print(
            spacing + r1 + "\n" + spacing + r2 + "\n" + (spacing + rm + "\n") * (16-h+p) + 
            eyes + " " * (len(spacing) -len(eyes)) + rm + "\n" + 
            top1 + " " * (len(spacing) -len(top1)) + rm + "\n" + 
            top2 + " " * (len(spacing) -len(top2)) + rm + "\n" + 
            mt + " " * (len(spacing) -len(mt)) + rm + "\n" +
            mouth_mid +
            mb + " " * (len(spacing) -len(mt)) + rm + "\n" + 
            bottom1 + " " * (len(spacing) -len(bottom1)) + r2 + "\n" +
            bottom2 + " " * (len(spacing) -len(bottom2)) + r1 + "\n"
            )
        # bottom border        
        for j in range(len(rg)+ 9 - len(rg_dwn)):
            print(border)

    # lower jaw
    elif (h<20+p):
        mouth_mid = ""
        for j in range(18):
            mouth_mid += mc + " " * (len(spacing) -len(mt)) + rm + "\n"
        mouth_mid += mc + " " * (len(spacing) -len(mt)) + r2 + "\n"
        mouth_mid += mc + " " * (len(spacing) -len(mt)) + r1 + "\n"
        print(
            spacing + r1 + "\n" + spacing + r2 + "\n" + (spacing + rm + "\n") * (16-h-p) + 
            eyes + " " * (len(spacing) -len(eyes)) + rm + "\n" + 
            top1 + " " * (len(spacing) -len(top1)) + rm + "\n" + 
            top2 + " " * (len(spacing) -len(top2)) + rm + "\n" + 
            mt + " " * (len(spacing) -len(mt)) + rm + "\n" +
            mouth_mid +
            mb + " " * (len(spacing) -len(mt)) + "\n" + 
            bottom1 + " " * (len(spacing) -len(bottom1)) + "\n" +
            bottom2 + " " * (len(spacing) -len(bottom2)) + "\n"
            )
        # bottom border        
        for j in range(len(rg)+ 7 - len(rg_dwn)):
            print(border)
    # raise jaw
    else:
        mouth_mid = ""
        # for k in range(4)
        mouth_mid += mc + " " * (len(spacing) -len(mt)) + r1 + "\n"
        mouth_mid += mc + " " * (len(spacing) -len(mt)) + r2 + "\n"
        for j in range(21):
            mouth_mid += mc + " " * (len(spacing) -len(mt)) + rm + "\n"
        mouth_mid += mc + " " * (len(spacing) -len(mt)) + r2 + "\n"
        mouth_mid += mc + " " * (len(spacing) -len(mt)) + r1 + "\n"
        print(
            eyes + "\n" +
            top1 + "\n" + 
            top2 + "\n" +
            mt + "\n" +
            mouth_mid +
            mb + "\n" +
            bottom1 + "\n" +
            bottom2 + "\n"
            )
    
        for j in range(len(rg)+ 7 - len(rg_dwn)):
            print(border)

    time.sleep(.1)

#swollow:
rg_sw = range(30)
for h in rg_sw:
        
    top_border()
    r1_s = r1[h:]
    r2_s = r2[h:]
    rm_s = rm[h:]

    mouth_mid = ""
    # for k in range(4)
    mouth_mid += mc + " " * (len(spacing) -len(mt)) + r1_s + "\n"
    mouth_mid += mc + " " * (len(spacing) -len(mt)) + r2_s + "\n"
    for j in range(21):
        mouth_mid += mc + " " * (len(spacing) -len(mt)) + rm_s + "\n"
    mouth_mid += mc + " " * (len(spacing) -len(mt)) + r2_s + "\n"
    mouth_mid += mc + " " * (len(spacing) -len(mt)) + r1_s + "\n"
    print(
        eyes + "\n" +
        top1 + "\n" + 
        top2 + "\n" +
        mt + "\n" +
        mouth_mid +
        mb + "\n" +
        bottom1 + "\n" +
        bottom2 + "\n"
        )

    for j in range(len(rg)+ 7 - len(rg_dwn)):
        print(border)
    time.sleep(.1)

#close
rg_sw = range(20)
for h in rg_sw:
        
    top_border()
 
    print(
        eyes + "\n" +
        top1 + "\n" + 
        top2 + "\n" +
        cl + "\n" +
        bottom1 + "\n" +
        bottom2 + "\n"
        )

    for j in range(len(rg)+ 7 - len(rg_dwn)):
        print(border)
    time.sleep(.1)

#burp 
for i in range(100):
    print(border)

print(
    burp + "\n" +
    eyes + "\n" +
    top1 + "\n" + 
    top2 + "\n" +
    op + "\n" +
    bottom1 + "\n" +
    bottom2 + "\n"
    )

for j in range(len(rg)+ 7 - len(rg_dwn)):
    print(border)
