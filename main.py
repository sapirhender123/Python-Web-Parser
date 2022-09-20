import urllib.request
from bs4 import BeautifulSoup as bs
import os
import urllib
import xlsxwriter

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

INDEX_TACTIC = 9
def create_html(link, name_for_html):
    urllib.request.urlretrieve(link, name_for_html)

'''
def read_html():
    fp = urllib.request.urlopen("http://www.python.org")
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()
'''


def find_specific_tag_in_html(html_name, specific_tag):
    file = open(html_name, encoding="utf8")
    soup_file = bs(file, 'html.parser')
    return soup_file.findAll(specific_tag)


def find_another_attr():
    find_specific_tag_in_html('tr')


def get_links_and_ids(html_name):
    urls = []
    ids = []
    desire_tags = find_specific_tag_in_html(html_name, 'td')

    for item in desire_tags:
        children = item.findChildren()
        # print(item['id'])
        ids.append(item['id'])
        for child in children:
            # print(child['href'])
            urls.append(child['href'])
    return urls, ids


'''
# return the 
∙	TTP ID [String] 
∙	TTP Name [String] 
∙	Tactic [String] 
∙	Description [String] 
∙	Mitigations [List of String, separated by comma]
'''


def parse_link(html_file):
    pass


def create_excel_file(input_dict):
    workbook = xlsxwriter.Workbook('Result.xlsx')
    bold = workbook.add_format({'bold': True})
    worksheet = workbook.add_worksheet()
    col = 0
    for key, value in input_dict.items():
        width = max([len(x) for x in value])
        width = max([width, len(key)]) + 5

        worksheet.write(0, col, key, bold)
        worksheet.write_column(1, col, value)
        worksheet.set_column(col, col, width)
        col += 1

    workbook.close()


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
res_links, res_ids = get_links_and_ids('ATT&CK.html')

names = []
tactics = []
descriptions = []
for _link in res_links:
    name = 'temp.html'
    print("looking now at link: https://collaborate.mitre.org/" + _link)
    create_html('https://collaborate.mitre.org/' + _link, name)

    # create parser
    soup = bs(name, 'html.parser')

    # find name
    list_of_details_for_name = find_specific_tag_in_html(name, "tbody")[0].findChildren()
    names.append(list_of_details_for_name[0].text)

    a = list_of_details_for_name[10].text
    b = find_specific_tag_in_html(name, "table")

    # find tactic
    tactic = find_specific_tag_in_html(name, "tbody")[0].findChildren()[INDEX_TACTIC]
    tactics.append(tactic)

    # find description
    description = find_specific_tag_in_html(name, "p")[1].text
    descriptions.append(description)

    # find Mitigations
    # mitigations = find_specific_tag_in_html(name, "ul")
    # mitigations = soup.find_all("div", {"class": "mw-parser-output"})

    os.remove(name)
