import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item, Field

"""
    parse course list on ACC website

    <table class="rsMultiTable>
        <tbody>
            <tr>
                <th class="crsTitle">
                    <a name="course_name">Course Title

            <tr class="crsDesc">
                description
"""

YEAR    = 2016
DEPTS   = ['COSC', 'COIS']
BASE_URL = 'http://www3.austincc.edu/it/cms/www/catalog/coursedetails_fox.php'

class CourseItem(Item):
    title = Field()
    description = Field()

class CourseSpider(CrawlSpider):
    name = 'course_spider'
    start_urls = [
        BASE_URL + '?year=%s&deptcode=%s' % (YEAR, DEPTS[0]),
        BASE_URL + '?%sdept=%s' % (YEAR, DEPTS[1])
    ]
    rules =[Rule(SgmlLinkExtractor(callback='parse_data'))]

    def parse_data(self, response):
        for url in response.css('table.entries > tr > th a').extract():
            yield {'course': post_title}


