import fileinput

for line in fileinput.input():
    print(fileinput.filename(), '|', 'Line Number:',
          fileinput.lineno(), '|: ', line)
