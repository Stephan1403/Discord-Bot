#alternative webpage https://experience.arcgis.com/experience/478220a4c454480e823b17327b2bf1d4/page/page_1/

from methods import get_tChannel_by_name
from discord import Embed, Colour
import datetime
import requests
from bs4 import BeautifulSoup
from svglib.svglib import svg2rlg

coronaWords = ["!info", "corona", "numbers", "ostallgäu", "show", "update", "info", "covid", "news"]


def getKey(text):
    text = text.lower().replace(" ", "")
    
    if text.startswith("einwohner"):
        return "population"
    if text.startswith("infektionen"):
        return "infections"
    if text.startswith("infektionsrate"):
        return "infectionrate"
    if text.startswith("neuinfektionen"):
        return "new cases"
    if text.startswith("todesfälle"):
        return "deaths"
    if text.startswith("letalitätsrate"):
        return "mortalityrate"
    else:
        return False


headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}

page = requests.get('https://www.corona-in-zahlen.de/landkreise/lk%20ostallg%C3%A4u/', headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

info = {'population': 0, 'infections': 0, 'infectionrate': 0, 'new cases': 0, 'deaths': 0, 'mortalityrate': 0}
content = soup.find('div', class_='row row-cols-1 row-cols-md-3')   #numbers

for card in content.find_all('div', class_='card-body'):
    text = card.find('p', class_='card-text').text  #e.g. population

    title = card.find('p', class_='card-title').text #e.g. 194.000

    key = getKey(text)

    if key: #key isn´t false
        info[key] = title

#Date
curDate = soup.find('span', class_='badge badge-secondary')


#get picture about current situation etc --- https://www.lgl.bayern.de/gesundheit/infektionsschutz/infektionskrankheiten_a_z/coronavirus/karte_coronavirus/

# picture = requests.get('https://www.lgl.bayern.de/gesundheit/infektionsschutz/infektionskrankheiten_a_z/coronavirus/karte_coronavirus/')

# picSoup = BeautifulSoup(picture.content, 'html.parser')

# picContent = picSoup.find('div', class_='map')



#embed
coronaInfo = Embed(title="Corona numbers Ostallgäu", colour=Colour(0x7ed321), url="https://www.corona-in-zahlen.de/landkreise/lk%20ostallg%C3%A4u/", description="All current important corona numbers in Ostallgäu.")

#coronaInfo.set_image(url="https://cdn.discordapp.com/embed/avatars/0.png")
#coronaInfo.set_thumbnail(url="https://www.links-bewegt.de/kontext/controllers/image.php/o/220")

coronaInfo.set_footer(text=curDate.text)

coronaInfo.add_field(name="Population", value=str(info['population']))
coronaInfo.add_field(name="Infections", value=str(info['infections']))
coronaInfo.add_field(name="Infectionrate", value=str(info['infectionrate']))
coronaInfo.add_field(name="New cases", value=str(info['new cases']))
coronaInfo.add_field(name="Deaths", value=str(info['deaths']))
coronaInfo.add_field(name="Mortality rate", value=str(info['mortalityrate']))


async def coronaInfoEmbed(message):    #returns Embed
    channel = get_tChannel_by_name(message.guild, "covid-19")
    if message.channel == channel:
        if message.content.replace(" ", "").lower() in coronaWords:
            await message.channel.send(embed=coronaInfo)

#TODO: screenshot from statistic e.g. from https://experience.arcgis.com/experience/478220a4c454480e823b17327b2bf1d4/page/page_1/
    #than substitute discord avater

    #more options than ostallgäu