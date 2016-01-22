from tinydb import TinyDB, where
import markdown2

articles_db = TinyDB("data/articles.json")
MARKDOWN_EXTRAS = ["fenced-code-blocks", "tables"]


def get_published():
	return articles_db.search(where("state") == 1)


def get_article_data_by_url(url: str, non_published=False) -> dict:
	"""
	:param url: url of article to get
	:param non_published: whether to return data if article is not in published state
	"""
	if non_published:
		results = articles_db.search(where("url") == url)
	else:
		results = articles_db.search((where("url") == url) & (where("state") == 1))

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
		html = get_file_content(info["html"])
	elif "markdown" in info:
		markdown = get_file_content(info["markdown"])
		html = markdown2.markdown(markdown, extras=MARKDOWN_EXTRAS)

	# Hack for proper bootstrap table rendering
	html = html.replace("<table>", "<table class=\"table\"")
	return html


def get_file_content(filename: str):
	contents = None
	with open("data/articles/" + filename, "r", encoding="utf8") as file:
		contents = file.read()
	return contents
