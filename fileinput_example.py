"""
file for fileinput
"""
import fileinput

for line in fileinput.input():   # input file by argument
    print(fileinput.filename(), '|', 'Line Number:',
          fileinput.lineno(), '|: ', line)
