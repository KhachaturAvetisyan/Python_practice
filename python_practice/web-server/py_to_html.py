from yattag import Doc

doc, tag, text = Doc().tagtext()

with tag('html'):
    with tag('body'):
        with tag('table'):
            for i in range(1, 11):
                with tag('tr'):
                    for j in range(1, 11):
                        with tag('td'):
                            num = i * j
                            with tag('a', href=f" http://{num}.ru"):
                                text(num)

with open("index.html", "w") as fd:
    fd.write(doc.getvalue())