import scrapy
from datetime import date

from URLset import URLset
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

BASE_URL = '/Users/rblack/_projects/TechCommittee/src/'

today = date.today()
today = today.strftime("%A %d %B %Y")

HEAD = """Course List
##################

As of: %s

..  csv-table::
    :Header: Course
    :delim: |

""" % today

course_urls = [
    '../data/COSCcourses.html',
    '../data/COIScourses.html'
]

class_urls = [
    '../data/COISclasses.html',
    '../data/COSCclasses.html'
]

staff_urls = [
    '../data/COISstaff.html',
    '../data/COSCstaff.html'
]

url_set = []

def page_urls():
    global url_set
    res = []
    for p in course_urls:
        url = 'file://127.0.0.1' + BASE_URL + p
        res.append(url)
    url_set = res
    print url_set

class ACCspider(scrapy.Spider):
    global url_set
    name='CIS'
    allowed_domains = 'austincc.edu'
    page_urls()
    ID = 0
    start_urls = url_set

    def parse(self, response):
        fname = '../docs/courses' + str(ACCspider.ID) + '.rst'
        print 'parsing:',response.url
        ACCspider.ID += 1
        fout  = open(fname, 'wb')
        if ACCspider.ID == 1:
            head = 'COSC ' + HEAD
        else:
            head = 'COIS ' + HEAD
        fout.write(head)
        sel = response.xpath('//th')
        for s in sel.xpath('.//a/text()'):
            fout.write('    ' + s.extract() + '\n')
        fout.close()

configure_logging()
runner=CrawlerRunner()

@defer.inlineCallbacks
def crawl():
    yield runner.crawl(ACCspider)
    reactor.stop()

crawl()
reactor.run()


