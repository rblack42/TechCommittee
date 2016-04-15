import scrapy

DATA_DIR = '/Users/rblack/_projects/TechCommittee/data'

class ClassSpider(scrapy.Spider):
    name = 'clist'
    allowed_domains = ["austincc.edu"]
    start_urls = [
        "file://127.0.0.1" + DATA_DIR + "/COSCclasses.html"
    ]

    def parse(self, response):
        filename = response.url.split('/')[-1]
        base,ext = filename.split('.')
        filename = base + '.data'
        with open(filename, 'wb') as f:
            f.write(response.body)

