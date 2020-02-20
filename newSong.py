### newSong.py ###

import os
import sys
from datetime import date

name = sys.argv[1]

today = date.today()
d = today.strftime("%y.%m.%d")

with open('index.html', 'r') as old, open('tmp.txt', 'w') as new:

    lines = old.readlines()
    pauseLine = 0

    for num, line in enumerate(lines):
        if "<table>" in line:
            new.write(line)
            new.write("\n    <tr>\n\t\t<td>%s</td>\n\t\t<td><A class='fresh' HREF='songs/%s.wav'>%s</A></td>\n    </tr>\n" % (d, name, name))
        else:
            new.write(line)
            
os.rename("tmp.txt", "index.html")