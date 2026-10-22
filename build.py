import pathlib
s = pathlib.Path("index.html").read_text()
d = pathlib.Path("data.js").read_text()
inlined = s.replace('<script src="data.js"></script>', "<script>\n" + d + "\n</script>")
# Artifact version: the host adds the document skeleton.
pathlib.Path("iraq-fault-lines.html").write_text(inlined)
# GitHub Pages version: a complete standalone document.
head = '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n<meta name="description" content="Interactive web and timeline of the people and events behind the Iraq War, 1951 to 2011, with stakeholder motives and a primary source on every blurb.">\n'
body = inlined.replace("</style>", "</style>\n</head>\n<body>", 1) + "\n</body>\n</html>\n"
docs = pathlib.Path("docs"); docs.mkdir(exist_ok=True)
(docs / "index.html").write_text(head + body)
