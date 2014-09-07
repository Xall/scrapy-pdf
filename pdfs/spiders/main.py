from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from pdfs.items import PdfsItem

class MySpider(CrawlSpider):
    name = "pdfs"
    allowed_domains = ["forschendes-lernen.de"]
    start_urls = ["http://forschendes-lernen.de"]

    # Follow every link
    rules = (
        Rule(LinkExtractor(allow=('')), callback="parse_items", follow= True),
    )

    def parse_items(self, response):
        items = []
        for link in response.xpath('//a'):
            item = PdfsItem()
            item["title"] = link.select("text()").extract()
            item["link"] = link.select("@href").extract()
            item["page"] = response.url
            # extract returns a unicode list, ''.join converts it into a string
            if "pdf" in ''.join(item["link"]):
                items.append(item)
        return items