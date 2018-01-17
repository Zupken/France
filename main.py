import lxml.html
import scraper as sc
import requests


class Scraping:

    def __init__(self):
        self.url = 'http://www.cenior.fr/auto-entrepreneur-departement-bas-rhin-67/'
        self.data = []

    def get_data(self):
        for number in range(1, 17):
            self.source = requests.get(self.url+str(number)+'/')
            self.tree = lxml.html.fromstring(self.source.content)
            self.etree = self.tree.xpath('//div[@id="departement-content"]/a[@class]')
            for element in self.etree:
                self.location = sc.get_text(element.xpath('./span[@class="ville"]/text()'))
                self.name = sc.get_text(element.xpath('./span[@class="nom"]/text()'))
                self.description = sc.get_text(element.xpath('./span[@class="intitule"]/text()'))
                self.data.append([self.location, self.name, self.description])
        sc.Database(('location', 'name', 'description')).push_data(self.data)


Scraping = Scraping()
Scraping.get_data()
