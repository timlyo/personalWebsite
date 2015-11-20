import sys
from tinydb import TinyDB, where
import markdown2

articles_db = TinyDB("data/articles.json")


def get_all_articles():
	return articles_db.all()


def get_article_data_by_url(url: str):
	results = articles_db.search(where("url") == url)
	if len(results) == 0:
		raise FileNotFoundError("Error: no article with url " + url)
	elif len(results) == 1:
		return results[0]
	else:
		# TODO handle multiple results case
		return results[0]


def get_article_html(url: str):
	info = get_article_data_by_url(url)
	html = None
	if "html" in info:
		html = get_contents(info["html"])
	elif "markdown" in info:
		markdown = get_contents(info["markdown"])
		html = markdown2.markdown(markdown)
	return html


def get_contents(filename: str):
	contents = None
	with open("data/articles/" + filename, "r", encoding="utf8") as file:
		contents = file.read()
	return contents
