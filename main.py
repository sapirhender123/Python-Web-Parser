
import urllib.request
from bs4 import BeautifulSoup as bs
import os
import urllib
'''
fp = urllib.request.urlopen("https://collaborate.mitre.org/attackics/index.php/Main_Page")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

print(mystr)


base=os.path.dirname(os.path.abspath('main.py'))
# open the HTML file
#html=open(os.path.join(base, 'ATT&CK.html'))


'''


def create_html(link, name):
    urllib.request.urlretrieve(link, name)


def get_links(html_name):
    urls = []
    file = open(html_name, encoding="utf8")
    soup = bs(file, 'html.parser')
    desire_links = soup.findAll('td')
    for link in desire_links:
        children = link.findChildren()
        print(link)
        for child in children:
            #print(child['href'])
            print(child)
            urls.append(child['href'])
    return urls

'''
# return the 
∙	TTP ID [String] 
∙	TTP Name [String] 
∙	Tactic [String] 
∙	Description [String] 
∙	Mitigations [List of String, separated by comma]
'''
def parse_link():
    pass


def write_to_excel():
    pass

'''
links = soup.findAll('a', href=True)
for link in links:
    urls.append(link['href'])
#print(urls)



unordered_list=soup.find("div",
      {"class":"matrix_container"})
for child in unordered_list.children:
    print (child)
children = unordered_list.findChildren()
for child in children:
    print (child)
    '''

create_html("https://collaborate.mitre.org/attackics/index.php/Main_Page", "ATT&CK.html")
get_links('ATT&CK.html')
