import scrapy

class DmozSpoder(scrapy.Spider):
    name='dmoz'
    allow_domains=['dmoz-odp.org']
    start_urls=['http://dmoz-odp.org/Computers/Programming/Languages/Python/Resources/',
                'http://dmoz-odp.org/Computers/Programming/Languages/Python/Books/']

    def parse(self,response):
        filename = response.url.split('/')[-2]
        with open(filename,'wb') as f:
            f.write(response.body)
