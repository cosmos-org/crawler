import scrapy

from crawl_post.items import CrawlPostItem


def normalize_text(text):
    return '\n'.join(text).strip()


class TinhteSpider(scrapy.Spider):
    name = 'tinhte'
    allowed_domains = ['tinhte.vn']
    starts_url = ['https://tinhte.vn/thread/3-cong-nghe-khong-loi-thoi-tren-may-giat-moi-nguoi-dang-lua-chon-may-giat'
                  '-tren-tieu-chi-nao.3438778/']

    def parse(self, response):
        item = CrawlPostItem()
        item['content'] = normalize_text(response.css('#__next > div.jsx-4091196271.thread-view > div > '
                                                      'div.jsx-3866953344.threadpage.false > '
                                                      'div.jsx-3866953344.section.bg-white.false > '
                                                      'div.jsx-3866953344.fst.false > div > div > '
                                                      'div.jsx-3147581474.thread-view--content-wrapper > article > '
                                                      'div > div::text').extract())
        print(item['content'])
        return item
        pass
