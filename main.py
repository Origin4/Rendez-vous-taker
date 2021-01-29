from urllib.request import urlopen
html = urlopen("http://www.val-de-marne.gouv.fr/").read()
print(html)