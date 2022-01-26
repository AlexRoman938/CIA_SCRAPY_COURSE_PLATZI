import scrapy

#links: response.xpath('//a[starts-with(@href, "collection") and (parent :: h3 | parent ::h2)]/@href').getall()
#El xpath de arriba es que agarremos las etiqeutas a que tengan una clase href que comienza con collection y tenga como nodo padre a las etiquetas h2 y h3. Asi al final agarrar el href

class SpiderCIA(scrapy.Spider):

    name = 'cia'
    start_urls = [

        'https://www.cia.gov/readingroom/historical-collections'

    ]

    custom_settings = {
         
         'FEED_URI' : 'cia.json',
         'FEED_FORMAT' : 'json',
         'FEED_EXPORT_ENCODING' : 'utf-8'

    }

    def parse(self, response):

        link_declassied = response.xpath('//a[starts-with(@href, "collection") and (parent :: h3 | parent ::h2)]/@href').getall()

        for link in link_declassied:

            yield response.follow(link, callback = self.parse_link)
    
    def parse_link(self, response):
        pass
