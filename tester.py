from urlcompleter import URLCompleter

comp = URLCompleter()

print(comp.complete('example.com', 'path', 'another_path', 'file.html'))
