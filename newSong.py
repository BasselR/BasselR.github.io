### newSong.py ###

# Run this script with one CLA: the name of the song you wish to add (without extension).
# i.e: python newSong.py song
# ^ This will add song.wav to your index.html file for basselr.github.io

import os
import sys
from datetime import date

name = sys.argv[1]

today = date.today()
d = today.strftime("%y.%m.%d")

with open('index.html', 'r') as old, open('tmp.txt', 'w') as new:

    lines = old.readlines()

    for line in lines:
        if "<table>" in line:
            new.write(line)
            new.write("\n    <tr>\n\t\t<td>%s</td>\n\t\t<td><A class='fresh' HREF='songs/%s.wav'>%s</A></td>\n    </tr>\n" % (d, name, name))
        else:
            new.write(line)

os.rename("tmp.txt", "index.html")