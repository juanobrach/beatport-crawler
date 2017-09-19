# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.


import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.beatport.com/tracks/all?key=8&page=3&genres=12',
    ]

    def parse(self, response):
        for track in response.css('ul.bucket-items'):
           yield {
                'track_id': track.css('li::attr(data-ec-id)').extract_first(),
                'media': track.css('li div.buk-track-artwork-parent a img::attr(href)').extract_first(),
                'name': track.css('li div.buk-track-meta-parent p a span::text').extract(),
            }