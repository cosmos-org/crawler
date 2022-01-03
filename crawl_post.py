from TinhTe.bot_tinhte import BotTinhte


def start_crawl():
    a = BotTinhte()
    a.parse()
    print(a.list_url_post)
    for url in a.list_url_post:
        try:
            a.crawl_post_content(url)
            a.crawl_comment(url)
        except:
            print("Loi")
    print(a.list_url_author_new)
    for url in a.list_url_author_new:
        if url not in a.list_url_author_old:
            try:
                a.crawl_author(url)
            except:
                print("Loi")


start_crawl()
