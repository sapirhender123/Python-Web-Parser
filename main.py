
import urllib.request
from bs4 import BeautifulSoup as bs
import os
import urllib

fp = urllib.request.urlopen("https://collaborate.mitre.org/attackics/index.php/Main_Page")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

print(mystr)

urllib.request.urlretrieve("https://collaborate.mitre.org/attackics/index.php/Main_Page", "ATT&CK.html")
base=os.path.dirname(os.path.abspath('main.py'))
# open the HTML file
html=open(os.path.join(base, 'ATT&CK.html'))
