import requests
import lxml.html
import code
from requests_html import HTMLSession

# response = requests.get("https://www.reddit.com/r/news/")
# html = lxml.html.fromstring(response.text)
# articles = html.xpath("//article")
session = HTMLSession()
response = session.get("https://www.reddit.com/r/news/")
response.html.render()

