# crawler
1. Run tor proxy:
docker-compose -f tor/docker-compose.yml up -d
2. Install env:
pip install -r requirements.txt
3. Change CHROMEDRIVER_PATH in TinhTe/bot_tinhte.py (line 46):
Có thế có bug do phiên bản chromedrive khác với phiên bản chrome trong máy.
4. Run project:
python crawl_post.py