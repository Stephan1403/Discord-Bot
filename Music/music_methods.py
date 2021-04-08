import requests
from bs4 import BeautifulSoup
from requests.models import stream_decode_response_unicode

name = "Hallo"
search = ""


while "  " in name:
    name.replace("  ", " ")

for i in name.split(" "):
    search = search + i + "+"



url = f"https://www.youtube.com/results?name_query={search}"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

print(url)




# payload = {'search': 'hallo Welt'}
# r = requests.get("https://www.youtube.com/", params=payload)


#receiving name, returning link
def link_by_name(name):
    pass

