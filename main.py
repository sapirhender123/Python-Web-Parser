import urllib.request
from bs4 import BeautifulSoup as bs
import os
import urllib
import xlsxwriter
import pandas as pd



INDEX_TACTIC = 9


def create_html(link, name_for_html):
    urllib.request.urlretrieve(link, name_for_html)


def find_specific_tag_in_html(html_name, specific_tag):
    file = open(html_name, encoding="utf8")
    soup_file = bs(file, 'html.parser')
    return soup_file.findAll(specific_tag)


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


def create_excel_file(ids_list, names_list, tactic_list, description_list):
    workbook = xlsxwriter.Workbook("Results.xlsx")
    worksheet = workbook.add_worksheet("namesheet")

    worksheet.write_column('A1', ids_list)
    worksheet.write_column('B1', names_list)
    worksheet.write_column('C1', tactic_list)
    worksheet.write_column('D1', description_list)

    workbook.close()


def find_name(html_name):
    return find_specific_tag_in_html(html_name, "tbody")[0].findChildren()[0].text


def find_tactic(html_name):
    return find_specific_tag_in_html(html_name, "tbody")[0].findChildren()[INDEX_TACTIC].text


def find_description(html_name):
    return find_specific_tag_in_html(html_name, "p")[1].text


def main():
    create_html("https://collaborate.mitre.org/attackics/index.php/Main_Page", "ATT&CK.html")

    # get links and ids from the main link
    res_links, res_ids = get_links_and_ids('ATT&CK.html')

    names = []
    tactics = []
    descriptions = []
    for _link in res_links:
        # create temp file in order to parse it as requested
        name = 'temp.html'

        print("looking now at link: https://collaborate.mitre.org/" + _link)
        create_html('https://collaborate.mitre.org/' + _link, name)

        # create parser
        soup = bs(name, 'html.parser')

        # find name
        names.append(find_name(name))

        # find tactic
        tactics.append(find_tactic(name))

        # find description
        descriptions.append(find_description(name))

        # find Mitigations
        # mitigations = find_specific_tag_in_html(name, "ul")
        # mitigations = soup.find_all("div", {"class": "mw-parser-output"})

        os.remove(name)
    create_excel_file(res_ids, names, tactics, descriptions)


if __name__ == "__main__":
    main()