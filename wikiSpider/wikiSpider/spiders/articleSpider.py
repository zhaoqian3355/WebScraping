from scrapy.selector import Selector
from scrapy import Spider
from wikiSpider.spiders.items import Article
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

class ArticleSpider(Spider):
    name="article"
    allowed_domains=['en.wikipedia.org']
    start_urls=["http://en.wikipedia.org/wiki/Main_Page",
                  "http://en.wikipedia.org/wiki/Python_%28programming_language%29"]
    rules=[Rule(LinkExtractor(allow=('(/wiki/)((?!:).)*$'),),
                                    follow=True)]

    def parse(self,response):
        try:
            item=Article()
            title=response.xpath("//h1/text()")[0].extract()
            print("parse:Title is: "+title)
            item['title']=title
            return item
        except:
            print("Something is error!")


    def parse_item(self,response):
        try:
            item=Article()
            title=response.xpath("//h1/text()")[0].extract()
            print("Title is: "+title)
            item['title']=title
            return item
        except:
            print("Something is error!")