import scrapy


class TracksSpider(scrapy.Spider):
    name = "tracks"
    start_urls = [
        'https://www.beatport.com/tracks/all?&page=100&genres=12&per-page=150',
        'https://www.beatport.com/tracks/all?&page=101&genres=12&per-page=150',
        'https://www.beatport.com/tracks/all?&page=102&genres=12&per-page=150'
    ]

    def parse(self, response):
        mediaUrl = "https://geo-samples.beatport.com/lofi/"
        for track in response.css('ul.bucket-items li'):
           yield {
                'preview': mediaUrl+ track.css('li::attr(data-ec-id)').extract_first() +".LOFI.mp3",
                'track_id': track.css('li::attr(data-ec-id)').extract_first(),
                'cover': track.css(' li div.buk-track-artwork-parent a img.buk-track-artwork::attr(data-src)').extract_first(),
                'name': track.css('li div.buk-track-meta-parent p.buk-track-title a span::text').extract_first(),
                'artist': track.css('li div.buk-track-meta-parent p.buk-track-artists a::text').extract_first(),
                'genre':track.css('li div.buk-track-meta-parent p.buk-track-genre a::text').extract_first(),
                'key':track.css('li div.buk-track-meta-parent p.buk-track-key::text').extract_first(),

            }