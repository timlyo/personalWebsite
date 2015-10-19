import os
import sys

import markdown2

ARTICLE_DIRECTORY = "static/articles/"

# https://github.com/trentm/python-markdown2/wiki/Extras
MARKDOWN_EXTRAS = ["fenced-code-blocks", "metadata", "tables", "smarty-pants"]


class Article:
    def __init__(self, file):
        """
        :param file: filename without the extension
        :param kwargs:
        """
        self.file = file
        file = open(ARTICLE_DIRECTORY + self.file + ".md")
        processed = markdown2.markdown(file.read(), extras=MARKDOWN_EXTRAS)

        print(processed.metadata)

        self.title = processed.metadata["title"]
        self.outline = processed.metadata["outline"]
        self.content = processed

        print("Loaded " + self.file)

    def __repr__(self):
        return "{} from {}.md".format(self.title, self.file)


def get_article_by_name(name: str) -> Article:
    # TODO existence check
    return Article(name)


def get_all_articles() -> list:
    articles = []
    for file in os.listdir(ARTICLE_DIRECTORY):
        try:
            file = str(file).replace(".md", "")

            article = Article(file)
            articles.append(article)
        except Exception as e:
            print(e, file=sys.stderr)

    return articles


def get_all_articles_sorted_date():
    pass
