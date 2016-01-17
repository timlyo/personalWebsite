import re
import pyTag

from website import articles


def tag_all_articles():
    for article in articles.get_published():
        with open(article.path) as file:
            tags = article.tags.split(",")
            tags += get_article_tags(article.file.read())
            tagString = "tags:" + str(tags) + "\n"
            print(tagString)
            # content = str(content[:match.start()] + "tags:" + str(tags) + "\n" + content[match.end():])

        with open(article.path, "w") as file:
            file.write(content)

    print("Done tagging")


def get_article_tags(content: str) -> list:
    reader = pyTag.Reader()
    stemmer = pyTag.Stemmer()
    rater = pyTag.Rater(pyTag.weights)

    tagger = pyTag.Tagger(reader, stemmer, rater)
    return tagger(content, 4)
