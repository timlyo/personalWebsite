import json
import os
import sys
from datetime import datetime

import markdown2

ARTICLE_DIRECTORY = "data/articles/"

# https://github.com/trentm/python-markdown2/wiki/Extras
MARKDOWN_EXTRAS = ["fenced-code-blocks", "tables"]


class Article:
	def __init__(self, name):
		"""
		:param name: filename without the extension
		:param kwargs:
		"""
		print("Loading article", name)
		try:
			self.name = name  # name of url (file name without extension)
			self.path = ARTICLE_DIRECTORY + self.name + ".md"
			self.content = open(self.path).read().split("---")  # list of metadata and markdown

			self.metadata = json.loads(self.content[0])

			self.html = None

			self.title = self.get_metadata("title")
			self.outline = self.get_metadata("outline")

			date = [int(x) for x in self.get_metadata("date").split("/")]
			self.date = datetime(date[0], date[1], date[2])

			self.tags = self.get_metadata("tags")

		except BaseException as e:
			print(e)

		finally:
			pass

	def __repr__(self):
		return "{} from {}.md".format(self.title, self.name)

	def get_html(self) -> str:
		if not self.html:
			self.html = markdown2.markdown(self.content[1], extras=MARKDOWN_EXTRAS)
		return self.html

	def get_metadata(self, attribute):
		data = None
		try:
			data = self.metadata[attribute]
		except AttributeError as e:
			print("Failed to get article attribute", attribute, "because", e, file=sys.stderr)
		finally:
			return data


def get_article_by_name(name: str) -> Article:
	# TODO existence check
	return Article(name)


def get_all_articles(sorted=True) -> list:
	articles = []
	for file in os.listdir(ARTICLE_DIRECTORY):
		try:
			file = str(file).replace(".md", "")

			article = Article(file)
			articles.append(article)
		except Exception as e:
			print(e, file=sys.stderr)

	if sorted:
		try:  # fails if date doesn't load
			articles.sort(key=lambda x: x.date, reverse=True)
		except:
			pass

	return articles
