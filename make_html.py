import os

from GETREADME import main


main("2", "1")

os.popen("pandoc python-cheatsheet.md -t html -o python-cheatsheet.html")

with open("python-cheatsheet.html", "r", encoding="utf-8") as f:
    data = f.read()
os.remove("python-cheatsheet.html")

before = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>python-cheatsheet by pynickle</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='index.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='github.css') }}">
    <script src="{{ url_for('static', filename='highlight.pack.js') }}"></script>
    <script>hljs.initHighlightingOnLoad();</script>
</head>
<body>
"""

after = """
</body>
</html>
"""

data = before + data + after

with open("./web/templates/python-cheatsheet.html", "w", encoding="utf-8") as f:
    f.write(data)