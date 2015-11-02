import argparse
from multiprocessing import Process

from flask import Flask, render_template, jsonify

from website import articles
from website import system
from website import tagging

app = Flask(__name__)


@app.route("/index")
@app.route("/")
def index():
	return render_template("index.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
	return render_template("contact.html")


@app.route("/_ram")
def get_ram():
	response = {
		"total": round(system.get_total_ram()),
		"server": round(system.get_process_ram()),
		"other": round(system.get_other_ram()),
	}
	return jsonify(response)


@app.route("/_cpu")
def get_cpu():
	response = {
		"percentage": [round(system.get_cpu())]
	}
	return jsonify(response)


# pages
@app.route("/stats")
def stats_page():
	return render_template("stats.html")


@app.route("/projects")
def projects_page():
	return render_template("projects.html")


@app.route("/articles")
def articles_page():
	recentArticles = articles.get_all_articles()
	return render_template("articles.html", articles=recentArticles)


@app.route("/articles/<name>")
def getArticle(name):
	article = articles.get_article_by_name(name)
	print("Displaying {}".format(article))
	return render_template("article.html", article=article)


@app.route("/search")
def getSearchResults():
	return jsonify


if __name__ == "__main__":
	tagger = Process(target=tagging.tag_all_articles)
	# tagger.start()

	parser = argparse.ArgumentParser()
	parser.add_argument("-d", dest="debug", type=bool)
	args = parser.parse_args()

	if args.debug:
		app.debug = True

	app.run()
