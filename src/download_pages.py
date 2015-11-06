import scrapy
from URLset import URLset
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

url_set = []

def page_urls():
    global url_set
    for list in URLset:
        data = URLset[list]
        server = data['server']
        path = data['path']
        query = data['query']
        keys = data['keys']
        for key in keys:
            url_set.append(server + path + '?' + query % key)

def get_filename(res):
    if 'coursedetails' in res.url:
        if 'COSC' in res.url:
            fname = '../data/COSCcourses.html'
        else:
            fname = '../data/COIScourses.html'
    elif 'ViewSched' in res.url:
        if 'PCCOS' in res.url:
            fname = '../data/COSCclasses.html'
        else:
            fname = '../data/COISclasses.html'
    elif 'position' in res.url:
        if 'COSC' in res.url:
            fname = '../data/COSCstaff.html'
        else:
            fname = '../data/COISstaff.html'
    else:
        fname = 'unknown.html'
    return fname

class ACCspider(scrapy.Spider):
    name='CIS'
    allowed_domains = 'austincc.edu'
    page_urls()
    ID = 0
    start_urls = url_set

    def parse(self, response):
        fname = get_filename(response)
        with open(fname, 'wb') as f:
            f.write(response.body)

configure_logging()
runner=CrawlerRunner()

@defer.inlineCallbacks
def crawl():
    yield runner.crawl(ACCspider)
    reactor.stop()

crawl()
reactor.run()


